# This file was generated by SableCC (http://www.sablecc.org/).

import sys
from Asi.grammar.analysis import ReversedDepthFirstAdapter
from Asi.grammar.lexer import Lexer
from Asi.grammar.parser import Parser
from Asi.grammar.utils import Stack

class TreePrinter(ReversedDepthFirstAdapter):
    def __init__(self):
        self.indent = str() 
        self.output = str()
        self.indentchar = Stack()
        self.last = False

    def out_start(self, node):
        print("\n" + self.output[3:] + "\n")

    def default_in(self, node):
        if (self.last):
            self.indentchar.push('`')
        else:
            self.indentchar.push('|')

        self.indent = self.indent + "   "
        self.last = True

    def default_out(self, node):
        self.indent = self.indent[0 : len(self.indent) - 3]
        self.indent = self.indent[0 : len(self.indent) - 1] + self.indentchar.peek()
        self.indentchar.pop()
        self.output = self.indent + "- " + node.__class__.__name__ + "\n" + self.output
        self.indent = self.indent[0 : len(self.indent) - 1] + "|"

    def default_case(self, node):
        if (self.last):
            self.indent = self.indent[0 : len(self.indent) - 1] + "`"

        self.output = self.indent + "- " + node.get_text() + "\n" + self.output
 
        self.indent = self.indent[0 : len(self.indent) - 1] + "|"

        self.last = False

    def case_eof(self, node):
        self.last = False

def main():
    if len(sys.argv) < 2:
        print("usage:")
        print("    python test_parser.py <filename>")
    else:
        f = open(sys.argv[1], "r")
        _lexer = Lexer(f)
        _parser = Parser(_lexer)
        start = _parser.parse()

        printer = TreePrinter()
        start.apply(printer)
        f.close() # close the stream

if __name__ == '__main__':
    main()         
