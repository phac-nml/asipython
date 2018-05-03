from Asi.Grammar.AsiGrammarAdapter import AsiGrammarAdapter
from Asi.Grammar.StringMutationComparator import StringMutationComparator
from Asi.test.helpers.AsiGrammarTestHelper import AsiGrammarTestHelper


class TestSelect:
    
    @classmethod
    def setup_class(cls):
        cls.comparator = StringMutationComparator(False)
        cls.mutations = ["41L","50VW","Q98LRG"]

    def test_select_exactly(self):
        statement = "SELECT EXACTLY 2 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()

    def test_select_at_least(self):
        statement = "SELECT EXACTLY 2 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()

    def test_select_and_at_least(self):
        statement = "50V AND SELECT ATLEAST 1 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()

    def test_select_not_more_than(self):
        statement = "SELECT NOTMORETHAN 1 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == False

    def test_select_at_least_and_not_more_than(self):
        statement = "SELECT ATLEAST 1 AND NOTMORETHAN 2 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()

    def test_select_at_least_or_not_more_than(self):
        statement = "SELECT ATLEAST 3 OR NOTMORETHAN 2 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()
