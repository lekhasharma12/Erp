# Generated from ERPL.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("D\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\3\6\3\22\n\3\r\3\16\3\23\3\3\3\3\3\4\6\4\31\n\4")
        buf.write("\r\4\16\4\32\3\4\6\4\36\n\4\r\4\16\4\37\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\6\6\60\n\6")
        buf.write("\r\6\16\6\61\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\t")
        buf.write("\n\2A\2\16\3\2\2\2\4\21\3\2\2\2\6\30\3\2\2\2\b!\3\2\2")
        buf.write("\2\n(\3\2\2\2\f8\3\2\2\2\16\17\5\4\3\2\17\3\3\2\2\2\20")
        buf.write("\22\5\6\4\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2")
        buf.write("\23\24\3\2\2\2\24\25\3\2\2\2\25\26\7\5\2\2\26\5\3\2\2")
        buf.write("\2\27\31\5\b\5\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2")
        buf.write("\2\2\32\33\3\2\2\2\33\35\3\2\2\2\34\36\5\n\6\2\35\34\3")
        buf.write("\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \7\3\2")
        buf.write("\2\2!\"\7\4\2\2\"#\7\r\2\2#$\7\b\2\2$%\7\r\2\2%&\7\f\2")
        buf.write("\2&\'\7\16\2\2\'\t\3\2\2\2()\7\4\2\2)*\7\r\2\2*+\7\7\2")
        buf.write("\2+,\7\r\2\2,-\7\f\2\2-/\7\16\2\2.\60\5\f\7\2/.\3\2\2")
        buf.write("\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2")
        buf.write("\2\63\64\7\13\2\2\64\65\7\r\2\2\65\66\7\7\2\2\66\67\7")
        buf.write("\16\2\2\67\13\3\2\2\289\7\6\2\29:\7\r\2\2:;\t\2\2\2;<")
        buf.write("\7\r\2\2<=\7\f\2\2=>\7\r\2\2>?\7\3\2\2?@\7\r\2\2@A\7\f")
        buf.write("\2\2AB\7\16\2\2B\r\3\2\2\2\6\23\32\37\61")
        return buf.getvalue()


