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


class LevelAction:
    """LevelAction"""

    def __init__(self, level):
        """Requires a LevelDefinition object"""
        self.level = level

    def get_level(self):
        """Returns: LevelDefinition level"""
        return self.level

    def evaluate(self, result):
        """Requires a bool argument result"""
        if not isinstance(result, bool):
            raise ValueError("evaluate(self, result) in LevelAction requires bool argument")
        return self.level if result else None

    # pylint: disable=no-self-use
    def supports(self, result_type):
        """Returns bool indicating if result_type matches the argument type evalute requires"""
        return isinstance(result_type, bool)
