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
            transformer = XmlAsiTransformer(False)
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

    def test_bool_result_rule_action_type(self):
        """for ETR drug, drug class NNRTI, for the rule, which is a bool condition, the actions contain as SCORERANGE action"""
        gene_dict = dict()
        transformer = None
        try:
            transformer = XmlAsiTransformer(False)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_invalidRuleActionType.xml"), "r")
            gene_dict = transformer.transform(fd)
        except AsiParsingException as e:
            print("testInvalidRuleActionType AsiParsingException:" + str(e))
            raise e
        except Exception as exc:
            print("testInvalidRuleActionType Exception:" + str(exc))
            raise exc

        try:
            # get Gene
            gene = gene_dict.get(self.gene_name)

            # get set
            drug_classes = gene.get_drug_classes()

            # get DrugClass
            drug_class = None
            for item in drug_classes:
                if item.get_class_name() == "NNRTI":
                    drug_class = item
                    break

            # get Drug
            drug = None
            for item in drug_class.get_drugs():
                if item.get_drug_name() == "ETR":
                    drug = item
                    break

            levels = dict()
            levels["1"] = LevelDefinition(1, "level 1","S")
            levels["2"] = LevelDefinition(1, "level 1", "S")

            score_range_str = "(-INF TO 10 => 1, 11 TO INF  => 2)"
            score_range = transformer.parse_score_range(score_range_str, levels)
            drug_rule = drug.get_drug_rules()[0]
            drug_rule.get_actions().append(ScoreRangeAction(score_range))

            try:
                evaluatedGene = gene.evaluate(self.mutations, self.mutation_comparator)
            except AsiEvaluationException as e:
                print("the action does not support a result of type:" + str(e))
                try:
                    actual_err_message = str(e).index("does not support a result of type")
                except ValueError as v:
                    raise Exception("The following error message was expected: " +
                                    "does not support a result of type\n" +
                                    "Instead received:%s" % (str(e)))
        except AsiParsingException as ape:
            print("testInvalidRuleActionType AsiParsingException (evaluate):" + str(ape))
            raise ape

    def test_float_result_rule_action_type(self):
        """for ETR drug, drug class NNRTI, for the rule, which is a score condition, the actions contain a COMMENT action"""
        gene_dict = dict()
        transformer = None
        try:
            transformer = XmlAsiTransformer(False)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_invalidFloatResultActionType.xml"), "r")
            gene_dict = transformer.transform(fd)
        except AsiParsingException as e:
            print("testInvalidRuleActionType AsiParsingException:" + str(e))
            raise e
        except Exception as exc:
            print("testInvalidRuleActionType Exception:" + str(exc))
            raise exc

        # get Gene
        gene = gene_dict.get(self.gene_name)
        # get set of DrugClass objects
        drug_classes = gene.get_drug_classes()

        # get DrugClass
        drug_class = None
        for item in drug_classes:
            if item.get_class_name() == "NNRTI":
                drug_class = item
                break

        # get Drug
        drug = None
        for item in drug_class.get_drugs():
            if item.get_drug_name() == "ETR":
                drug = item
                break

        # get Rule
        drug_rule = drug.get_drug_rules()[0]
        drug_rule.get_actions().append(CommentAction(CommentDefinition("test","used in Python tests",1)))

        try:
            evaluated_gene = gene.evaluate(self.mutations, self.mutation_comparator)
        except AsiEvaluationException as e:
            print("the action does not support a result of type:\n\t" + str(e))
            actual_err_message = str(e).index("does not support a result of type:")
            assert True == (actual_err_message > -1)

    def test_result_out_of_range(self):
        """for ETR drug, drug class NNRTI, for the second rule, which is a boolean condition the actions contain a SCORERANGE action"""
        gene_dict = dict()
        transformer = None

        try:
            transformer = XmlAsiTransformer(False)
            fd = open(os.path.join(self.module_path,"test/data/HIVDB_evaluationExceptionScoreRangeAction.xml"), "r")
            gene_dict = transformer.transform(fd)
        except AsiParsingException as e:
            print("testInvalidRuleActionType AsiParsingException:" + str(e))
            raise e
        except Exception as exc:
            print("testInvalidRuleActionType Exception:" + str(exc))
            raise exc

        gene = gene_dict.get(self.gene_name)

        try:
            evaluated_gene = gene.evaluate(self.mutations, self.mutation_comparator)
        except AsiEvaluationException as e:
            print("No score range has been defined for a score of\n\t" + str(e))
            actual_err_message = str(e).index("No score range has been defined for a score of:")
            assert True == (actual_err_message > -1)
