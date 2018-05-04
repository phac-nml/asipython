from io import StringIO
from Asi.Grammar.AsiGrammarAdapter import AsiGrammarAdapter
from Asi.Grammar.Lexer import Lexer
from Asi.Grammar.Parser import Parser


class AsiGrammarTestHelper:

    @classmethod
    def apply_statement(cls, statement, mutations, comparator):
        parser = Parser(Lexer(StringIO(statement)))
        tree = parser.parse()
        adapter = AsiGrammarAdapter(mutations, comparator)
        tree.apply(adapter)
        return adapter
