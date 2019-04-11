from ERPLListener import ERPLListener as EL
from ERPLParser import ERPLParser

class ERPLCustomListener(EL) :
    idP = []
    idR = []
    idT = {}
    def enterS(self, ctx:ERPLParser.SContext):
        pass

    # Exit a parse tree produced by ERPLParser#s.
    def exitS(self, ctx:ERPLParser.SContext):
        pass


    # Enter a parse tree produced by ERPLParser#q.
    def enterQ(self, ctx:ERPLParser.QContext):
        pass

    # Exit a parse tree produced by ERPLParser#q.
    def exitQ(self, ctx:ERPLParser.QContext):
        print(ctx.getText())
        print(self.idR)
        print(self.idP)
        print(self.idT)


    # Enter a parse tree produced by ERPLParser#a.
    def enterA(self, ctx:ERPLParser.AContext):
        pass

    # Exit a parse tree produced by ERPLParser#a.
    def exitA(self, ctx:ERPLParser.AContext):
        pass


    # Enter a parse tree produced by ERPLParser#r.
    def enterR(self, ctx:ERPLParser.RContext):
        pass

    # Exit a parse tree produced by ERPLParser#r.
    def exitR(self, ctx:ERPLParser.RContext):
        self.idR.append(ctx.ID().getText())


    # Enter a parse tree produced by ERPLParser#p.
    def enterP(self, ctx:ERPLParser.PContext):
        pass

    # Exit a parse tree produced by ERPLParser#p.
    def exitP(self, ctx:ERPLParser.PContext):
        self.idP.append(ctx.ID().getText())


    # Enter a parse tree produced by ERPLParser#t.
    def enterT(self, ctx:ERPLParser.TContext):
        pass

    # Exit a parse tree produced by ERPLParser#t.
    def exitT(self, ctx:ERPLParser.TContext):
        a = list(ctx.ID())
        if a[1].getText() in self.idR:
            self.idT[a[0].getText()] = a[1].getText()
        else:
            print('Error! Role not found - ' + a[1].getText())