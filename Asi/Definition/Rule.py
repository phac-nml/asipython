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

from Asi.AsiParsingException import AsiParsingException
from Asi.AsiEvaluationException import AsiEvaluationException
from Asi.Definition.ScoreRangeAction import ScoreRangeAction


class Rule(object):

    def __init__(self, condition, actions):
        """Requires a RuleCondition argument condition and a list argument actions."""
        if len(actions) == 0:
            raise AsiParsingException("no action exists for the rule:\n%s" %
                                      condition.get_statement())
        elif self.more_than_one_score_range(actions):
            raise AsiParsingException("more than one score range for the rule:\n%s" %
                                      condition.get_statement())
        self.condition = condition
        self.actions = actions

    def get_condition(self):
        return self.condition

    def get_actions(self):
        return self.actions

    def evaluate(self, mutations, comparator):
        """Requires a list of mutations and a MutationComparator"""
        # get the EvaluatedCondition object
        evaluated_condition = self.condition.evaluate(mutations, comparator)
        # get the AsiGrammarAdapter object
        evaluator = evaluated_condition.get_evaluator()
        for action in self.actions:
            if not action.supports(evaluator.get_result()):
                raise AsiEvaluationException("Action: %s; does not support a result of type: %s" %
                                             (action, type(evaluator.get_result())))
            evaluated_condition.add_definition(action.evaluate(evaluator.get_result()))
        return evaluated_condition

    def more_than_one_score_range(actions):
        """Requires a list argument actions"""
        score_range_action_count = 0
        for action in actions:
            if isinstance(action, ScoreRangeAction):
                score_range_action_count += 1
        return score_range_action_count > 1

    def __str__(self):
        return str(self.condition)
