"""
Copyright Government of Canada 2018

Written by: Eric Enns and Matthew Fogel, National Microbiology Laboratory,
            Public Health Agency of Canada

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
from Asi.Definition.Drug import Drug
from Asi.Definition.RuleCondition import RuleCondition
from Asi.Definition.Rule import Rule
from Asi.Definition.ScoreRangeAction import ScoreRangeAction
from Asi.Definition.CommentAction import CommentAction
from Asi.Definition.LevelAction import LevelAction
from Asi.Definition.DrugClass import DrugClass
from Asi.Definition.Gene import Gene


class XmlAsiTransformer:
    """XmlAsiTransformer"""
    SCORE_RANGE_PATTERN = \
        re.compile("(-INF|\\d+(?:\\.\\d+)?)\\s*TO\\s*(INF|\\d+(?:\\.\\d+)?)\\s*=>\\s*(\\d+)")

    GENE_DEFINITION_XPATH = "/ALGORITHM/DEFINITIONS/GENE_DEFINITION"
    GENE_DEFINITION_NAME_XPATH = "NAME"
    # pylint: disable=invalid-name
    GENE_DEFINITION_DRUGCLASSLIST_XPATH = "DRUGCLASSLIST"
    # pylint: disable=invalid-name
    GENE_MUTATION_COMMENTS_XPATH = "/ALGORITHM/MUTATION_COMMENTS/GENE"
    GENE_MUTATION_COMMENTS_NAME_XPATH = "NAME"
    GENE_RULE_XPATH = "RULE"

    LEVEL_XPATH = "/ALGORITHM/DEFINITIONS/LEVEL_DEFINITION"
    LEVEL_ORDER_XPATH = "ORDER"
    LEVEL_TEXT_XPATH = "ORIGINAL"
    LEVEL_SIR_XPATH = "SIR"

    COMMENT_XPATH = "/ALGORITHM/DEFINITIONS/COMMENT_DEFINITIONS/COMMENT_STRING"
    COMMENT_ID_XPATH = "id"
    COMMENT_TEXT_XPATH = "TEXT"
    COMMENT_SORT_XPATH = "SORT_TAG"

    GLOBAL_RANGE_XPATH = "/ALGORITHM/DEFINITIONS/GLOBALRANGE"

    DRUG_XPATH = "/ALGORITHM/DRUG"
    DRUG_NAME_XPATH = "NAME"
    DRUG_FULLNAME_XPATH = "FULLNAME"

    ALGORITHM_XPATH = "/ALGORITHM"
    ALGORITHM_NAME_XPATH = "ALGNAME"
    ALGORITHM_VERSION_XPATH = "ALGVERSION"
    ALGORITHM_DATE_XPATH = "ALGDATE"

    RULE_XPATH = "RULE"
    RULE_CONDITION_XPATH = "CONDITION"
    RULE_COMMENT_XPATH = "ACTIONS/COMMENT"
    RULE_COMMENT_REF_XPATH = "ref"
    RULE_LEVEL_XPATH = "ACTIONS/LEVEL"
    RULE_SCORERANGE_XPATH = "ACTIONS/SCORERANGE"
    RULE_USE_GLOBALRANGE_PATH = "USE_GLOBALRANGE"

    DRUG_CLASS_XPATH = "/ALGORITHM/DEFINITIONS/DRUGCLASS"
    DRUG_CLASS_NAME_XPATH = "NAME"
    DRUG_CLASS_DRUGLIST_XPATH = "DRUGLIST"

    def __init__(self, validate_xml):
        """Requires a bool argument indicating whether xml should be validated.
           To see more specific errors turn xml validation off."""
        self.validate_xml = validate_xml

    # pylint: disable=too-many-locals,c-extension-no-member
    def transform(self, asi_xml_file):
        """Transform an xml file"""
        root = etree.parse(asi_xml_file)
        if self.validate_xml:
            schema = root.docinfo.internalDTD.system_url
            dtd = None

            module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if schema.split('/')[-1] == 'ASI.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI.dtd")))
            elif schema.split('/')[-1] == 'ASI2.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI2.dtd")))
            elif schema.split('/')[-1] == 'ASI2.1.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI2.1.dtd")))

            if dtd is None or not dtd.validate(root):
                raise AsiParsingException("Not a Stanford resistance analysis XML file")

        levels = self.create_level_dict(root)
        comments = self.create_comment_dict(root)

        global_node = self.select_unique_single_node(root, self.GLOBAL_RANGE_XPATH)
        global_range = self.parse_score_range(global_node.text.strip(), levels) \
            if global_node is not None else None
        drugs = self.parse_drugs(root, levels, comments, global_range)
        drug_classes = self.parse_drug_classes(root, drugs)

        gene_evaluated_drugs = self.parse_genes(root, drug_classes)
        gene_names_drugs = set(gene_evaluated_drugs.keys())

        gene_evaluated_mutation_comments = \
            self.parse_gene_mutation_comments(root, levels, comments, global_range)
        gene_names_comments = set(gene_evaluated_mutation_comments.keys())

        intersection = gene_names_drugs.intersection(gene_names_comments)
        if len(intersection) < len(gene_names_comments):
            raise AsiParsingException("Some genes defined in MUTATION_COMMENTS," +
                                      " have no corresponding GENE_DEFINITION.")

        gene_names = set()
        gene_names.update(gene_names_drugs)
        gene_names.update(gene_names_comments)

        genes = {}

        for gene_name in gene_names:
            # for every gene
            gene_drug_class = gene_evaluated_drugs.get(gene_name)
            gene_mutation_comments = gene_evaluated_mutation_comments.get(gene_name)
            if gene_mutation_comments is None:
                genes[gene_name] = Gene(name=gene_name,
                                        drug_classes=gene_drug_class.get_drug_classes(),
                                        gene_rules=list())
            else:
                genes[gene_name] = Gene(name=gene_name,
                                        drug_classes=gene_drug_class.get_drug_classes(),
                                        gene_rules=gene_mutation_comments.get_rules())

        return genes

    def create_level_dict(self, root):
        """Create level dictionary.
           Params: ElementTree root
           Returns: dict levels"""
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
        """Create comment dictionary.
           Params: ElementTree root
           Returns: dict comments"""
        nodes = root.xpath(self.COMMENT_XPATH)
        comments = {}

        for node in nodes:
            comment_id = node.get(self.COMMENT_ID_XPATH)
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
        """Parse score range.
           Params: str score_range, dict levels
           Returns: list range_values"""
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
        """Parse drugs.
           Params: ElementTree root, dict levels, dict comments, list global_range.
           Returns: dict drugs"""
        drugs = {}
        drug_nodes = root.xpath(self.DRUG_XPATH)
        for drug in drug_nodes:
            drug_name = drug.find(self.DRUG_NAME_XPATH).text.strip()
            drug_full_name = None
            if drug.find(self.DRUG_FULLNAME_XPATH) is not None:
                drug_full_name = drug.find(self.DRUG_FULLNAME_XPATH).text.strip()

            # get all the rules for one drug
            rule_nodes = drug.xpath(self.RULE_XPATH)
            drug_rules = self.parse_rules(rule_nodes, levels, comments, global_range)
            drugs[drug_name] = Drug(drug_name, drug_full_name, drug_rules)

        return drugs

    def parse_rules(self, rule_nodes, levels, comments, global_range):
        """Parse rules.
           Params: list rule_nodes, dict levels, dict comments, list global_range.
           Returns: list drug_rules"""
        drug_rules = []
        for rule in rule_nodes:
            condition = RuleCondition(rule.find(self.RULE_CONDITION_XPATH).text.strip())
            rule_actions = list()
            # attempt to retrieve all of the possible action nodes
            # (e.g. comment, score range, level)
            comment_node = self.select_unique_single_node(rule, self.RULE_COMMENT_XPATH)
            level_node = self.select_unique_single_node(rule, self.RULE_LEVEL_XPATH)
            score_range_node = self.select_unique_single_node(rule, self.RULE_SCORERANGE_XPATH)

            if comment_node is not None:
                definition = \
                    self.get_required_definition(comments,
                                                 comment_node.get(self.RULE_COMMENT_REF_XPATH))
                rule_actions.append(CommentAction(definition))
            if level_node is not None:
                definition = self.get_required_definition(levels, level_node)
                rule_actions.append(LevelAction(definition))
            if score_range_node is not None:
                # If a global range reference exists map to the global range
                # else parse out a new range
                score_range = list()
                if len(score_range_node.xpath(self.RULE_USE_GLOBALRANGE_PATH)) == 1:
                    if global_range is None:
                        raise AsiParsingException("required global range does not exist: " +
                                                  str(score_range_node.tag))
                    score_range = global_range
                else:
                    score_range = self.parse_score_range(score_range_node.text.strip(), levels)
                rule_actions.append(ScoreRangeAction(score_range))
            if comment_node is None and level_node is None and score_range_node is None:
                raise AsiParsingException("no action exists for rule: " +
                                          str(rule.tag) +
                                          "\n" +
                                          condition.get_statement())
            drug_rules.append(Rule(condition, rule_actions))

        return drug_rules

    def parse_drug_classes(self, root, drugs):
        """Parse drug classes
           Params: ElementTree root, dict drugs
           Returns: dict drug_classes"""
        tag_defined_drug_names = set()
        tag_defined_drug_names.update(set(drugs.keys()))

        drug_classes = dict()
        nodes = root.xpath(self.DRUG_CLASS_XPATH)
        # for every drug class node create a DrugClass object
        for drug_class_node in nodes:
            class_name = self.select_unique_single_node(drug_class_node,
                                                        self.DRUG_CLASS_NAME_XPATH).text.strip()
            drug_list_str = \
                self.select_unique_single_node(drug_class_node,
                                               self.DRUG_CLASS_DRUGLIST_XPATH).text.strip()
            drug_names = drug_list_str.split(",")

            drug_list = set()
            for i, _ in enumerate(drug_names):
                drug = drugs.get(drug_names[i].strip())
                if drug is None:
                    raise AsiParsingException(drug_names[i].strip() +
                                              " has not been defined as a drug.")
                if not self.is_unique_defined_drug(drug.get_drug_name(), drug_classes):
                    raise AsiParsingException("The drug: " +
                                              drug.get_drug_name() +
                                              "; has been defined for more than one drug class.")

                # remove the valid drug from the drug list defined in DRUG tags
                tag_defined_drug_names.remove(drug.get_drug_name())
                drug_list.add(drug)

            drug_classes[class_name] = DrugClass(class_name, drug_list)

        # some drugs defined in DRUG tags are not associated with any class

        if tag_defined_drug_names:
            raise AsiParsingException("The following drugs have not been associated" +
                                      " with a drug class: " +
                                      str(tag_defined_drug_names))

        return drug_classes

    def parse_genes(self, root, drug_classes):
        """Parses genes
           Params: ElementTree root
           Returns: dict drug_classes"""
        nodes = root.xpath(self.GENE_DEFINITION_XPATH)
        if nodes is None:
            raise AsiParsingException("no gene specified")

        genes = dict()

        # Create a map of genes. Every gene has associated a list of DrugClass objects
        for node in nodes:
            gene_name = node.find(self.GENE_DEFINITION_NAME_XPATH).text.strip()
            # get the names of drug drug_classes
            drug_class_list_nodes = node.xpath(self.GENE_DEFINITION_DRUGCLASSLIST_XPATH)
            if len(drug_class_list_nodes) > 1:
                raise AsiParsingException("duplicate node " +
                                          self.GENE_DEFINITION_DRUGCLASSLIST_XPATH)

            drug_class_set = set()
            if len(drug_class_list_nodes) == 1:
                drug_class_list_str = (drug_class_list_nodes[0]).text.strip()
                if drug_class_list_str.strip() == "":
                    raise AsiParsingException("drug class list missing for gene " + gene_name)
                drug_class_names = drug_class_list_str.split(",")

                # create the drug class list

                for i, _ in enumerate(drug_class_names):
                    drug_class_set.add(drug_classes.get(drug_class_names[i].strip()))

            genes[gene_name] = Gene(name=gene_name, drug_classes=drug_class_set)

        return genes

    def parse_gene_mutation_comments(self, root, levels, comments, global_range):
        """Get all the gene nodes specified in GENE_MUTATION_COMMENTS
           Params: ElementTree root, dict levels, dict comments, dict global_range
           Returns: dict genes"""
        nodes = root.xpath(self.GENE_MUTATION_COMMENTS_XPATH)
        genes = dict()

        # for every gene node
        for gene_node in nodes:
            gene_name_node = self.select_unique_single_node(gene_node,
                                                            self.GENE_MUTATION_COMMENTS_NAME_XPATH)

            # if no gene name throw an AsiParsingException
            if gene_name_node is None:
                raise AsiParsingException("no gene name")

            # get the gene rules
            gene_rule_nodes = gene_node.xpath(self.GENE_RULE_XPATH)

            if gene_rule_nodes is None:
                # no rules for the current gene
                raise AsiParsingException("no rule for gene " + gene_name_node)

            gene_name = gene_name_node.text.strip()
            gene_rules = self.parse_rules(gene_rule_nodes, levels, comments, global_range)

            # for every gene rule
            genes[gene_name] = Gene(name=gene_name, gene_rules=gene_rules)

        return genes

    # pylint: disable=no-self-use
    def is_unique_defined_drug(self, drug_name, drug_classes):
        """Search for every class if the drug is already associated with a different one
           Params: str drug_name, dict drug_classes
           Returns: bool is_unique"""
        for class_name in set(drug_classes.keys()):
            # get the DrugClass
            drug_class = drug_classes.get(class_name)
            # get the set of drugs
            drug_list = drug_class.get_drugs()
            # for every drug of the class
            for drug in drug_list:
                if drug_name == drug.get_drug_name():
                    return False

        return True

    # pylint: disable=no-self-use
    def select_unique_single_node(self, parent, xpath):
        """Select unique single node
           Params: ElementTree parent, str xpath
           Returns: Element nodes[0]"""
        nodes = parent.xpath(xpath)
        if len(nodes) > 1:
            raise AsiParsingException("unique node: " +
                                      str(xpath) +
                                      ", does not exist within parent: " +
                                      str(parent))
        return None if not nodes else nodes[0]

    # pylint: disable=no-self-use
    def get_required_definition(self, definitions, key):
        """Get required definition
           Params: dict definitions, Element key
           Returns: LevelDefinition or CommentDefinition object"""
        obj = definitions.get(key)
        if obj is None:
            raise AsiParsingException("required definition: " + key + " does not exist.")
        # return the new Definition
        return obj

    def get_algorithm_info(self, asi_xml_file):
        """Return the algoirthm info"""
        root = etree.parse(asi_xml_file)
        if self.validate_xml:
            schema = root.docinfo.internalDTD.system_url
            dtd = None

            module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if schema.split('/')[-1] == 'ASI.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI.dtd")))
            elif schema.split('/')[-1] == 'ASI2.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI2.dtd")))
            elif schema.split('/')[-1] == 'ASI2.1.dtd':
                dtd = etree.DTD(open(os.path.join(module_path, "ASI2.1.dtd")))

            if dtd is None or not dtd.validate(root):
                raise AsiParsingException("Not a Stanford resistance analysis XML file")

        alg_dict = {}
        alg_name_version_date = self.parse_for_alg_name_version_date(root)
        alg_dict["ALGNAME_ALGVERSION_ALGDATE"] = alg_name_version_date
        alg_dict["ALGNAME_ALGVERSION"] = alg_name_version_date

        # get the lowest levelDefinition as defined when the order = 1
        lowest_level_definition = self.create_level_dict(root).get("1")
        lowest_level_original_sir = {}
        lowest_level_original_sir["ORIGINAL"] = lowest_level_definition.get_text()
        lowest_level_original_sir["SIR"] = lowest_level_definition.get_sir()
        alg_dict["ORDER1_ORIGINAL_SIR"] = lowest_level_original_sir

        drug_and_full_names = self.parse_for_drug_and_full_names(root)
        alg_dict["DRUG_FULLNAME"] = drug_and_full_names

        drug_class_and_drugs = self.parse_for_drug_classes_and_drugs(root, drug_and_full_names)
        alg_dict["DRUGCLASS_DRUGLIST"] = drug_class_and_drugs

        gene_and_drug_classes = self.parse_for_gene_and_drug_classes(root, drug_class_and_drugs)
        alg_dict["GENE_DRUGCLASSLIST"] = gene_and_drug_classes

        return alg_dict

    def parse_for_alg_name_version_date(self, root):
        """Traverse through the list of drugs and add them to the list
           Returns: dict with algorithm name, version, and date
           Throws: AsiParsingException"""
        alg_info = {}
        alg_node = self.select_unique_single_node(root, self.ALGORITHM_XPATH)
        alg_name = alg_node.find(self.ALGORITHM_NAME_XPATH).text.strip()
        alg_version = alg_node.find(self.ALGORITHM_VERSION_XPATH).text.strip()

        # must check becaues algorithm version was added later on
        alg_date = "NA"
        if alg_node.find(self.ALGORITHM_DATE_XPATH) is not None:
            alg_date = alg_node.find(self.ALGORITHM_DATE_XPATH).text.strip()

        alg_info["ALGNAME"] = alg_name
        alg_info["ALGVERSION"] = alg_version
        alg_info["ALGDATE"] = alg_date

        return alg_info

    def parse_for_drug_and_full_names(self, root):
        """Traverse through the list of Drugs and add them to the list
        Derived from parse_drugs() above; except that for efficiency we don't want the rules.
        Params: root, dict levels, dict comments, list global_range.
        Returns: a dict[drug_name] = drug_full_name, where drug_name and drug_full_name
        are strings
        Throws: AsiParsingException"""
        drugs = {}

        drug_nodes = root.xpath(self.DRUG_XPATH)
        for drug in drug_nodes:
            drug_name = drug.find(self.DRUG_NAME_XPATH).text.strip()
            drug_full_name = None
            if drug.find(self.DRUG_FULLNAME_XPATH) is not None:
                drug_full_name = drug.find(self.DRUG_FULLNAME_XPATH).text.strip()

            drugs[drug_name] = drug_full_name

        return drugs

    def parse_for_drug_classes_and_drugs(self, root, drugs):
        """Derived from parse_drug_classes() above; except that for efficiency
           we don't want the rules and thus no Drug objects
           Params: root, dict drugs"""
        tag_defined_drug_names = set()
        tag_defined_drug_names.update(set(drugs.keys()))

        drug_classes = {}
        nodes = root.xpath(self.DRUG_CLASS_XPATH)

        # for every drug class node create a DrugClass object
        for drug_class_node in nodes:
            class_name = self.select_unique_single_node(drug_class_node,
                                                        self.DRUG_CLASS_NAME_XPATH).text.strip()
            drug_list_str = \
                self.select_unique_single_node(drug_class_node,
                                               self.DRUG_CLASS_DRUGLIST_XPATH).text.strip()
            drug_names = drug_list_str.split(",")

            drug_list = set()
            for element in drug_names:
                drug_name = element.strip()
                # check if the drug_name is in dict drugs
                if drug_name not in drugs:
                    raise AsiParsingException(drug_name +
                                              " has not been defined as a drug.")
                if not self.is_unique_defined_drug_2(drug_name, drug_classes):
                    raise AsiParsingException("The drug: " +
                                              drug_name +
                                              "; has been defined for more than one drug class.")

                # remove the valid drug from the drug list defined in DRUG tags
                tag_defined_drug_names.remove(drug_name)
                drug_list.add(drug_name)

            drug_classes[class_name] = drug_list

        # some drugs defined in DRUG tags are not associated with any class

        if tag_defined_drug_names:
            raise AsiParsingException("The following drugs have not been associated" +
                                      " with a drug class: " +
                                      str(tag_defined_drug_names))

        return drug_classes

    # pylint: disable=no-self-use
    def is_unique_defined_drug_2(self, in_drug_name, drug_classes):
        """Search for every class if the drug is already associated with a different one
           Derived from is_unique_defined_drug above; except that for efficiency we don't
           want the rules and thus no Drug objects
           Params: str drug_name, dict drug_classes
           Returns: bool is_unique"""
        for class_name in set(drug_classes.keys()):
            # get the set of drugs
            drug_list = drug_classes.get(class_name)
            # for every drug of the class
            if in_drug_name in drug_list:
                return False

        return True

    def parse_for_gene_and_drug_classes(self, root, drug_classes):
        """Parses genes
           Derived from parse_genes() above; except that for efficiency we don't
           want the rules and thus no Drug objects.
           Params: root
           Returns: dict drug_classes"""
        nodes = root.xpath(self.GENE_DEFINITION_XPATH)
        if nodes is None:
            raise AsiParsingException("no gene specified")

        genes = dict()

        # Create a dict of genes. Every gene has associated a list of DrugClass objects
        for node in nodes:
            gene_name = node.find(self.GENE_DEFINITION_NAME_XPATH).text.strip()
            # get the names of drug drug_classes
            drug_class_list_nodes = node.xpath(self.GENE_DEFINITION_DRUGCLASSLIST_XPATH)
            if len(drug_class_list_nodes) > 1:
                raise AsiParsingException("duplicate node " +
                                          self.GENE_DEFINITION_DRUGCLASSLIST_XPATH)

            drug_class_set = set()
            if len(drug_class_list_nodes) == 1:
                drug_class_list_str = (drug_class_list_nodes[0]).text.strip()
                if drug_class_list_str.strip() == "":
                    raise AsiParsingException("drug class list missing for gene " + gene_name)
                drug_class_names = drug_class_list_str.split(",")

                # create the drug class list

                for i, _ in enumerate(drug_class_names):
                    drug_class_name = drug_class_names[i].strip()
                    if drug_class_name in drug_classes:
                        drug_class_set.add(drug_class_name)
                    else:
                        raise AsiParsingException(drug_class_name + " has not been defined as" +
                                                  " a drug_class.")

            genes[gene_name] = drug_class_set

        return genes
