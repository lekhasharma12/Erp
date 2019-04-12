# Generated from ERPL.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\6\fS\n\f\r\f\16\fT\3\r\3\r\3\16\5\16Z\n\16\3\16")
        buf.write("\3\16\6\16^\n\16\r\16\16\16_\2\2\17\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\4\5\2")
        buf.write("C\\aac|\4\2\13\13\"\"\2d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7")
        buf.write("#\3\2\2\2\t(\3\2\2\2\13,\3\2\2\2\r\64\3\2\2\2\179\3\2")
        buf.write("\2\2\21>\3\2\2\2\23I\3\2\2\2\25M\3\2\2\2\27R\3\2\2\2\31")
        buf.write("V\3\2\2\2\33]\3\2\2\2\35\36\7<\2\2\36\4\3\2\2\2\37 \7")
        buf.write("f\2\2 !\7g\2\2!\"\7h\2\2\"\6\3\2\2\2#$\7g\2\2$%\7z\2\2")
        buf.write("%&\7k\2\2&\'\7v\2\2\'\b\3\2\2\2()\7c\2\2)*\7f\2\2*+\7")
        buf.write("f\2\2+\n\3\2\2\2,-\7r\2\2-.\7t\2\2./\7q\2\2/\60\7e\2\2")
        buf.write("\60\61\7g\2\2\61\62\7u\2\2\62\63\7u\2\2\63\f\3\2\2\2\64")
        buf.write("\65\7t\2\2\65\66\7q\2\2\66\67\7n\2\2\678\7g\2\28\16\3")
        buf.write("\2\2\29:\7v\2\2:;\7c\2\2;<\7u\2\2<=\7m\2\2=\20\3\2\2\2")
        buf.write(">?\7u\2\2?@\7v\2\2@A\7c\2\2AB\7t\2\2BC\7v\2\2CD\7\"\2")
        buf.write("\2DE\7v\2\2EF\7c\2\2FG\7u\2\2GH\7m\2\2H\22\3\2\2\2IJ\7")
        buf.write("g\2\2JK\7p\2\2KL\7f\2\2L\24\3\2\2\2MN\7t\2\2NO\7w\2\2")
        buf.write("OP\7p\2\2P\26\3\2\2\2QS\t\2\2\2RQ\3\2\2\2ST\3\2\2\2TR")
        buf.write("\3\2\2\2TU\3\2\2\2U\30\3\2\2\2VW\t\3\2\2W\32\3\2\2\2X")
        buf.write("Z\7\17\2\2YX\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[^\7\f\2\2\\^")
        buf.write("\7\17\2\2]Y\3\2\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3")
        buf.write("\2\2\2`\34\3\2\2\2\7\2TY]_\2")
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
    RUN = 10
    ID = 11
    WS = 12
    NEWLINE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'def'", "'exit'", "'add'", "'process'", "'role'", "'task'", 
            "'start task'", "'end'", "'run'" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "EXIT", "ADD", "PROCESS", "ROLE", "TASK", "STARTTASK", 
            "END", "RUN", "ID", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "DEF", "EXIT", "ADD", "PROCESS", "ROLE", "TASK", 
                  "STARTTASK", "END", "RUN", "ID", "WS", "NEWLINE" ]

    grammarFileName = "ERPL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


