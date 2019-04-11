import sys

from ERPLLexer import ERPLLexer
from ERPLVis import ERPLVis
from ERPLParser import ERPLParser
from antlr4 import *

def main():
    filepath = "temp.erpl"
    input = FileStream(filepath)
    lexer = ERPLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ERPLParser(stream)
    tree = parser.s()

    visitor = ERPLVis()
    return visitor.visit(tree)


if __name__ == '__main__':

    main()
