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


class EvaluatedDrugClass():
    """An evaluated Drug Class"""

    FORMAT = "EvaluatedDrugClass{Drug Class: %s, Evaluated Drugs: %s}"

    def __init__(self, drug_class, evaluated_drugs):
        """Requires: DrugClass drug_class, list of EvaluatedDrugs evaluated_drugs"""
        self.drug_class = drug_class
        self.evaluated_drugs = evaluated_drugs

    def get_drug_class(self):
        """Returns: DrugClass drug_class"""
        return self.drug_class

    def get_evaluated_drugs(self):
        """Returns: list of EvaluatedDrugs evaluated_drugs"""
        return self.evaluated_drugs

    def __str__(self):
        return self.FORMAT % (self.drug_class, self.evaluated_drugs)

    def __repr__(self):
        return self.FORMAT % (self.drug_class, self.evaluated_drugs)
