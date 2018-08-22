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

import os
from Asi.AsiEvaluationException import AsiEvaluationException
from Asi.AsiParsingException import AsiParsingException
from Asi.Definition.Gene import Gene
from Asi.Evaluate.EvaluatedGene import EvaluatedGene
from Asi.Grammar.StringMutationComparator import StringMutationComparator
from Asi.XML.XmlAsiTransformer import XmlAsiTransformer

class TestDrug:

    @classmethod
    def setup_class(cls):
        cls.strict_comparison = False
        cls.validate_xml = False
        cls.gene_name = "RT"
        cls.mutation_comparator = StringMutationComparator(cls.strict_comparison)
        cls.mutation_list = "41L,75MA,98G,100I,90M"
        cls.set_mutations(cls, cls.mutation_list, cls.mutation_comparator)
        cls.module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def set_mutations(cls, mutations_string, comparator):
        """Requires string MutataionsString and MutationComparator"""
        cls.mutations = mutations_string.split(",")
        if not comparator.are_mutations_valid(cls.mutations):
            raise Exception("Mutations are not valid %s" % cls.mutations_string)

    
