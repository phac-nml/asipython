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
from Asi.Definition.Rule import Rule
from Asi.AsiParsingException import AsiParsingException
from Asi.AsiEvaluationException import AsiEvaluationException
from Asi.Definition.CommentAction import CommentAction
from Asi.Definition.CommentDefinition import CommentDefinition
from Asi.Definition.Drug import Drug
from Asi.Definition.DrugClass import DrugClass
from Asi.Definition.Gene import Gene
from Asi.Definition.LevelDefinition import LevelDefinition
from Asi.Definition.Rule import Rule
from Asi.Definition.ScoreRangeAction import ScoreRangeAction
from Asi.Evaluate.EvaluatedGene import EvaluatedGene
from Asi.Grammar.StringMutationComparator import StringMutationComparator
from Asi.XML.XmlAsiTransformer import XmlAsiTransformer


class TestRule:

    @classmethod
    def setup_class(cls):
        cls.strict_comparison = False
        cls.validate_xml = True
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

    def test_missing_required_rule_elements(self):
        """Test when a rule is missing the condition for DLV drug"""
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_missingCondition.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("CONDITION tag is a required element:\n\t%s" % str(e))
            try:
                actual_err_message = str(e).index("Not a Stanford resistance analysis XML file")
            except ValueError as v:
                raise Exception("The following error message was expected: " +
                                "Not a Stanford resistance analysis XML file\n" +
                                "Instead received:%s" % (str(e)))
        except Exception as exc:
            print("ex:%s" % str(exc))
            raise exc
        finally:
            fd.close()

        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_missingActions.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("ACTIONS tag is a required element:\n\t%s" % str(e))
            try:
                actual_err_message = str(e).index("Not a Stanford resistance analysis XML file")
            except ValueError as v:
                raise Exception("The following error message was expected: " +
                                "Not a Stanford resistance analysis XML file\n" +
                                "Instead received:%s" % (str(e)))
        except Exception as exc:
            print("ex:%s" % str(exc))
            raise exc
        finally:
            fd.close()

    def test_required_global_range(self):
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_missingRequiredGlobalRange.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("GLOBALRANGE tag is a required element (some rules are using USE_GLOBALRANGE tag):\n\t" + str(e))
            try:
                actual_err_message = str(e).index("required global range does not exist")
            except ValueError as v:
                raise Exception("The following error message was expected: " +
                                "required global range does not exist\n" +
                                "Instead received:%s" % (str(e)))
        except Exception as exc:
            print("ex:%s" % str(exc))
            raise exc
        finally:
            fd.close()
