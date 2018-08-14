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

from Asi.Evaluate.EvaluatedDrugClass import EvaluatedDrugClass


class DrugClass(object):

    def __init__(self, name, drugs):
        self.name = name
        self.drugs = drugs

    def get_class_name(self):
        return self.name

    def get_drugs(self):
        return self.drugs

    def __str__(self):
        return self.name

    def evaluate(self, mutations, comparator):
        evaluated_drugs = list()
        for drug in self.drugs:
            try:
                evaluated_drugs.add(drug.evaluate(mutations, comparator))
            except Exception as e:
                raise("Exception occured on line 39 of DrugClass.py:\n%s" % e)
        return EvaluatedDrugClass(self, evaluated_drugs)
