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
from Asi.Grammar.StringMutationComparator import StringMutationComparator
from Asi.test.helpers.AsiGrammarTestHelper import AsiGrammarTestHelper


class TestSelect:

    @classmethod
    def setup_class(cls):
        cls.comparator = StringMutationComparator(False)
        cls.mutations = ["41L", "50VW", "Q98LRG"]

    def test_select_exactly(self):
        statement = "SELECT EXACTLY 2 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()

    def test_select_at_least(self):
        statement = "SELECT ATLEAST 1 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()

    def test_select_and_at_least(self):
        statement = "50V AND SELECT ATLEAST 1 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()

    def test_select_not_more_than(self):
        statement = "SELECT NOTMORETHAN 1 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() is False

    def test_select_at_least_and_not_more_than(self):
        statement = "SELECT ATLEAST 1 AND NOTMORETHAN 2 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()

    def test_select_at_least_or_not_more_than(self):
        statement = "SELECT ATLEAST 3 OR NOTMORETHAN 2 FROM (41LRGFD, M50WERST, Q98A, 45ALT)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result()


class TestScore:

    @classmethod
    def setup_class(cls):
        cls.comparator = StringMutationComparator(False)
        cls.mutations = ["41L", "50VW", "Q98LRG"]

    def test_score_simple_residue_list(self):
        statement = "SCORE FROM (41(NOTL)=>2.5,50WVA=>2,Q98AST=>10)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == 2.0

    def test_score_exclude_residue_list(self):
        statement = "SCORE FROM (41(NOTL)=>2.5,50W AND EXCLUDE 50VA=>2,Q98AST=>10)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == 0.0

    def test_score_exclude_not_residue_list(self):
        statement = "SCORE FROM (41(NOTL)=>2.5,50W AND EXCLUDE 50(NOTV)=>2,Q98ASRT=>10)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == 10.0

    def test_score_max_residue_list(self):
        statement = "SCORE FROM (MAX (41L => 50, 50N => 100))"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == 50.0

    def test_score_negative_max_residue_list(self):
        statement = "SCORE FROM (MAX (41L => -50, 50N => 100, 50V=>-40))"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == -40.0

    def test_score_neg_max_with_zero_score_residue_list(self):
        statement = "SCORE FROM (MAX (41L => -50, 50V=>0, 50N => 100))"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == 0.0

    def test_score_max_with_no_fired_score(self):
        statement = "SCORE FROM (MAX (41T => -50, 50L=>0, 50N => 100))"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == 0.0

    def test_score_max_eith_boolean_condition(self):
        statement = "SCORE FROM (MAX (41L => -50, 50N => 100, 100T=>0, 55W=>-40),50V=>3)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == -47.0

    def test_score_sub_condition_select_residue_list(self):
        statement = "SCORE FROM (SELECT ATLEAST 1 FROM (41L, Q98L) AND 50V => -50, 50N => 100)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == -50.0

    def test_score_logic_symbols_residue_list(self):
        statement = "SCORE FROM ((41M OR (Q98L AND 50V)) AND 50V => -50, (SELECT ATLEAST 1 AND" \
                    + " NOTMORETHAN 2 FROM(41L,50VW,45L) AND 50V) AND 41V => 100)"
        adapter = AsiGrammarTestHelper.apply_statement(statement, self.mutations, self.comparator)

        assert adapter.get_result() == -50.0
