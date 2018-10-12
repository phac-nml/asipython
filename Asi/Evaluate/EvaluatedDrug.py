"""
Copyright Government of Canada 2018

Written by: Matthew Fogel, National Microbiology Laboratory, Public Health Agency of Canada

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this work except in compliance with the License. You may obtain a copy of the
License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from Asi.Definition.LevelDefinitionComparator import LevelDefinitionComparator
from Asi.Definition.LevelDefinition import LevelDefinition
from Asi.Definition.CommentDefinition import CommentDefinition


class EvaluatedDrug():
    """An evaluated Drug"""

    FORMAT = "EvaluatedDrug{Drug: %s, Scored Mutations: %s, Level: %s, Comments: %s}"

    def __init__(self, drug, evaluated_conditions):
        """Requires Drug drug, list evaluated_conditions"""
        self.drug = drug
        self.scored_mutations = set()
        self.level_definitions = set()
        self.comment_definitions = set()
        self.parse_evaluated_conditions(evaluated_conditions)

    def parse_evaluated_conditions(self, evaluated_conditions):
        """Parse list evaluated_conditions"""
        self.evaluated_conditions = evaluated_conditions
        for evaluated_condition in evaluated_conditions:

            self.scored_mutations.update(evaluated_condition.get_evaluator().get_scored_mutations())
            definitions = evaluated_condition.get_definitions()

            for definition in definitions:
                if isinstance(definition, LevelDefinition):  # level definition
                    self.level_definitions.add(definition)
                elif isinstance(definition, CommentDefinition):  # comment definition
                    self.comment_definitions.add(definition)
                else:
                    raise TypeError("Unexpected attribute found for " +
                                    str(definition) +
                                    "expected to be of type LevelDefinition or CommentDefinition")

    def get_evaluated_conditions(self):
        """Returns: list evaluated_conditions"""
        return self.evaluated_conditions

    def get_highest_level_definition(self):
        """Returns: highest level definition in set level_definitions"""
        if len(self.level_definitions) > 1:
            return max(self.level_definitions, key=LevelDefinitionComparator.compare)

        return None

    def get_comment_definitions(self):
        """Returns: set comment_definitions"""
        return self.comment_definitions

    def get_level_definitions(self):
        """Returns: set level_definitions"""
        return self.level_definitions

    def get_scored_mutations(self):
        """Returns: set scored_mutations"""
        return self.scored_mutations

    def get_drug(self):
        """Returns: Drug drug"""
        return self.drug

    def __str__(self):
        highest_lev_def = self.get_highest_level_definition()
        return self.FORMAT % (self.drug,
                              self.scored_mutations,
                              str(highest_lev_def) if highest_lev_def is not None else "",
                              self.comment_definitions)

    def __repr__(self):
        highest_lev_def = self.get_highest_level_definition()
        return self.FORMAT % (self.drug,
                              self.scored_mutations,
                              str(highest_lev_def) if highest_lev_def is not None else "",
                              self.comment_definitions)
