# Generated from ERPL.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\6\3\24\n\3\r\3\16\3\25\3\3\3\3\3\4\6")
        buf.write("\4\33\n\4\r\4\16\4\34\3\4\6\4 \n\4\r\4\16\4!\3\4\6\4%")
        buf.write("\n\4\r\4\16\4&\5\4)\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\6\69\n\6\r\6\16\6:\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16")
        buf.write("\2\3\3\2\t\n\2R\2\20\3\2\2\2\4\23\3\2\2\2\6(\3\2\2\2\b")
        buf.write("*\3\2\2\2\n\61\3\2\2\2\fA\3\2\2\2\16L\3\2\2\2\20\21\5")
        buf.write("\4\3\2\21\3\3\2\2\2\22\24\5\6\4\2\23\22\3\2\2\2\24\25")
        buf.write("\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\27\3\2\2\2\27")
        buf.write("\30\7\5\2\2\30\5\3\2\2\2\31\33\5\b\5\2\32\31\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\37\3\2\2\2")
        buf.write("\36 \5\n\6\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3")
        buf.write("\2\2\2\")\3\2\2\2#%\5\16\b\2$#\3\2\2\2%&\3\2\2\2&$\3\2")
        buf.write("\2\2&\'\3\2\2\2\')\3\2\2\2(\32\3\2\2\2($\3\2\2\2)\7\3")
        buf.write("\2\2\2*+\7\4\2\2+,\7\16\2\2,-\7\b\2\2-.\7\16\2\2./\7\r")
        buf.write("\2\2/\60\7\17\2\2\60\t\3\2\2\2\61\62\7\4\2\2\62\63\7\16")
        buf.write("\2\2\63\64\7\7\2\2\64\65\7\16\2\2\65\66\7\r\2\2\668\7")
        buf.write("\17\2\2\679\5\f\7\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;")
        buf.write("\3\2\2\2;<\3\2\2\2<=\7\13\2\2=>\7\16\2\2>?\7\7\2\2?@\7")
        buf.write("\17\2\2@\13\3\2\2\2AB\7\6\2\2BC\7\16\2\2CD\t\2\2\2DE\7")
        buf.write("\16\2\2EF\7\r\2\2FG\7\16\2\2GH\7\3\2\2HI\7\16\2\2IJ\7")
        buf.write("\r\2\2JK\7\17\2\2K\r\3\2\2\2LM\7\f\2\2MN\7\16\2\2NO\7")
        buf.write("\t\2\2OP\7\16\2\2PQ\7\r\2\2QR\7\17\2\2R\17\3\2\2\2\b\25")
        buf.write("\34!&(:")
        return buf.getvalue()


class ERPLParser ( Parser ):

    grammarFileName = "ERPL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'def'", "'exit'", "'add'", "'process'", 
                     "'role'", "'task'", "'start task'", "'end'", "'run'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "DEF", "EXIT", "ADD", "PROCESS", 
                      "ROLE", "TASK", "STARTTASK", "END", "RUN", "ID", "WS", 
                      "NEWLINE" ]

    RULE_s = 0
    RULE_q = 1
    RULE_a = 2
    RULE_r = 3
    RULE_p = 4
    RULE_t = 5
    RULE_i = 6

    ruleNames =  [ "s", "q", "a", "r", "p", "t", "i" ]

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
    RUN=10
    ID=11
    WS=12
    NEWLINE=13

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
            self.state = 14
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
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.a()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ERPLParser.DEF or _la==ERPLParser.RUN):
                    break

            self.state = 21
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


        def i(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ERPLParser.IContext)
            else:
                return self.getTypedRuleContext(ERPLParser.IContext,i)


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
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ERPLParser.DEF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 23
                        self.r()

                    else:
                        raise NoViableAltException(self)
                    self.state = 26 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 29 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 28
                        self.p()

                    else:
                        raise NoViableAltException(self)
                    self.state = 31 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [ERPLParser.RUN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 33
                        self.i()

                    else:
                        raise NoViableAltException(self)
                    self.state = 36 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 40
            self.match(ERPLParser.DEF)
            self.state = 41
            self.match(ERPLParser.WS)
            self.state = 42
            self.match(ERPLParser.ROLE)
            self.state = 43
            self.match(ERPLParser.WS)
            self.state = 44
            self.match(ERPLParser.ID)
            self.state = 45
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
            self.state = 47
            self.match(ERPLParser.DEF)
            self.state = 48
            self.match(ERPLParser.WS)
            self.state = 49
            self.match(ERPLParser.PROCESS)
            self.state = 50
            self.match(ERPLParser.WS)
            self.state = 51
            self.match(ERPLParser.ID)
            self.state = 52
            self.match(ERPLParser.NEWLINE)
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.t()
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ERPLParser.ADD):
                    break

            self.state = 58
            self.match(ERPLParser.END)
            self.state = 59
            self.match(ERPLParser.WS)
            self.state = 60
            self.match(ERPLParser.PROCESS)
            self.state = 61
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
            self.state = 63
            self.match(ERPLParser.ADD)
            self.state = 64
            self.match(ERPLParser.WS)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==ERPLParser.TASK or _la==ERPLParser.STARTTASK):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 66
            self.match(ERPLParser.WS)
            self.state = 67
            self.match(ERPLParser.ID)
            self.state = 68
            self.match(ERPLParser.WS)
            self.state = 69
            self.match(ERPLParser.T__0)
            self.state = 70
            self.match(ERPLParser.WS)
            self.state = 71
            self.match(ERPLParser.ID)
            self.state = 72
            self.match(ERPLParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RUN(self):
            return self.getToken(ERPLParser.RUN, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ERPLParser.WS)
            else:
                return self.getToken(ERPLParser.WS, i)

        def TASK(self):
            return self.getToken(ERPLParser.TASK, 0)

        def ID(self):
            return self.getToken(ERPLParser.ID, 0)

        def NEWLINE(self):
            return self.getToken(ERPLParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ERPLParser.RULE_i

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterI" ):
                listener.enterI(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitI" ):
                listener.exitI(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitI" ):
                return visitor.visitI(self)
            else:
                return visitor.visitChildren(self)




    def i(self):

        localctx = ERPLParser.IContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_i)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ERPLParser.RUN)
            self.state = 75
            self.match(ERPLParser.WS)
            self.state = 76
            self.match(ERPLParser.TASK)
            self.state = 77
            self.match(ERPLParser.WS)
            self.state = 78
            self.match(ERPLParser.ID)
            self.state = 79
            self.match(ERPLParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





