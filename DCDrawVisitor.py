# Generated from DCDraw.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DCDrawParser import DCDrawParser
else:
    from DCDrawParser import DCDrawParser

# This class defines a complete generic visitor for a parse tree produced by DCDrawParser.

class DCDrawVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DCDrawParser#programa.
    def visitPrograma(self, ctx:DCDrawParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DCDrawParser#comando.
    def visitComando(self, ctx:DCDrawParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DCDrawParser#canvas.
    def visitCanvas(self, ctx:DCDrawParser.CanvasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DCDrawParser#circle.
    def visitCircle(self, ctx:DCDrawParser.CircleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DCDrawParser#rect.
    def visitRect(self, ctx:DCDrawParser.RectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DCDrawParser#line.
    def visitLine(self, ctx:DCDrawParser.LineContext):
        return self.visitChildren(ctx)



del DCDrawParser