class ERPLParser ( Parser ):

    grammarFileName = "ERPL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'def'", "'exit'", "'add'", "'process'", 
                     "'role'", "'task'", "'start_task'", "'end'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "DEF", "EXIT", "ADD", "PROCESS", 
                      "ROLE", "TASK", "STARTTASK", "END", "ID", "WS", "NEWLINE" ]

    RULE_s = 0
    RULE_q = 1
    RULE_a = 2
    RULE_r = 3
    RULE_p = 4
    RULE_t = 5

    ruleNames =  [ "s", "q", "a", "r", "p", "t" ]

    EOF = Token.EOF
    T__0=1
    DEF=2
    EXIT=3
    ADD=4
    PROCESS=5
    ROLE=6
    TASK=7
    STARTTASK=8
    END=9
    ID=10
    WS=11
    NEWLINE=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def q(self):
            return self.getTypedRuleContext(ERPLParser.QContext,0)


        def getRuleIndex(self):
            return ERPLParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = ERPLParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.q()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXIT(self):
            return self.getToken(ERPLParser.EXIT, 0)

        def a(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ERPLParser.AContext)
            else:
                return self.getTypedRuleContext(ERPLParser.AContext,i)


        def getRuleIndex(self):
            return ERPLParser.RULE_q

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQ" ):
                listener.enterQ(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQ" ):
                listener.exitQ(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQ" ):
                return visitor.visitQ(self)
            else:
                return visitor.visitChildren(self)




    def q(self):

        localctx = ERPLParser.QContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_q)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.a()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ERPLParser.DEF):
                    break

            self.state = 19
            self.match(ERPLParser.EXIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ERPLParser.RContext)
            else:
                return self.getTypedRuleContext(ERPLParser.RContext,i)


        def p(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ERPLParser.PContext)
            else:
                return self.getTypedRuleContext(ERPLParser.PContext,i)


        def getRuleIndex(self):
            return ERPLParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA" ):
                return visitor.visitA(self)
            else:
                return visitor.visitChildren(self)




    def a(self):

        localctx = ERPLParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_a)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 21
                    self.r()

                else:
                    raise NoViableAltException(self)
                self.state = 24 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 27 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 26
                    self.p()

                else:
                    raise NoViableAltException(self)
                self.state = 29 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(ERPLParser.DEF, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ERPLParser.WS)
            else:
                return self.getToken(ERPLParser.WS, i)

        def ROLE(self):
            return self.getToken(ERPLParser.ROLE, 0)

        def ID(self):
            return self.getToken(ERPLParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(ERPLParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ERPLParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR" ):
                return visitor.visitR(self)
            else:
                return visitor.visitChildren(self)




    def r(self):

        localctx = ERPLParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ERPLParser.DEF)
            self.state = 32
            self.match(ERPLParser.WS)
            self.state = 33
            self.match(ERPLParser.ROLE)
            self.state = 34
            self.match(ERPLParser.WS)
            self.state = 35
            self.match(ERPLParser.ID)
            self.state = 36
            self.match(ERPLParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(ERPLParser.DEF, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ERPLParser.WS)
            else:
                return self.getToken(ERPLParser.WS, i)

        def PROCESS(self, i:int=None):
            if i is None:
                return self.getTokens(ERPLParser.PROCESS)
            else:
                return self.getToken(ERPLParser.PROCESS, i)

        def ID(self):
            return self.getToken(ERPLParser.ID, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ERPLParser.NEWLINE)
            else:
                return self.getToken(ERPLParser.NEWLINE, i)

        def END(self):
            return self.getToken(ERPLParser.END, 0)

        def t(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ERPLParser.TContext)
            else:
                return self.getTypedRuleContext(ERPLParser.TContext,i)


        def getRuleIndex(self):
            return ERPLParser.RULE_p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP" ):
                listener.enterP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP" ):
                listener.exitP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP" ):
                return visitor.visitP(self)
            else:
                return visitor.visitChildren(self)




    def p(self):

        localctx = ERPLParser.PContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ERPLParser.DEF)
            self.state = 39
            self.match(ERPLParser.WS)
            self.state = 40
            self.match(ERPLParser.PROCESS)
            self.state = 41
            self.match(ERPLParser.WS)
            self.state = 42
            self.match(ERPLParser.ID)
            self.state = 43
            self.match(ERPLParser.NEWLINE)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.t()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ERPLParser.ADD):
                    break

            self.state = 49
            self.match(ERPLParser.END)
            self.state = 50
            self.match(ERPLParser.WS)
            self.state = 51
            self.match(ERPLParser.PROCESS)
            self.state = 52
            self.match(ERPLParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ERPLParser.ADD, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ERPLParser.WS)
            else:
                return self.getToken(ERPLParser.WS, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ERPLParser.ID)
            else:
                return self.getToken(ERPLParser.ID, i)

        def NEWLINE(self):
            return self.getToken(ERPLParser.NEWLINE, 0)

        def STARTTASK(self):
            return self.getToken(ERPLParser.STARTTASK, 0)

        def TASK(self):
            return self.getToken(ERPLParser.TASK, 0)

        def getRuleIndex(self):
            return ERPLParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = ERPLParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_t)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ERPLParser.ADD)
            self.state = 55
            self.match(ERPLParser.WS)
            self.state = 56
            _la = self._input.LA(1)
            if not(_la==ERPLParser.TASK or _la==ERPLParser.STARTTASK):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 57
            self.match(ERPLParser.WS)
            self.state = 58
            self.match(ERPLParser.ID)
            self.state = 59
            self.match(ERPLParser.WS)
            self.state = 60
            self.match(ERPLParser.T__0)
            self.state = 61
            self.match(ERPLParser.WS)
            self.state = 62
            self.match(ERPLParser.ID)
            self.state = 63
            self.match(ERPLParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





