# This file was generated by SableCC (http://www.sablecc.org/).

from types import StringType

from Asi.grammar.node import *
from Asi.grammar.utils import PushbackReader, StringBuffer

class LexerException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
        
# lexer states
STATE_INITIAL = 0

accept_tokens = [None] * 20
        
accept_tokens[0] = lambda line, pos: TMin(line, pos)
accept_tokens[1] = lambda line, pos: TAnd(line, pos)
accept_tokens[2] = lambda line, pos: TOr(line, pos)
accept_tokens[3] = lambda line, pos: TNot(line, pos)
accept_tokens[4] = lambda line, pos: TExclude(line, pos)
accept_tokens[5] = lambda line, pos: TSelect(line, pos)
accept_tokens[6] = lambda line, pos: TFrom(line, pos)
accept_tokens[7] = lambda line, pos: TAtleast(line, pos)
accept_tokens[8] = lambda line, pos: TExactly(line, pos)
accept_tokens[9] = lambda line, pos: TNotmorethan(line, pos)
accept_tokens[10] = lambda line, pos: TScore(line, pos)
accept_tokens[11] = lambda line, pos: TMax(line, pos)
accept_tokens[12] = lambda line, pos: TLPar(line, pos)
accept_tokens[13] = lambda line, pos: TRPar(line, pos)
accept_tokens[14] = lambda line, pos: TMapper(line, pos)
accept_tokens[15] = lambda line, pos: TComma(line, pos)
accept_tokens[16] = lambda line, pos: TBlank(None, line, pos)
accept_tokens[17] = lambda line, pos: TInteger(None, line, pos)
accept_tokens[18] = lambda line, pos: TFloat(None, line, pos)
accept_tokens[19] = lambda line, pos: TAminoAcid(None, line, pos)


lexer_gotoTable = [
                    [
                      [
                        [9, 9, 1],
                        [10, 10, 2],
                        [13, 13, 3],
                        [32, 32, 4],
                        [40, 40, 5],
                        [41, 41, 6],
                        [44, 44, 7],
                        [45, 45, 8],
                        [48, 57, 9],
                        [61, 61, 10],
                        [65, 65, 11],
                        [67, 67, 12],
                        [68, 68, 13],
                        [69, 69, 14],
                        [70, 70, 15],
                        [71, 71, 16],
                        [72, 72, 17],
                        [73, 73, 18],
                        [75, 75, 19],
                        [76, 76, 20],
                        [77, 77, 21],
                        [78, 78, 22],
                        [79, 79, 23],
                        [80, 80, 24],
                        [81, 81, 25],
                        [82, 82, 26],
                        [83, 83, 27],
                        [84, 84, 28],
                        [86, 86, 29],
                        [87, 87, 30],
                        [89, 89, 31],
                        [90, 90, 32],
                        [100, 100, 33],
                        [105, 105, 34],
                      ],
                      [
                        [9, 32, -2],
                      ],
                      [
                        [9, 32, -2],
                      ],
                      [
                        [9, 32, -2],
                      ],
                      [
                        [9, 32, -2],
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                        [46, 46, 35],
                        [48, 57, 9],
                      ],
                      [
                        [62, 62, 36],
                      ],
                      [
                        [78, 78, 37],
                        [84, 84, 38],
                      ],
                      [
                      ],
                      [
                      ],
                      [
                        [88, 88, 39],
                      ],
                      [
                        [82, 82, 40],
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                        [65, 65, 41],
                      ],
                      [
                        [79, 79, 42],
                      ],
                      [
                        [82, 82, 43],
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                        [67, 67, 44],
                        [69, 69, 45],
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                        [48, 57, 46],
                      ],
                      [
                      ],
                      [
                        [68, 68, 47],
                      ],
                      [
                        [76, 76, 48],
                      ],
                      [
                        [65, 65, 49],
                        [67, 67, 50],
                      ],
                      [
                        [79, 79, 51],
                      ],
                      [
                        [88, 88, 52],
                      ],
                      [
                        [84, 84, 53],
                      ],
                      [
                      ],
                      [
                        [79, 79, 54],
                      ],
                      [
                        [76, 76, 55],
                      ],
                      [
                        [48, 57, 46],
                      ],
                      [
                      ],
                      [
                        [69, 69, 56],
                      ],
                      [
                        [67, 67, 57],
                      ],
                      [
                        [76, 76, 58],
                      ],
                      [
                        [77, 77, 59],
                      ],
                      [
                      ],
                      [
                        [77, 77, 60],
                      ],
                      [
                        [82, 82, 61],
                      ],
                      [
                        [69, 69, 62],
                      ],
                      [
                        [65, 65, 63],
                      ],
                      [
                        [84, 84, 64],
                      ],
                      [
                        [85, 85, 65],
                      ],
                      [
                      ],
                      [
                        [79, 79, 66],
                      ],
                      [
                        [69, 69, 67],
                      ],
                      [
                        [67, 67, 68],
                      ],
                      [
                        [83, 83, 69],
                      ],
                      [
                        [76, 76, 70],
                      ],
                      [
                        [68, 68, 71],
                      ],
                      [
                        [82, 82, 72],
                      ],
                      [
                      ],
                      [
                        [84, 84, 73],
                      ],
                      [
                        [84, 84, 74],
                      ],
                      [
                        [89, 89, 75],
                      ],
                      [
                        [69, 69, 76],
                      ],
                      [
                        [69, 69, 77],
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                      ],
                      [
                        [84, 84, 78],
                      ],
                      [
                        [72, 72, 79],
                      ],
                      [
                        [65, 65, 80],
                      ],
                      [
                        [78, 78, 81],
                      ],
                      [
                      ],
                    ],
                  ] 
                
