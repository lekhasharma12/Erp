# Generated from ERPL.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("[\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\6\13M\n\13\r\13\16\13")
        buf.write("N\3\f\3\f\3\r\5\rT\n\r\3\r\3\r\6\rX\n\r\r\r\16\rY\2\2")
        buf.write("\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\3\2\4\5\2C\\aac|\4\2\13\13\"\"\2^\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2")
        buf.write("\2\7!\3\2\2\2\t&\3\2\2\2\13*\3\2\2\2\r\62\3\2\2\2\17\67")
        buf.write("\3\2\2\2\21<\3\2\2\2\23G\3\2\2\2\25L\3\2\2\2\27P\3\2\2")
        buf.write("\2\31W\3\2\2\2\33\34\7<\2\2\34\4\3\2\2\2\35\36\7f\2\2")
        buf.write("\36\37\7g\2\2\37 \7h\2\2 \6\3\2\2\2!\"\7g\2\2\"#\7z\2")
        buf.write("\2#$\7k\2\2$%\7v\2\2%\b\3\2\2\2&\'\7c\2\2\'(\7f\2\2()")
        buf.write("\7f\2\2)\n\3\2\2\2*+\7r\2\2+,\7t\2\2,-\7q\2\2-.\7e\2\2")
        buf.write("./\7g\2\2/\60\7u\2\2\60\61\7u\2\2\61\f\3\2\2\2\62\63\7")
        buf.write("t\2\2\63\64\7q\2\2\64\65\7n\2\2\65\66\7g\2\2\66\16\3\2")
        buf.write("\2\2\678\7v\2\289\7c\2\29:\7u\2\2:;\7m\2\2;\20\3\2\2\2")
        buf.write("<=\7u\2\2=>\7v\2\2>?\7c\2\2?@\7t\2\2@A\7v\2\2AB\7a\2\2")
        buf.write("BC\7v\2\2CD\7c\2\2DE\7u\2\2EF\7m\2\2F\22\3\2\2\2GH\7g")
        buf.write("\2\2HI\7p\2\2IJ\7f\2\2J\24\3\2\2\2KM\t\2\2\2LK\3\2\2\2")
        buf.write("MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\26\3\2\2\2PQ\t\3\2\2Q")
        buf.write("\30\3\2\2\2RT\7\17\2\2SR\3\2\2\2ST\3\2\2\2TU\3\2\2\2U")
        buf.write("X\7\f\2\2VX\7\17\2\2WS\3\2\2\2WV\3\2\2\2XY\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z\32\3\2\2\2\7\2NSWY\2")
        return buf.getvalue()


class ERPLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    DEF = 2
    EXIT = 3
    ADD = 4
    PROCESS = 5
    ROLE = 6
    TASK = 7
    STARTTASK = 8
    END = 9
    ID = 10
    WS = 11
    NEWLINE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'def'", "'exit'", "'add'", "'process'", "'role'", "'task'", 
            "'start_task'", "'end'" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "EXIT", "ADD", "PROCESS", "ROLE", "TASK", "STARTTASK", 
            "END", "ID", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "DEF", "EXIT", "ADD", "PROCESS", "ROLE", "TASK", 
                  "STARTTASK", "END", "ID", "WS", "NEWLINE" ]

    grammarFileName = "ERPL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


