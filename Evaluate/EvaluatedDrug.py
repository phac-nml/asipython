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

import Asi.Definition.CommentDefinition
import Asi.Definition.Drug
import Asi.Definition.LevelDefinition
import Asi.Definition.LevelDefinitionComparator

class EvaluatedDrug(object):

    FORMAT = "{Drug: %s, Scored Mutations: %s, Level: %s, Comments: %s}"

    def __init__(self, drug, evaluated_conditions):
        self.drug = drug
        self.scored_mutations = set()
        self.level_definitions = set()
        self.comment_definitions = set()
        self.parse_evaluated_conditions(evaluated_conditions)

    def parse_evaluated_conditions(self, evaluated_conditions):
        self.evaluated_conditions = evaluated_conditions
        for evaluated_condition in evaluated_conditions:

            self.score_mutations.update(evaluated_condition.get_evaluator().get_scored_mutations())
            definitions = evaluated_condition.get_definitions()

            for definition in definitions:
                if hasattr(definition, 'order'):  # level definition
                    self.level_definitions.add(definition)
                elif hasattr(definition, 'identifier'):  # comment definition
                    self.comment_definitions.add(definition)

    def get_evaluated_conditions(self):
        return self.evaluated_conditions;

    def get_highest_level_definition(self):
        return max(self.level_definitions, key=LevelDefinitionComparator.compare()) \
                   if len(self.level_definitions) > 0 else None

    def get_comment_definitions(self):
        return self.comment_definitions

    def get_level_definitions(self):
        return self.level_definitions

    def get_scored_mutations(self):
        return self.scored_mutations

    def get_drug(self):
        return self.drug

    def to_string(self):
        highest_level_definition = self.get_highest_level_definition()
        level_def == "" if highest_level_definition is None else \
                     str(highest_level_definition)
        return self.FORMAT % (self.drug,
                              self.scored_mutations,
                              level_def,
                              self.comment_definitions)
