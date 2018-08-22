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
from Asi.AsiParsingException import AsiParsingException
from Asi.Grammar.StringMutationComparator import StringMutationComparator
from Asi.XML.XmlAsiTransformer import XmlAsiTransformer

class TestXMLDefinitions:
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

    def test_overlapping_ranges(self):
        """Test overlapping ranges"""
        try:
            transformer = XmlAsiTransformer(False)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_overlappingRanges.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("test_overLapping_ranges:\n\t%s" % str(e))
            try:
                actual_err_message = str(e).index("Score range values overlap")
            except ValueError as v:
                raise Exception("The following error message was expected: " +
                                "Score range values overlap\n" +
                                "Instead received:%s" % (str(e)))
        except Exception as exc:
            print("ex:%s" % str(exc))
            raise exc
        finally:
            fd.close()

    def test_multiple_global_range_tags(self):
        """Test multiple global range tags"""
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_multipleGlobalRangeTags.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("test_multiple_global_range_tags:\n\t%s" % str(e))
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

    def test_missing_drug_class_name(self):
        """Test missing drug class name"""
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_missingDrugClassName.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("test_missing_drug_class_name:\n\t%s" % str(e))
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


    def test_missing_drug_class_drug_list(self):
        """Test missing drug class drug list"""
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_missingDrugClassDrugList.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("test_missing_drug_class_drug_list:\n\t%s" % str(e))
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


    def test_multiple_comment_definition_tags(self):
        """Test multiple comment definition tags"""
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_multipleCommentDefinitionTags.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("test_multiple_comment_definition_tags:\n\t%s" % str(e))
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

    def test_missing_level_definition_order(self):
        """Test missing_level_definition_order"""
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_missingLevelDefinitionOrder.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("test_missing_level_definition_order:\n\t%s" % str(e))
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

    def test_missing_level_definition_sir(self):
        """Test missing_level_definition_sir"""
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_missingLevelDefinitionSIR.xml"), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
            print("test_missing_level_definition_sir:\n\t%s" % str(e))
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
