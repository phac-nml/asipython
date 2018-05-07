"""
Copyright Government of Canada 2018

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
import re
from lxml import etree
from Asi.AsiParsingException import AsiParsingException
from Asi.Definition.LevelDefinition import LevelDefinition
from Asi.Definition.CommentDefinition import CommentDefinition
from Asi.Definition.RangeValue import RangeValue


class XmlAsiTransformer:
    SCORE_RANGE_PATTERN = re.compile("(-INF|\\d+(?:\\.\\d+)?)\\s*TO\\s*(INF|\\d+(?:\\.\\d+)?)\\s*=>\\s*(\\d+)")

    GENE_DEFINITION_XPATH = "/ALGORITHM/DEFINITIONS/GENE_DEFINITION"
    GENE_DEFINITION_NAME_XPATH = "NAME"
    GENE_DEFINITION_DRUGCLASSLIST_XPATH = "DRUGCLASSLIST"
    GENE_MUTATION_COMMENTS_XPATH = "/ALGORITHM/MUTATION_COMMENTS/GENE"
    GENE_MUTATION_COMMENTS_NAME_XPATH = "NAME"
    GENE_RULE_XPATH = "RULE"

    LEVEL_XPATH = "/ALGORITHM/DEFINITIONS/LEVEL_DEFINITION"
    LEVEL_ORDER_XPATH = "ORDER"
    LEVEL_TEXT_XPATH = "ORIGINAL"
    LEVEL_SIR_XPATH = "SIR"

    COMMENT_XPATH = "/ALGORITHM/DEFINITIONS/COMMENT_DEFINITIONS/COMMENT_STRING"
    COMMENT_ID_XPATH = "@id"
    COMMENT_TEXT_XPATH = "TEXT"
    COMMENT_SORT_XPATH = "SORT_TAG"

    GLOBAL_RANGE_XPATH = "/ALGORITHM/DEFINITIONS/GLOBALRANGE"

    DRUG_XPATH = "ALGORITHM/DRUG"
    DRUG_NAME_XPATH = "NAME"
    DRUG_FULLNAME_XPATH = "FULLNAME"

    ALGORITHM_NAME_XPATH = "ALGORITHM/ALGNAME"
    ALGORITHM_VERSION_XPATH = "ALGORITHM/ALGVERSION"
    ALGORITHM_DATE_XPATH = "ALGORITHM/ALGDATE"

    RULE_XPATH = "RULE"
    RULE_CONDITION_XPATH = "CONDITION"
    RULE_COMMENT_XPATH = "ACTIONS/COMMENT/@ref"
    RULE_LEVEL_XPATH = "ACTIONS/LEVEL"
    RULE_SCORERANGE_XPATH = "ACTIONS/SCORERANGE"
    RULE_USE_GLOBALRANGE_PATH = "USE_GLOBALRANGE"

    DRUG_CLASS_XPATH = "/ALGORITHM/DEFINITIONS/DRUGCLASS"
    DRUG_CLASS_NAME_XPATH = "NAME"
    DRUG_CLASS_DRUGLIST_XPATH = "DRUGLIST"

    def __init__(self, validate_xml):
        self.validate_xml = validate_xml

    def transform(self, asi_xml_file):
        root = etree.parse(asi_xml_file)

        if self.validate_xml:
            schema = root.docinfo.internalDTD.system_url
            dtd = None

            module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if schema.split('/')[-1] == '/ASI.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI.dtd")))
            elif schema.split('/')[-1] == '/ASI2.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI2.dtd")))
            elif schema.split('/')[-1] == '/ASI2.1.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI2.1.dtd")))

            if dtd is None or not dtd.validate(root):
                raise AsiParsingException("Not a Stanford resistance analysis XML file")
        
        levels = self.create_level_dict(root)
        comments = self.create_comment_dict(root)

        global_node = root.find(self.GLOBAL_RANGE_XPATH)
        global_range = self.parse_score_range(global_node.text.strip(), levels) if global_node is not None else None

        gene_names = set()

        genes = {}


        return genes

    def create_level_dict(self, root):
        nodes = root.xpath(self.LEVEL_XPATH)
        levels = {}

        for node in nodes:
            order = node.find(self.LEVEL_ORDER_XPATH).text.strip()
            text = node.find(self.LEVEL_TEXT_XPATH).text.strip()
            sir = node.find(self.LEVEL_SIR_XPATH).text.strip()

            level = LevelDefinition(int(order), text, sir)

            levels[order] = level

        return levels

    def create_comment_dict(self, root):
        nodes = root.xpath(self.COMMENT_XPATH)
        comments = {}

        for node in nodes:
            comment_id = node.find(self.COMMENT_ID_XPATH).text.strip()
            text = node.find(self.COMMENT_TEXT_XPATH).text.strip()
            sort = node.find(self.COMMENT_SORT_XPATH).text

            comment = None
            if sort is None:
                comment = CommentDefinition(comment_id, text)
            else:
                comment = CommentDefinition(comment_id, text, int(sort.strip()))

            comments[comment_id] = comment

        return comments

    def parse_score_range(self, score_range, levels):
        range_values = []

        for match in re.finditer(self.SCORE_RANGE_PATTERN, score_range):
            min_score = float('-infinity')
            if match.group(1).strip() != "-INF":
                min_score = float(match.group(1).strip())
            max_score = float('infinity')
            if match.group(2).strip() != "INF":
                max_score = float(match.group(2).strip())

            level = match.group(3).strip()
            if level not in levels:
                raise AsiParsingException("undefined level: %s" % level)

            range_values.append(RangeValue(min_score, max_score, levels.get(level)))

        return range_values

    def parse_drugs(self, root, levels, comments, global_range):
        drugs = {}

        drug_nodes = root.xpath(self.DRUG_XPATH)
        for drug in drug_nodes:
            drug_name = drug.find(self.DRUG_NAME_XPATH).text.strip()
            drug_full_name = None
            if drug.find(self.DRUG_FULLNAME_XPATH).text is not None:
                drug_full_name = drug.find(self.DRUG_FULLNAME_XPATH).text.strip()

            # get all the rules for one drug
            rule_nodes = drug.xpath(self.RULE_XPATH)
            drug_rules = self.parse_rules(rule_nodes, levels, comments, global_range)
            drugs[drug_name] = Drug(drug_name, drug_full_name, drug_rules)

        return drugs

    def parse_rules(self, rule_nodes, levels, comments, global_range):
        drug_rules = []

        for rule in rule_nodes:
            condition = None

        return drug_rules
