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

from Asi.AsiEvaluationException import AsiEvaluationException
from Asi.Evaluate.EvaluatedDrugClass import EvaluatedDrugClass


class DrugClass:
    """DrugClass"""

    def __init__(self, name, drugs):
        """Params: str name, set drugs"""
        self.name = name
        self.drugs = drugs

    def get_class_name(self):
        """Returns: str name"""
        return self.name

    def get_drugs(self):
        """Returns: set drugs"""
        return self.drugs

    def __str__(self):
        return "DrugClass{%s}" % self.name

    def __repr__(self):
        return "DrugClass{%s}" % self.name

    def evaluate(self, mutations, comparator):
        """Requires a list of mutations and a StringMutationComparator"""
        evaluated_drugs = list()
        for drug in self.drugs:
            try:
                evaluated_drugs.append(drug.evaluate(mutations, comparator))
            except AsiEvaluationException as exc:
                raise exc
        return EvaluatedDrugClass(self, evaluated_drugs)
