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

    def test_missing_drug_name(self):
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_missingDrugName.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("testMissingDrugName:\n\t%s" % str(e))
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

    def test_undefined_drug_within_a_drug_class(self):
        """DLV drug is missing from NNRTI drug class (the drug is associated with no drug class)"""
        try:
            transformer = XmlAsiTransformer(False)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_undefinedDrugWithinDrugClass.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("testUndefinedDrugWithinADrugClass:\n\t%s" % str(e))
            try:
                actual_err_message = str(e).index("The following drugs have not been associated with a drug class")
            except ValueError as v:
                raise Exception("The following error message was expected: " +
                                "The following drugs have not been associated with a drug class\n" +
                                "Instead received:%s" % (str(e)))
        except Exception as exc:
            print("testUndefinedDrugWithinADrugClass ex:%s" % str(exc))
            raise exc
        finally:
            fd.close()

    def test_defined_drug_within_different_drug_classes(self):
        """DLV drug defined in NNRTI and NRTI drug classes"""
        try:
            transformer = XmlAsiTransformer(False)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_definedDrugWithinDifferentDrugClasses.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("testDefinedDrugWithinDifferentDrugClasses:\n\t%s" % str(e))
            try:
                actual_err_message = str(e).index("has been defined for more than one drug class")
            except ValueError as v:
                raise Exception("The following error message was expected: " +
                                "has been defined for more than one drug class\n" +
                                "Instead received:%s" % (str(e)))
        except Exception as exc:
            print("testDefinedDrugWithinDifferentDrugClasses ex:%s" % str(exc))
            raise exc
        finally:
            fd.close()

    def test_undefined_drug(self):
        """DLV drug is not defined under a DRUG tag"""
        try:
            transformer = XmlAsiTransformer(False)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_undefinedDrug.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("testUndefinedDrug\n\t" + str(e))
            try:
                actual_err_message = str(e).index("has not been defined as a drug")
            except ValueError as v:
                raise Exception("The following error message was expected: " +
                                "has not been defined as a drug\n" +
                                "Instead received:%s" % (str(e)))
        except Exception as exc:
            print("ex:" + str(exc))
            raise exc
        finally:
            fd.close()

    def test_drug_without_any_rule(self):
        """DLV drug does not have defined any rule"""
        try:
            transformer = XmlAsiTransformer(False)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_drugWithoutAnyRule.xml"), "r")
            gene_dict = transformer.transform(fd)
            gene = gene_dict.get(self.gene_name)
            evaluated_gene = gene.evaluate(self.mutations, self.mutation_comparator)
            print("evaluated gene:" + str(evaluated_gene))
        except AsiEvaluationException as e:
            print("no rules for this drug\n\t" + str(e))
            raise e
        except Exception as exc:
            print("testDrugWtihoutAnyRule ex:" + str(exc))
            raise exc
