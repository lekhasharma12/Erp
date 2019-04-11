from antlr4 import *
from ERPLLexer import ERPLLexer
from ERPLListener import ERPLListener
from ERPLParser import ERPLParser
import sys
class ERPLPrintListener(ERPLListener):
    def enterHi(self, ctx):
        print("ERPL: %s" % ctx.ID())
def main():
    lexer = ERPLLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = ERPLParser(stream)
    tree = parser.hi()
    printer = ERPLPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
if __name__ == '__main__':
    main()