accept_table = [
                 [
                   -1, 16, 16, 16, 16, 12, 13, 15, 0, 17, -1, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, -1, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, -1, 14, -1, -1, -1, -1, -1, -1, 2, -1, -1, 18, 1, -1, -1, -1, -1, 11, 3, -1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, 5, 7, 8, 4, -1, -1, -1, -1, 9, 
                 ],
               ]
             
class Lexer(object):
    def __init__(self, source):
        if isinstance(source, StringType):
            self.reader = PushbackReader(file(source, "r"))
        else:
            self.reader = PushbackReader(source)

        self.token = None
        self.state = STATE_INITIAL
        self.line = 0
        self.pos = 0
        self.cr = False
        self.eof = False
        self.text = StringBuffer()

    def filter(self):
        pass

    def peek(self):
        while(self.token == None):
            self.token = self.getToken()
            self.filter()
        return self.token

    def next(self):
        while (self.token == None):
            self.token = self.getToken()
            self.filter()

        result = self.token
        self.token = None
        return result

    def getToken(self):
        dfa_state = 0

        start_pos = self.pos
        start_line = self.line

        accept_state = -1
        accept_token = -1
        accept_length = -1
        accept_pos = -1
        accept_line = -1
        gotoTable = lexer_gotoTable[self.state]
        accept = accept_table[self.state]
        text = self.text
        text.clear()

        while 1:
            c = self.getChar()

            if(c != -1):
                if (c == 10):
                    if(self.cr):
                        self.cr = False
                    else:
                        self.line = self.line + 1
                        self.pos = 0
                elif (c == 13):
                    self.line = self.line + 1
                    self.pos = 0
                    self.cr = True
                else:
                    self.pos = self.pos + 1
                    self.cr = False

                text.append(chr(c))
                
                while 1:
                    if (dfa_state < -1):
                        oldState = (-2 -dfa_state)
                    else:
                        oldState = dfa_state

                    dfa_state = -1

                    tmp1 =  gotoTable[oldState]
                    low = 0
                    high = len(tmp1) - 1

                    while (low <= high):
                        middle = (low + high) / 2
                        tmp2 = tmp1[middle]

                        if(c < tmp2[0]):
                            high = middle - 1
                        elif (c > tmp2[1]):
                            low = middle + 1
                        else:
                            dfa_state = tmp2[2]
                            break
                    if (dfa_state >= -1):
                    	break
            else:
                dfa_state = -1

            if (dfa_state >= 0):
                if (accept[dfa_state] != -1):
                    accept_state = dfa_state
                    accept_token = accept[dfa_state]
                    accept_length = len(text)
                    accept_pos = self.pos
                    accept_line = self.line
            else:
                if (accept_state != -1):
                    if (accept_token >= 0 and accept_token <= 19):
                    	token = accept_tokens[accept_token](start_line + 1, start_pos + 1)
                    	if token.getText() == None:
                    	    token.setText(self.getText(accept_length))
                    	
                        self.pushBack(accept_length)
                        self.pos = accept_pos
                        self.line = accept_line
                      
                        return token
                else:
                    if (len(text) > 0):
                        raise LexerException("[" + str(start_line + 1) + "," + str(start_pos + 1) + "]" +" Unknown token: " + str(text))
                    else:
                        return EOF(start_line + 1, start_pos + 1)

    def getChar(self):
        if (self.eof):
            return -1
        c = self.reader.read()
        
        if (c == ""):
            result = -1
        else:
            result = ord(c)

        if(result == -1):
            self.eof = True

        return result

    def pushBack(self, acceptLength):
        text = self.text
        length = len(text)
        for i in range(length - 1, acceptLength - 1, -1):
            self.eof = False
            self.reader.unread(text.charAt(i))

    def unread(self, token):
        text = token.getText()
        length = len(text)

        for i in range(length-1, -1, -1):
            self.eof = False
            self.reader.unread(text[i])

        self.pos = token.getPos() - 1
        self.line = token.getLine() - 1

    def getText(self, acceptLength):
        sb = StringBuffer()
        text = self.text
        for i in range(acceptLength):
            sb.append(text.charAt(i))

        return str(sb)