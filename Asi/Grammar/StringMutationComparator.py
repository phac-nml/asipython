
import re


class StringMutationComparator:
    AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWYZdi"
    MUTATION_PATTERN = re.compile("^(?:[A-Z]?)(\\d+)([%s]+)$" % AMINO_ACIDS)
    CODON_GROUP = 1
    AMINO_ACIDS_GROUP = 2

    def __init__(self, strict_comparison):
        self.strict_comparison = strict_comparison

    def compare(self, object1, object2):
        result1 = self.MUTATION_PATTERN.match(str(object1))
        result2 = self.MUTATION_PATTERN.match(str(object2))

        if result1 is None or result2 is None:
            raise RuntimeError("Invalid String formatted mutations: %s, %s" % (object1, object2))

        codon1 = int(result1.group(self.CODON_GROUP))
        codon2 = int(result2.group(self.CODON_GROUP))

        if codon1 != codon2:
            return 1

        aa_list1 = list(result1.group(self.AMINO_ACIDS_GROUP))
        aa_list2 = list(result2.group(self.AMINO_ACIDS_GROUP))

        intersection = [x for x in aa_list1 if x in aa_list2]
        if self.strict_comparison:
            min_size = len(aa_list2) if len(aa_list1) <= len(aa_list2) else len(aa_list1)
            if len(intersection) >= min_size:
                return 0
        else:
            if intersection:
                return 0

        return 1

    def create_mutation(self, codon_number, amino_acid_list):
        return ""

    def invert_mutation(self, mutation):
        return ""

    def is_mutation_valid(self, mutation):
        return ""

    def are_mutations_valid(self, mutation_list):
        return False
