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


class EvaluatedCondition():
    """An evaluated RuleCondition"""

    FORMAT = "EvaluatedCondition{%sstatement: %s,%sdefinitions: %s}"

    def __init__(self, rule_condition, evaluator):
        """Requires a RuleCondition and AsiGrammarAdapter object"""

        self.rule_condition = rule_condition
        self.evaluator = evaluator
        self.definitions = set()

    def add_definition(self, definition):
        """Add definitions to set of definitions"""
        if definition:
            self.definitions.add(definition)

    def get_rule_condition(self):
        """Return RuleCondition rule_condition"""
        return self.rule_condition

    def get_evaluator(self):
        """Return AsiGrammarAdapter evaluator"""
        return self.evaluator

    def get_definitions(self):
        """Return set definitions"""
        return self.definitions

    def __str__(self):
        return self.FORMAT % ("\n\t\t",
                              self.rule_condition,
                              "\n\t\t",
                              self.definitions)

    def __repr__(self):
        return self.FORMAT % ("\n\t\t",
                              self.rule_condition,
                              "\n\t\t",
                              self.definitions)
