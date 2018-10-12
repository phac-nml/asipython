"""
Copyright Government of Canada 2018

Written by: Eric Enns, National Microbiology Laboratory, Public Health Agency of Canada

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this work except in compliance with the License. You may obtain a copy of the
License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import math
from Asi.Grammar.Analysis import DepthFirstAdapter
from Asi.Grammar.Node import AAndLogicsymbol, AMaxScoreitem, AOrLogicsymbol
from Asi.Grammar.utils import Stack


class AsiGrammarAdapter(DepthFirstAdapter):
    """Adapter to evaluate ASI Grammar"""
    TRUE_VALUE = float(1)
    FALSE_VALUE = float(0)
    NOT_SCORED = float('nan')

    def __init__(self, mutation_list, comparator):
        """Params: mutation list and comparator"""
        super().__init__()
        self.stack = Stack()
        self.all_scored_mutations = set()
        self.scored_item_mutations = set()
        self.scored_items = []
        self.mutation_list = mutation_list
        self.comparator = comparator
        self.is_boolean_result = True

    def get_result(self):
        """Get the score"""
        score = self.stack.peek()

        if self.is_boolean_result:
            return score == self.TRUE_VALUE

        return score

    def case_aresidueresidue(self, node):
        """The residue production is used for evaluating whether or not the specified
        residue is IN the mutation list. Given the two properties of the residue
        node, amino acid list and codon number, create a mutation and compare it to
        each element in the list. If the mutation IS found, push TRUE onto the Stack,
        otherwise push FALSE
        """
        super().case_aresidueresidue(node)

        value = self.FALSE_VALUE

        residue = self.comparator.create_mutation(node.get_integer(), node.get_mutatedaminoacid())
        for mutation in self.mutation_list:
            if self.comparator.compare(mutation, residue) == 1:
                value = self.TRUE_VALUE
                self.all_scored_mutations.add(mutation)
                self.scored_item_mutations.add(mutation)
                break
        self.stack.push(value)

    def case_aresiduenotresidue(self, node):
        """TODO: fillme"""
        super().case_aresiduenotresidue(node)

        found_mutation = False

        for mutated_amino_acid in node.get_mutatedaminoacid():
            mutated_amino_acid_list = []
            mutated_amino_acid_list.append(mutated_amino_acid)

            residue = self.comparator.create_mutation(node.get_integer(), mutated_amino_acid_list)

            for mutation in self.mutation_list:
                if self.comparator.compare(mutation, residue) == 1:
                    found_mutation = True
                    break

        if not found_mutation:
            self.stack.push(self.TRUE_VALUE)
            self.all_scored_mutations.add(str(node).strip())
            self.scored_item_mutations.add(str(node).strip())
        else:
            self.stack.push(self.FALSE_VALUE)

    def case_aresidueinvertresidue(self, node):
        """TODO: fillme"""
        super().case_aresidueinvertresidue(node)

        value = self.FALSE_VALUE

        residue = self.comparator.create_mutation(node.get_integer(), node.get_mutatedaminoacid())
        residue = self.comparator.invert_mutation(residue)
        for mutation in self.mutation_list:
            if self.comparator.compare(mutation, residue) == 1:
                value = self.TRUE_VALUE
                self.all_scored_mutations.add(mutation)
                self.scored_item_mutations.add(mutation)
                break

        self.stack.push(value)

    def case_aselectlist(self, node):
        """TODO: fillme"""
        super().case_aselectlist(node)

        self.stack.push(self.sum_values_from_stack(len(node.get_listitems()) + 1))

    def case_aexactlyselectstatement2(self, node):
        """TODO: fillme"""
        super().case_aexactlyselectstatement2(node)

        if self.stack.pop() == float(node.get_integer().get_text()):
            self.stack.push(self.TRUE_VALUE)
        else:
            self.stack.push(self.FALSE_VALUE)

    def case_aatleastselectstatement2(self, node):
        """TODO: fillme"""
        super().case_aatleastselectstatement2(node)

        if self.stack.pop() >= float(node.get_integer().get_text()):
            self.stack.push(self.TRUE_VALUE)
        else:
            self.stack.push(self.FALSE_VALUE)

    def case_anotmorethanselectstatement2(self, node):
        """TODO: fillme"""
        super().case_anotmorethanselectstatement2(node)

        if self.stack.pop() <= float(node.get_integer().get_text()):
            self.stack.push(self.TRUE_VALUE)
        else:
            self.stack.push(self.FALSE_VALUE)

    def case_aatleastnotmorethanselectstatement2(self, node):
        """On the top of the Stack is the value of how many elements are evaluated to TRUE.
        It compares the top of the Stack with the ATLEAST attribute AND/OR the NOTMORETHAN
        attribute. If comparison is evaluated to TRUE, push TRUE otherwise push FALSE.
        """
        super().case_aatleastnotmorethanselectstatement2(node)

        count = int(self.stack.pop())
        is_atleast = count >= int(node.get_atleastnumber().get_text())
        is_notmorethan = count <= int(node.get_notmorethannumber().get_text())

        if isinstance(node.get_logicsymbol(), AAndLogicsymbol) and (is_atleast and is_notmorethan):
            self.stack.push(self.TRUE_VALUE)
        elif isinstance(node.get_logicsymbol(), AOrLogicsymbol) and (is_atleast or is_notmorethan):
            self.stack.push(self.TRUE_VALUE)
        else:
            self.stack.push(self.FALSE_VALUE)

    def case_ascorelist(self, node):
        """The score list production is used to sum the scores represented in the score list.
        The function will iterate through this list, removing each individual score items
        value, and push on the summation
        """
        super().case_ascorelist(node)

        self.is_boolean_result = False
        size = len(node.get_scoreitems()) + 1
        if isinstance(node.get_parent(), AMaxScoreitem):
            self.stack.push(self.max_value_from_stack(size))
        else:
            self.stack.push(self.sum_values_from_stack(size))

    def case_astatementscoreitem(self, node):
        """If the score items residue has evaluated to TRUE, push on the score associated
        with this item, otherwise push on a score of 0.
        """
        super().case_astatementscoreitem(node)

        value = self.stack.pop()
        if value != self.FALSE_VALUE:
            number = float(str(node.get_number()))
            score = number if node.get_min() is None else number * -1
            self.stack.push(score)
            self.scored_items.append(ScoredItem(str(node), self.scored_item_mutations, score))
        else:
            self.stack.push(self.NOT_SCORED)
        self.scored_item_mutations = set()

    def case_aexcludestatement(self, node):
        """If the residue was found in the mutation list, push FALSE onto the Stack,
        otherwise push TRUE (i.e. just invert the truth value on top of the Stack)
        """
        super().case_aexcludestatement(node)

        inverted = int(self.stack.pop()) ^ int(self.TRUE_VALUE)
        self.stack.push(float(inverted))

    def case_acondition2(self, node):
        """Evaluate the top 2 conditions on the Stack using the logic symbol provided, then push
        the resulting truth value back onto the Stack.
        """
        super().case_acondition2(node)

        first = int(self.stack.pop())
        second = int(self.stack.pop())

        if isinstance(node.get_logicsymbol(), AAndLogicsymbol):
            self.stack.push(float(first & second))
        elif isinstance(node.get_logicsymbol(), AOrLogicsymbol):
            self.stack.push(float(first | second))
        else:
            raise RuntimeError("Logic symbol %s was not expected." % node.get_logicsymbol())

    def sum_values_from_stack(self, num_items):
        """Pop off num_items from the Stack, then return the cumulative value"""
        summation = float(0)

        for _ in range(0, num_items):
            value = self.stack.pop()
            # print(value)

            if not math.isnan(value):
                summation += value

        return summation

    def max_value_from_stack(self, num_items):
        """Pop off num_items from the Stack, then return the max value"""
        max_value = float('-infinity')

        for _ in range(0, num_items):
            value = float(str(self.stack.pop()))
            if not math.isnan(value) and value > max_value:
                max_value = value

        return 0 if max_value == float('-infinity') else max_value

    def get_scored_mutations(self):
        """Return all scored mutations"""
        return self.all_scored_mutations


# pylint: disable=too-few-public-methods
class ScoredItem:
    """Object used to store a ScoredItem"""
    def __init__(self, value, mutations, score):
        self.value = value
        self.mutations = mutations
        self.score = score

    def __str__(self):
        """Returns a string representing the ScoredItem."""
        return self.value
