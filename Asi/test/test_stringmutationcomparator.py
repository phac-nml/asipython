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


class TestStringMutationComparator:

    @classmethod
    def setup_class(cls):
        cls.strict_comparator = StringMutationComparator(True)
        cls.lenient_comparator = StringMutationComparator(False)

    def test_compare_equals_mutations(self):
        assert self.strict_comparator.compare("41L", "41L") == 1
        assert self.strict_comparator.compare("Y41L", "41L") == 1

        assert self.lenient_comparator.compare("41L", "41L") == 1
        assert self.lenient_comparator.compare("Y41L", "41L") == 1
        assert self.lenient_comparator.compare("Y41LC", "41L") == 1
        assert self.lenient_comparator.compare("Y41L", "41LC") == 1
        assert self.lenient_comparator.compare("Y41LP", "41LC") == 1

    def test_compare_not_equals_mutations(self):
        assert self.strict_comparator.compare("41L", "41P") != 1
        assert self.strict_comparator.compare("41L", "41LP") != 1
        assert self.strict_comparator.compare("Y41L", "41LP") != 1
        assert self.strict_comparator.compare("Y41L", "Y52L") != 1

        assert self.lenient_comparator.compare("Y41L", "41P") != 1
        assert self.lenient_comparator.compare("Y41L", "Y52L") != 1

    def test_create_mutation(self):
        assert self.strict_comparator.create_mutation("41", ["L"]) == "41L"

    def test_invert_mutation(self):
        assert self.strict_comparator.invert_mutation("41L") == "41ACDEFGHIKMNPQRSTVWYZdi"

    def test_is_mutation_valid(self):
        assert self.strict_comparator.is_mutation_valid("41L")
        assert not self.strict_comparator.is_mutation_valid("41X")
        assert not self.strict_comparator.is_mutation_valid("X")

    def test_are_mutation_valid(self):
        assert self.strict_comparator.are_mutations_valid(["41L"])
        assert not self.strict_comparator.are_mutations_valid(["41X"])
