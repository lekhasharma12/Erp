# Generated from ERPL.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("N\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\6\n@\n\n\r\n\16\nA\3")
        buf.write("\13\3\13\3\f\5\fG\n\f\3\f\3\f\6\fK\n\f\r\f\16\fL\2\2\r")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3")
        buf.write("\2\4\5\2C\\aac|\4\2\13\13\"\"\2Q\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\37\3\2\2\2\t$\3\2")
        buf.write("\2\2\13(\3\2\2\2\r\60\3\2\2\2\17\65\3\2\2\2\21:\3\2\2")
        buf.write("\2\23?\3\2\2\2\25C\3\2\2\2\27J\3\2\2\2\31\32\7<\2\2\32")
        buf.write("\4\3\2\2\2\33\34\7f\2\2\34\35\7g\2\2\35\36\7h\2\2\36\6")
        buf.write("\3\2\2\2\37 \7g\2\2 !\7z\2\2!\"\7k\2\2\"#\7v\2\2#\b\3")
        buf.write("\2\2\2$%\7c\2\2%&\7f\2\2&\'\7f\2\2\'\n\3\2\2\2()\7r\2")
        buf.write("\2)*\7t\2\2*+\7q\2\2+,\7e\2\2,-\7g\2\2-.\7u\2\2./\7u\2")
        buf.write("\2/\f\3\2\2\2\60\61\7t\2\2\61\62\7q\2\2\62\63\7n\2\2\63")
        buf.write("\64\7g\2\2\64\16\3\2\2\2\65\66\7v\2\2\66\67\7c\2\2\67")
        buf.write("8\7u\2\289\7m\2\29\20\3\2\2\2:;\7g\2\2;<\7p\2\2<=\7f\2")
        buf.write("\2=\22\3\2\2\2>@\t\2\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2")
        buf.write("AB\3\2\2\2B\24\3\2\2\2CD\t\3\2\2D\26\3\2\2\2EG\7\17\2")
        buf.write("\2FE\3\2\2\2FG\3\2\2\2GH\3\2\2\2HK\7\f\2\2IK\7\17\2\2")
        buf.write("JF\3\2\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\30")
        buf.write("\3\2\2\2\7\2AFJL\2")
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
    END = 8
    ID = 9
    WS = 10
    NEWLINE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'def'", "'exit'", "'add'", "'process'", "'role'", "'task'", 
            "'end'" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "EXIT", "ADD", "PROCESS", "ROLE", "TASK", "END", "ID", 
            "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "DEF", "EXIT", "ADD", "PROCESS", "ROLE", "TASK", 
                  "END", "ID", "WS", "NEWLINE" ]

    grammarFileName = "ERPL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


