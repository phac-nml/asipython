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


class EvaluatedGene():
    """An evaluated Gene"""

    FORMAT = "EvaluatedGene{Gene: %s, Evaluated Drug Classes: %s, Gene Comments: %s}"

    def __init__(self, gene, gene_evaluated_conditions, evaluated_drug_classes):
        """Requires a Gene and two Lists"""
        self.gene = gene
        self.evaluated_drug_classes = evaluated_drug_classes
        self.gene_scored_mutations = set()
        self.gene_comment_definitions = set()
        self.parese_gene_comment_definitions(gene_evaluated_conditions)

    def parese_gene_comment_definitions(self, gene_evaluated_conditions):
        """Requires a list of EvaluatedCondition objects"""
        self.gene_evaluated_conditions = gene_evaluated_conditions
        for evaluated_condition in gene_evaluated_conditions:
            self.gene_scored_mutations.update(
                evaluated_condition.get_evaluator().get_scored_mutations())
            self.gene_comment_definitions.update(evaluated_condition.get_definitions())

    def get_gene_evaluated_conditions(self):
        """Returns: list of EvaluatedCondition gene_evaluated_conditions"""
        return self.gene_evaluated_conditions

    def get_gene_scored_mutations(self):
        """Returns: set gene_scored_mutations"""
        return self.gene_scored_mutations

    def get_gene_comment_definitions(self):
        """Returns: set gene_comment_definitions"""
        return self.gene_comment_definitions

    def get_gene(self):
        """Returns: Gene gene"""
        return self.gene

    def get_evaluated_drug_classes(self):
        """Returns: list evaluated_drug_classes"""
        return self.evaluated_drug_classes

    def __str__(self):
        return self.FORMAT % (self.gene, self.evaluated_drug_classes, self.gene_comment_definitions)

    def __repr__(self):
        return self.FORMAT % (self.gene, self.evaluated_drug_classes, self.gene_comment_definitions)
