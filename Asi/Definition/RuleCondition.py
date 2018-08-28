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

from io import StringIO
from Asi.Grammar.Lexer import Lexer
from Asi.Grammar.Parser import Parser
from Asi.Evaluate.EvaluatedCondition import EvaluatedCondition
from Asi.Grammar.AsiGrammarAdapter import AsiGrammarAdapter
from Asi.AsiParsingException import AsiParsingException


class RuleCondition:
    """RuleCondition"""

    def __init__(self, statement):
        """Param: str statement"""
        self.statement = statement
        parser = Parser(Lexer(StringIO(str(statement))))
        try:
            self.condition_tree = parser.parse()
        except Exception:
            raise AsiParsingException("Invalid condition statement: " + statement)

    def get_statement(self):
        """Returns: str statement"""
        return self.statement

    def evaluate(self, mutations, comparator):
        """Requires a list of mutations and a StringMutationComparator"""
        adapter = AsiGrammarAdapter(mutations, comparator)
        self.condition_tree.apply(adapter)
        return EvaluatedCondition(self, adapter)

    def __str__(self):
        return "RuleCondition{%s}" % self.statement

    def __repr__(self):
        return "RuleCondition{%s}" % self.statement
