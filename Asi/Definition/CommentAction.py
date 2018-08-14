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

from Asi.AsiEvaluationException import AsiEvaluationException


class CommentAction(object):

    def __init__(self, comment):
        """Requires a CommentDefinition object"""
        self.comment = comment

    def get_comment(self):
        return self.comment

    def evaluate(result):
        """Requires a boolean argument result"""
        return self.comment if result else None

    def supports(resultType):
        return resultType.equals(bool)
