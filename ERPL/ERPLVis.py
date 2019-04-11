from ERPLVisitor import ERPLVisitor as EV
from ERPLListener import ERPLListener as EL
from ERPLParser import ERPLParser
import sqlite3

class ERPLVis(EV, EL) :
    idP = []
    idR = []
    idT = {}
    dbname = ''


    def visitS(self, ctx:ERPLParser.SContext):
        return super().visitS(ctx)


    # Visit a parse tree produced by ERPLParser#q.
    def exitQ(self, ctx:ERPLParser.QContext):
        print(ctx.getText())
        print(self.idR)
        print(self.idP)
        print(self.idT)
        return super().exitQ(ctx)


    # Visit a parse tree produced by ERPLParser#a.
    def visitA(self, ctx:ERPLParser.AContext):
        return super().visitA(ctx)

    def create_table(self):
        try:
            c = sqlite3.connect(ERPLVis.dbname+'.db').cursor()
            f = open('create.txt')
            st = ''
            for line in f:
                st = st + line
            c.execute(st)
            return c
        except Exception as e:
            print(e)

    def insert_role(role_name):
        sql = 'INSERT INTO roles(name) VALUES(?)'
        cur = sqlite3.connect(ERPLVis.dbname+'.db').cursor()
        cur.execute(sql, (role_name))

    def insert_task(task_name, role_name):
        sql = 'INSERT INTO bar (description, foo_id) VALUES( ?, ?),'
        cur = sqlite3.connect(ERPLVis.dbname+'.db').cursor()
        cur.execute(sql, (task_name, 'SELECT id from roles WHERE type=' + role_name))

    # Visit a parse tree produced by ERPLParser#p.
    def visitP(self, ctx:ERPLParser.PContext):
        self.idP.append(ctx.ID().getText())
        print(ERPLVis.idP)
        global dbname
        dbname = ctx.ID().getText()
        conn = sqlite3.connect(ERPLVis.dbname + '.db')
        c = ERPLVis.create_table(self)
        return super().visitP(ctx)

    # Visit a parse tree produced by ERPLParser#r.
    def visitR(self, ctx: ERPLParser.RContext):
        self.idR.append(ctx.ID().getText())
        print(ERPLVis.idR)
        ERPLVis.insert_role(ctx.ID().getText())
        return super().visitR(ctx)

    # Visit a parse tree produced by ERPLParser#t.
    def visitT(self, ctx:ERPLParser.TContext):
        a = list(ctx.ID())
        self.idT[a[0].getText()] = a[1].getText()
        print(ERPLVis.idT)
        ERPLVis.insert_task(a[0].getText(), a[1].getText())
        return super().visitT(ctx)


    # def visitS(self, ctx: ERPLParser.SContext):
    #     print('hi')
    #     return super().visitS(ctx)
    #
    # def visitR(self, ctx: ERPLParser.RContext):
    #     print(ctx.getText())
    #     return super().visitR(ctx)
    #
    # def visitA(self, ctx: ERPLParser.AContext):
    #     # print(ctx.getText())
    #     return super().visitA(ctx)
    #
    # def visitP(self, ctx: ERPLParser.PContext):
    #     # print(ctx.getText())
    #     # print(ctx.i().n().ID().getText())
    #     # temp = ctx.getText()
    #     # a = temp.spilt()
    #     ERPLVis.idP.append(ctx.i().n().ID().getText())
    #     return super().visitP(ctx)
    #
    # def visitQ(self, ctx: ERPLParser.QContext):
    #     # print(ctx.i().n().ID().getText())
    #     # temp = ctx.getText()
    #     # a = temp.spilt()
    #     ERPLVis.idR.append(ctx.i().n().ID().getText())
    #     # print(ERPLVis.idR)
    #     return super().visitQ(ctx)
    #
    # def visitM(self, ctx: ERPLParser.MContext):
    #     if str(ctx.ID()[0]) not in ERPLVis.idR:
    #         print("The role is not added!")
    #         exit()
    #     if str(ctx.ID()[1]) not in ERPLVis.idP:
    #         print("The process is not added!")
    #         exit()
    #     return super().visitM(ctx)
    #
    # def visitI(self, ctx: ERPLParser.IContext):
    #     # print(ctx.getText())
    #     return super().visitI(ctx)
    #
    # def visitN(self, ctx: ERPLParser.NContext):
    #     # print(ctx.getText())
    #     return super().visitN(ctx)
