from Asi.Grammar.StringMutationComparator import StringMutationComparator


class TestStringMutationComparator:

    @classmethod
    def setup_class(cls):
        cls.strict_comparator = StringMutationComparator(True)
        cls.lenient_comparator = StringMutationComparator(False)

    def test_compare_equals_mutations(self):
        assert self.strict_comparator.compare("41L", "41L") == 0
        assert self.strict_comparator.compare("Y41L", "41L") == 0

        assert self.lenient_comparator.compare("41L", "41L") == 0
        assert self.lenient_comparator.compare("Y41L", "41L") == 0
        assert self.lenient_comparator.compare("Y41LC", "41L") == 0
        assert self.lenient_comparator.compare("Y41L", "41LC") == 0
        assert self.lenient_comparator.compare("Y41LP", "41LC") == 0

    def test_compare_not_equals_mutations(self):
        assert self.strict_comparator.compare("41L", "41P") != 0
        assert self.strict_comparator.compare("41L", "41LP") != 0
        assert self.strict_comparator.compare("Y41L", "41LP") != 0
        assert self.strict_comparator.compare("Y41L", "Y52L") != 0

        assert self.lenient_comparator.compare("Y41L", "41P") != 0
        assert self.lenient_comparator.compare("Y41L", "Y52L") != 0
    
    def test_create_mutation(self):
        assert self.strict_comparator.create_mutation("41", ["L"]) == "41L"

    def test_invert_mutation(self):
        assert self.strict_comparator.invert_mutation("41L") == "41ACDEFGHIKMNPQRSTVWYZdi"

    def test_is_mutation_valid(self):
        assert self.strict_comparator.is_mutation_valid("41L") == True
        assert self.strict_comparator.is_mutation_valid("41X") == False
        assert self.strict_comparator.is_mutation_valid("X") == False

    def test_are_mutation_valid(self):
        assert self.strict_comparator.is_mutation_valid(["41L"]) == True
        assert self.strict_comparator.is_mutation_valid(["41X"]) == False
