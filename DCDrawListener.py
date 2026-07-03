# Generated from DCDraw.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DCDrawParser import DCDrawParser
else:
    from DCDrawParser import DCDrawParser

# This class defines a complete listener for a parse tree produced by DCDrawParser.
class DCDrawListener(ParseTreeListener):

    # Enter a parse tree produced by DCDrawParser#programa.
    def enterPrograma(self, ctx:DCDrawParser.ProgramaContext):
        pass

    # Exit a parse tree produced by DCDrawParser#programa.
    def exitPrograma(self, ctx:DCDrawParser.ProgramaContext):
        pass


    # Enter a parse tree produced by DCDrawParser#comando.
    def enterComando(self, ctx:DCDrawParser.ComandoContext):
        pass

    # Exit a parse tree produced by DCDrawParser#comando.
    def exitComando(self, ctx:DCDrawParser.ComandoContext):
        pass


    # Enter a parse tree produced by DCDrawParser#canvas.
    def enterCanvas(self, ctx:DCDrawParser.CanvasContext):
        pass

    # Exit a parse tree produced by DCDrawParser#canvas.
    def exitCanvas(self, ctx:DCDrawParser.CanvasContext):
        pass


    # Enter a parse tree produced by DCDrawParser#circle.
    def enterCircle(self, ctx:DCDrawParser.CircleContext):
        pass

    # Exit a parse tree produced by DCDrawParser#circle.
    def exitCircle(self, ctx:DCDrawParser.CircleContext):
        pass


    # Enter a parse tree produced by DCDrawParser#rect.
    def enterRect(self, ctx:DCDrawParser.RectContext):
        pass

    # Exit a parse tree produced by DCDrawParser#rect.
    def exitRect(self, ctx:DCDrawParser.RectContext):
        pass


    # Enter a parse tree produced by DCDrawParser#line.
    def enterLine(self, ctx:DCDrawParser.LineContext):
        pass

    # Exit a parse tree produced by DCDrawParser#line.
    def exitLine(self, ctx:DCDrawParser.LineContext):
        pass



del DCDrawParser