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


class CommentDefinition(object):
    FORMAT = "'{'id: %s, text: %s, sort: %d'}'"

    def __init__(self, identifier, text, sort=None):
        self.id = identifier
        self.text = text
        self.sort = sort

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text

    def get_scort(self):
        return self.sort

    def get_resistance(self):
        return self.text

    def __str__(self):
        return self.FORMAT % (self.id, self.text, self.sort)