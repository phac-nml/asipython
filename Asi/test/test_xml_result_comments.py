"""
Copyright Government of Canada 2019

Written by: Eric Enns, National Microbiology Laboratory, Public Health Agency of Canada

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
from Asi.XML.XmlAsiTransformer import XmlAsiTransformer


class TestXmlResultComments:
    @classmethod
    def setup_class(cls):
        cls.validate_xml = True
        cls.module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def attempt_transformation(self, file_path):
        transformer = XmlAsiTransformer(self.validate_xml)
        fd = open(os.path.join(self.module_path,file_path), "r")
        transformer.transform(fd)

    def test_valid_result_comment(self):
        file_path = "test/data/result_based_comments/KPL_1.0.xml"
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,file_path), "r")
            transformer.transform(fd)
        except Exception as exc:
            print("ex:%s" % str(exc))
            raise exc
        finally:
            fd.close()

    def test_no_result_comment_drug_with_no_name(self):
        file_path = "test/data/result_based_comments/ResultCommentDrugWithNoName.xml"
        try:
            transformer = XmlAsiTransformer(self.validate_xml)
            fd = open(os.path.join(self.module_path,file_path), "r")
            transformer.transform(fd)
        except AsiParsingException as e:
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
