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
# This file was generated by SableCC (http://www.sablecc.org/).
# pylint: disable=missing-docstring


def caller(num=1):
    import inspect
    return inspect.getouterframes(inspect.currentframe())[num][3]


# pylint: disable=unused-argument
def abstract(*args):
    raise NotImplementedError(caller() + ' must be implemented in subclass')


class Stack(list):
    def push(self, value):
        self.append(value)

    def peek(self):
        return self[len(self)-1]

    def empty(self):
        return len(self) == 0


class PushbackReader(object):
    def __init__(self, reader):
        self.__reader = reader
        self.__stack = Stack()

    def peek(self):
        if self.__stack:
            result = self.__stack.peek()
        else:
            result = self.__reader.read(1)
            self.__reader.seek(-1, 1)  # go back to the previous position
        return result

    def read(self):
        if self.__stack:
            return self.__stack.pop()
        return self.__reader.read(1)

    def unread(self, char):
        self.__stack.append(char)


class StringBuffer(object):
    def __init__(self, obj=None):
        self.buffer = []
        if obj is not None:
            if isinstance(obj, bytes):
                self.buffer.extend(list(obj))
            else:
                self.buffer.extend(list(str(obj)))

    def append(self, obj):
        if isinstance(obj, bytes):
            self.buffer.extend(list(obj))
        else:
            self.buffer.extend(list(str(obj)))

    def char_at(self, index):
        return self.buffer[index]

    def __len__(self):
        return len(self.buffer)

    def __eq__(self, other):
        if type(self) is not type(other):
            return False

        return self.buffer == other.buffer

    def __ne__(self, other):
        if type(self) is not type(other):
            return True

        return self.buffer != other.buffer

    def clear(self):
        del self.buffer[0:len(self.buffer)]

    def __str__(self):
        return "".join(self.buffer)

    def __repr__(self):
        return "'" + self.__str__() + "'"

    def substring(self, start, finish):
        return ''.join(self.buffer[start:finish])

    def __getitem__(self, index):
        return self.buffer[index]

    def __setitem__(self, index, char):
        if not isinstance(char, bytes):
            raise RuntimeError("Only single characters can be assigned")
        if not len(char) == 1:
            raise RuntimeError("Only single characters can be assigned")
        self.buffer[index] = char

    def __iter__(self):
        return iter(self.buffer)

    def __getslice__(self, start, finish):
        return self.substring(start, finish)

    def reverse(self):
        self.buffer.reverse()

    def __contains__(self, char):
        if not isinstance(char, bytes):
            raise RuntimeError("Only single characters can be assigned")
        if not len(char) == 1:
            raise RuntimeError("Only single characters can be assigned")
        return self.buffer.__contains__(char)

    def contains(self, char):
        self.__contains__(char)
