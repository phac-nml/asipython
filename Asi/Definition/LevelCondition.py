"""
Copyright Government of Canada 2019

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

from Asi.Definition.LevelConditionComparison import LevelConditionComparison
from Asi.Evaluate.EvaluatedLevelCondition import EvaluatedLevelCondition


class LevelCondition:
    """LevelCondition"""

    def __init__(self):
        self.comparisons = list()

    def add_comparison(self, level_order, comparison_operator):
        """Add a comparison to list of comparisons"""
        self.comparisons.append(LevelConditionComparison(level_order, comparison_operator))

    def evaluate(self, level, drug):
        """Requires a level and drug"""
        result = len(self.comparisons) > 0

        return EvaluatedLevelCondition(self, result, level, drug)
