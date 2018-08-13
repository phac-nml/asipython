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
from Asi.Evaluate import EvaluatedCondition
from Asi.Grammar import AsiGrammarAdapter
from Asi import AsiParsingException


class RuleCondition(object):
    DEFAULT_BUFFER_SIZE = 1024

    def __init__(self, statement):
        self.statement = statement
        parser = Parser(Lexer(StringIO(statement)))
        try:
            self.condition_tree = parser.parse()
        except:
            raise ASIParsingException("Invalid condition statement: " + statement)

    def getStatement(self):
        return self.statement

    def evaluate(mutations, comparator):
        adapter = new AsiGrammarAdapter(mutations, comparator)
        self.condition_tree.apply(adapter)
        return EvaluatedCondition(self, adapter)

    def __str__(self):
        return self.statement
