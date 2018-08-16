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
from Asi.Definition.Rule import Rule
from Asi.AsiEvaluationException import AsiEvaluationException
from Asi.Definition.CommentAction import CommentAction
from Asi.Definition.CommentDefinition import CommentDefinition
from Asi.Definition.Drug import Drug
from Asi.Definition.DrugClass import DrugClass
from Asi.Definition.Gene import Gene
from Asi.Definition.LevelDefinition import LevelDefinition
from Asi.Definition.Rule import Rule
from Asi.Definition.ScoreRangeAction import ScoreRangeAction
from Asi.Evalute.EvaluatedGene import EvaluatedGene
from Asi.Grammar.StringMutationComparator import StringMutationComparator
from Asi.XML.XmlAsiTransformer import XmlAsiTransformer


class RuleTest:

    @classmethod
    def setup_class(cls):
        cls.strict_comparison = False
        cls.validate_xml = True
        cls.gene_name = "RT"
        cls.mutation_comparator = StringMutationComparator(cls.strict_comparison)
        cls.mutation_list = "41L,75MA,98G,100I,90M"
        cls.mutations = (cls.mutations_list).split(",")
        if not cls.mutation_comparator.are_mutations_valid(cls.mutations):
            raise Exception("Mutations are not valid %s" % cls.mutations_list)

    
