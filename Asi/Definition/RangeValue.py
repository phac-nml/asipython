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


class RangeValue:

    def __init__(self, min_score, max_score, level):
        """Requires float min, float max, LevelDefinition level"""
        self.min = min_score
        self.max = max_score
        self.level = level

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_level(self):
        return self.level

    def within_range(self, score):
        """Requires float score"""
        return score >= self.min and score <= self.max

    def __str__(self):
        return "%f to %f => %i" % (self.min, self.max, self.level.get_order())

    def is_overlapping(self, other):
        """Requires RangeValue other"""
        try:
            return (self.min <= other.min and other.min <= self.max) \
                   or (other.min <= self.min and self.min <= self.max)
        except AttributeError:
            raise
