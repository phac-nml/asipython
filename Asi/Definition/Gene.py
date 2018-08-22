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
from Asi.Evaluate.EvaluatedGene import EvaluatedGene


class Gene(object):

    def __init__(self, name, drug_classes=None, gene_rules=None):
        self.name = name

        if drug_classes==None and gene_rules==None:
            raise Exception("User must pass as an argument at least one of" +
                            " drug_classes or gene_rules.")

        if drug_classes:
            self.drug_classes = drug_classes
        else:
            self.drug_classes = set()

        if gene_rules:
            self.gene_rules = gene_rules
        else:
            self.gene_rules = list()

    def get_name(self):
        return self.name

    def get_drug_classes(self):
        return self.drug_classes

    def get_rules(self):
        return self.gene_rules

    def __str__(self):
        return self.name

    def evaluate(self, mutations, comparator):
        """Requires a list of mutations and a MutationComparator"""
        evaluated_gene_rules = list()
        for gene_rule in self.gene_rules:
            try:
                evaluated_gene_rules.append(gene_rule.evaluate(mutations, comparator))
            except AsiEvaluationException:
                raise

        evaluated_drug_classes = list()
        for drug_class in self.drug_classes:
            try:
                evaluated_drug_classes.append(drug_class.evaluate(mutations, comparator))
            except AsiEvaluationException:
                raise

        return EvaluatedGene(self, evaluated_gene_rules, evaluated_drug_classes)
