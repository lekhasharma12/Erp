# Generated from ERPL.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ERPLParser import ERPLParser
else:
    from ERPLParser import ERPLParser

# This class defines a complete generic visitor for a parse tree produced by ERPLParser.

class ERPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ERPLParser#s.
    def visitS(self, ctx:ERPLParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERPLParser#q.
    def visitQ(self, ctx:ERPLParser.QContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERPLParser#a.
    def visitA(self, ctx:ERPLParser.AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERPLParser#r.
    def visitR(self, ctx:ERPLParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERPLParser#p.
    def visitP(self, ctx:ERPLParser.PContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERPLParser#t.
    def visitT(self, ctx:ERPLParser.TContext):
        return self.visitChildren(ctx)



del ERPLParser