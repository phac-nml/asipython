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

from Asi.AsiParsingException import AsiParsingException
from Asi.AsiEvaluationException import AsiEvaluationException


class ScoreRangeAction:
    """ScoreRangeAction"""

    def __init__(self, range_values):
        """Requires a list of RangeValue objects"""
        self.check_for_overlapping_ranges(range_values)
        self.range_values = range_values

    # pylint: disable=no-self-use
    def check_for_overlapping_ranges(self, range_values):
        """Requires a list of RangeValue objects"""
        for range_value1 in range_values:
            for range_value2 in range_values:
                try:
                    if (range_value1 is not range_value2 and
                            range_value1.is_overlapping(range_value2)):
                        raise AsiParsingException("Score range values overlap: %s, %s" %
                                                  (str(range_value1),
                                                   str(range_value2)))
                except AttributeError as exc:
                    raise exc

    def evaluate(self, result):
        """Requires a float argument result"""
        if not isinstance(result, float):
            raise ValueError("evaluate(self, result) in ScoreRangeAction requires float argument")
        for range_value in self.range_values:
            try:
                if range_value.within_range(result):
                    return range_value.get_level()
            except AttributeError as exc:
                raise exc
        raise AsiEvaluationException("No score range has been defined for a score of: %s" % result)

    # pylint: disable=no-self-use
    def supports(self, result_type):
        """Returns bool indicating if result_type matches the argument type evalute requires"""
        return isinstance(result_type, float)
