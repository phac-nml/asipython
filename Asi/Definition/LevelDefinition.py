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


class LevelDefinition:
    """LevelDefinition"""

    FORMAT = "LevelDefinition{order: %i, text: %s, sir: %s}"

    def __init__(self, order, text, sir):
        """Params: int order, str text, str sir"""
        self.order = order
        self.text = text
        self.sir = sir

    def get_order(self):
        """Returns: int order"""
        return self.order

    def get_text(self):
        """Returns: str text"""
        return self.text

    def get_sir(self):
        """Returns: str sir"""
        return self.sir

    def get_resistance(self):
        """Returns: str text"""
        return self.text

    def __str__(self):
        return self.FORMAT % (self.order, self.text, self.sir)

    def __repr__(self):
        return self.FORMAT % (self.order, self.text, self.sir)
