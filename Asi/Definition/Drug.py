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

from Asi.AsiEvaluationException import AsiEvaluationException
from Asi.Evaluate.EvaluatedDrug import EvaluatedDrug


class Drug:

    def __init__(self, name, full_name, rules):
        self.name = name
        self.full_name = full_name
        self.drug_rules = rules

    def get_drug_name(self):
        return self.name

    def get_drug_full_name(self):
        return self.full_name

    def get_drug_rules(self):
        return self.drug_rules

    def evaluate(self, mutations, comparator):
        """Requires a list of mutations and a MutationComparator"""
        evaluated_conditions = list()
        for rule in self.drug_rules:
            try:
                evaluated_conditions.append(rule.evaluate(mutations, comparator))
            except AsiEvaluationException:
                raise
        return EvaluatedDrug(self, evaluated_conditions)

    def __str__(self):
        return self.name
