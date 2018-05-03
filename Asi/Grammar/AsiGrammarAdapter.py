from Asi.Grammar.Analysis import DepthFirstAdapter
from Asi.Grammar.Node import AAndLogicsymbol, AAtleastSelectstatement2, \
                             AAtleastnotmorethanSelectstatement2, ACondition2, \
                             AExactlySelectstatement2, AExcludestatement, AMaxScoreitem, \
                             ANotmorethanSelectstatement2, AOrLogicsymbol, AResidueResidue, \
                             AResidueinvertResidue, AResiduenotResidue, AScorelist, ASelectlist, \
                             AStatementScoreitem
from Asi.Grammar.utils import Stack


class AsiGrammarAdapter(DepthFirstAdapter):
    TRUE_VALUE = float(0)
    FALSE_VALUE = float(1)
    NOT_SCORED = float('nan')

    def __init__(self, mutation_list, comparator):
        self.stack = Stack()
        self.all_scored_mutations = {}
        self.scored_item_mutations = {}
        self.scored_items = []
        self.mutation_list = mutation_list
        self.comparator = comparator
        self.is_boolean_result = True

    def get_result(self):
        score = self.stack.peek()

        if self.is_boolean_result:
            return score == self.TRUE_VALUE

    def case_aresidueresidue(self, node):
        super().case_aresidueresidue(node)

        self.stack.push(self.FALSE_VALUE)

    def case_aresiduenotresidue(self, node):
        super().case_aresiduenotresidue(node)

        self.stack.push(self.FALSE_VALUE)

    def case_aresidueinvertresidue(self, node):
        super().case_aresidueinvertresidue(node)
        self.stack.push(self.FALSE_VALUE)

    def case_aselectlist(self, node):
        super().case_aselectlist(node)

        self.stack.push(self.sum_values_from_stack(len(node.get_listitems())+ 1))

    def case_aexactlyselectstatement2(self, node):
        super().case_aexactlyselectstatement2(node)

        if self.stack.pop() == node.get_integer().get_text():
            self.stack.push(self.TRUE_VALUE)
        else:
            self.stack.push(self.FALSE_VALUE)

    def case_aatleastselectstatement2(self, node):
        super().case_aatleastselectstatement2(node)
        self.stack.push(self.FALSE_VALUE)

    def case_anotmorethanselectstatement2(self, node):
        super().case_anotmorethanselectstatement2(node)
        self.stack.push(self.FALSE_VALUE)

    def case_aatleastnotmorethanselectstatement2(self, node):
        super().case_aatleastnotmorethanselectstatement2(node)
        self.stack.push(self.FALSE_VALUE)

    def case_ascorelist(self, node):
        super().case_ascorelist(node)
        self.stack.push(self.FALSE_VALUE)

    def case_astatementscoreitem(self, node):
        super().case_astatementscoreitem(node)
        self.stack.push(self.FALSE_VALUE)

    def case_aexcludestatement(self, node):
        super().case_aexcludestatement(node)
        self.stack.push(self.FALSE_VALUE)

    def case_acondition2(self, node):
        super().case_acondition2(node)
        self.stack.push(self.FALSE_VALUE)

    def sum_values_from_stack(self, n):
        summation = 0

        for i in range(0,n):
            value = float(str(self.stack.pop()))
            if value != self.NOT_SCORED:
                summation += value

        return summation

    def max_value_from_stack(self, n):
        max = float('-infinity')

        for i in range(0,n):
            value = float(str(self.stack.pop()))
            if value != self.NOT_SCORED and value > max:
                max = value

        return 0 if max == float('-infinity') else max

