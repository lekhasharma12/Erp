import sys

from ERPLLexer import ERPLLexer
from ERPLVis import ERPLVis
from ERPLCustomListener import ERPLCustomListener
from ERPLParser import ERPLParser
from antlr4 import *

def main():
    filepath = "temp.erpl"
    input = FileStream(filepath)
    lexer = ERPLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ERPLParser(stream)
    tree = parser.s()

    # visitor = ERPLVis()
    # return visitor.visit(tree)
    listener = ERPLCustomListener()
    walker = ParseTreeWalker()
    return walker.walk(listener, tree)


if __name__ == '__main__':

    main()
