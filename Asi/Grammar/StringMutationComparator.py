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
import re


class StringMutationComparator:
    """Compares two mutation strings"""
    AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWYZdi"
    AMINO_ACIDS_LIST = list(AMINO_ACIDS)
    MUTATION_PATTERN = re.compile("^(?:[A-Z]?)(\\d+)([%s]+)$" % AMINO_ACIDS)
    CODON_GROUP = 1
    AMINO_ACIDS_GROUP = 2

    def __init__(self, strict_comparison):
        self.strict_comparison = strict_comparison

    def compare(self, mutation1, mutation2):
        """Compares two mutations, and returns 1 for a match and 0 for a mismatch.
        If self.strict_comparison equals TRUE, then mutations must be identical.
        If self.strict_comparison equals FALSE, then mutation2 must contain a subset of mutation1.

        Parameters
        ----------
        mutation1 : mutation from rule
        mutation2 : mutation to query

        Returns:
            int: 1 for match, 0 for mismatch.
        """
        result1 = self.MUTATION_PATTERN.match(str(mutation1))
        result2 = self.MUTATION_PATTERN.match(str(mutation2))

        if result1 is None or result2 is None:
            raise RuntimeError("Invalid String formatted mutations: %s, %s"
                               % (mutation1, mutation2))

        codon1 = int(result1.group(self.CODON_GROUP))
        codon2 = int(result2.group(self.CODON_GROUP))

        if codon1 != codon2:
            return 0

        aa_list1 = list(result1.group(self.AMINO_ACIDS_GROUP))
        aa_list2 = list(result2.group(self.AMINO_ACIDS_GROUP))

        intersection = [x for x in aa_list1 if x in aa_list2]
        if self.strict_comparison:
            min_size = len(aa_list2) if len(aa_list1) <= len(aa_list2) else len(aa_list1)
            if len(intersection) >= min_size:
                return 1
        else:
            if intersection:
                return 1

        return 0

    def create_mutation(self, codon_number, amino_acid_list):
        """Return the String representation of this codon, amino_acid_list pair."""
        mutation = str(codon_number).strip()
        for amino_acid in amino_acid_list:
            mutation += str(amino_acid).strip()

        if not self.MUTATION_PATTERN.match(mutation):
            raise ValueError("Invalid create_mutation parameters: %s, %s"
                             % (codon_number, amino_acid_list))

        return mutation

    def invert_mutation(self, mutation):
        """Return this String mutation with its amino acid list inverted"""
        matches = self.MUTATION_PATTERN.match(mutation)
        if not matches:
            raise ValueError("Invalid invert_mutation parameter: %s" % mutation)

        found_acids = list(matches.group(self.AMINO_ACIDS_GROUP))
        not_found_acids = [x for x in self.AMINO_ACIDS_LIST if x not in found_acids]

        return self.create_mutation(matches.group(self.CODON_GROUP), not_found_acids)

    def is_mutation_valid(self, mutation):
        """Given a mutation, Return true if it is valid"""
        return self.MUTATION_PATTERN.match(str(mutation)) is not None

    def are_mutations_valid(self, mutation_list):
        """Given a list of mutations, Return true if all are valid"""
        for mutation in mutation_list:
            if self.MUTATION_PATTERN.match(str(mutation)) is None:
                return False
        return True
