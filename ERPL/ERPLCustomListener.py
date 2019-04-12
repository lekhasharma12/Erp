from ERPLListener import ERPLListener as EL
from ERPLParser import ERPLParser
import sqlite3
import os
import sys
import subprocess


class ERPLCustomListener(EL) :
    idP = []
    idR = []
    idT = {}
    dbname = ''

    def create_table(self):
        sql_create_roles_table = " CREATE TABLE IF NOT EXISTS roles (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(32) NOT NULL); "

        sql_create_tasks_table = "CREATE TABLE IF NOT EXISTS  tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(32) NOT NULL, role_id int NOT NULL, FOREIGN KEY (role_id) REFERENCES roles (id));"

        # create a database connection
        conn = sqlite3.connect(self.dbname+'.db')
        if conn is not None:
            # create projects table
            try:
                c = conn.cursor()
                c.execute(sql_create_roles_table)
                conn.commit()
            except Exception as e:
                print(e)
            try:
                c = conn.cursor()
                c.execute(sql_create_tasks_table)
                conn.commit()
            except Exception as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")

    def insert_role(self, role_name):
        conn = sqlite3.connect(self.dbname+'.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO roles(name) VALUES(?)', (role_name, ))
        conn.commit()
        conn.close()
        cur = sqlite3.connect(self.dbname + '.db').cursor()
        c = cur.execute('SELECT * FROM roles')
        c = c.fetchall()
        print(c)

    def insert_task(self, task_name, role_name):
        conn = sqlite3.connect(self.dbname + '.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO tasks (name, role_id) VALUES( ?, ?)', (task_name, 'SELECT id from roles WHERE name=' + role_name,))
        conn.commit()
        conn.close()

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
        # print(ctx.getText())
        # print(self.idR)
        # print(self.idP)
        # print(self.idT)
        pass


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
        #global dbname
        self.dbname = ctx.ID().getText()
        print(self.dbname)
        conn = sqlite3.connect(self.dbname + '.db')
        conn.commit()
        print('ki')
        ERPLCustomListener.create_table(self)
        for i in self.idR:
            ERPLCustomListener.insert_role(self, i)
        for i in self.idT:
            ERPLCustomListener.insert_task(self, i, self.idT[i])

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



    def enterI(self, ctx:ERPLParser.IContext):
        pass

    # Exit a parse tree produced by ERPLParser#i.
    def exitI(self, ctx:ERPLParser.IContext):
        os.system("python "+ ctx.ID().getText() +".py" )
        # s2_out = subprocess.check_output(["python ", ctx.ID().getText() +".py", "34"])
        # print(s2_out)

