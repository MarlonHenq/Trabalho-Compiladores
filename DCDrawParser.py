# Generated from DCDraw.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,0,
        14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,0,47,0,13,1,0,0,0,
        2,23,1,0,0,0,4,25,1,0,0,0,6,29,1,0,0,0,8,35,1,0,0,0,10,42,1,0,0,
        0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,
        1,0,0,0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,24,3,4,2,0,20,
        24,3,6,3,0,21,24,3,8,4,0,22,24,3,10,5,0,23,19,1,0,0,0,23,20,1,0,
        0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,1,0,0,26,27,
        5,5,0,0,27,28,5,5,0,0,28,5,1,0,0,0,29,30,5,2,0,0,30,31,5,5,0,0,31,
        32,5,5,0,0,32,33,5,5,0,0,33,34,5,6,0,0,34,7,1,0,0,0,35,36,5,3,0,
        0,36,37,5,5,0,0,37,38,5,5,0,0,38,39,5,5,0,0,39,40,5,5,0,0,40,41,
        5,6,0,0,41,9,1,0,0,0,42,43,5,4,0,0,43,44,5,5,0,0,44,45,5,5,0,0,45,
        46,5,5,0,0,46,47,5,5,0,0,47,48,5,6,0,0,48,11,1,0,0,0,2,15,23
    ]

class DCDrawParser ( Parser ):

    grammarFileName = "DCDraw.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'canvas'", "'circle'", "'rect'", "'line'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "IDENT", "COMENTARIO", "WS" ]

    RULE_programa = 0
    RULE_comando = 1
    RULE_canvas = 2
    RULE_circle = 3
    RULE_rect = 4
    RULE_line = 5

    ruleNames =  [ "programa", "comando", "canvas", "circle", "rect", "line" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUM=5
    IDENT=6
    COMENTARIO=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DCDrawParser.EOF, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DCDrawParser.ComandoContext)
            else:
                return self.getTypedRuleContext(DCDrawParser.ComandoContext,i)


        def getRuleIndex(self):
            return DCDrawParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = DCDrawParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.comando()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                    break

            self.state = 17
            self.match(DCDrawParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def canvas(self):
            return self.getTypedRuleContext(DCDrawParser.CanvasContext,0)


        def circle(self):
            return self.getTypedRuleContext(DCDrawParser.CircleContext,0)


        def rect(self):
            return self.getTypedRuleContext(DCDrawParser.RectContext,0)


        def line(self):
            return self.getTypedRuleContext(DCDrawParser.LineContext,0)


        def getRuleIndex(self):
            return DCDrawParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = DCDrawParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.canvas()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.circle()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.rect()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.line()
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


    class CanvasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(DCDrawParser.NUM)
            else:
                return self.getToken(DCDrawParser.NUM, i)

        def getRuleIndex(self):
            return DCDrawParser.RULE_canvas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCanvas" ):
                listener.enterCanvas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCanvas" ):
                listener.exitCanvas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCanvas" ):
                return visitor.visitCanvas(self)
            else:
                return visitor.visitChildren(self)




    def canvas(self):

        localctx = DCDrawParser.CanvasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_canvas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(DCDrawParser.T__0)
            self.state = 26
            self.match(DCDrawParser.NUM)
            self.state = 27
            self.match(DCDrawParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CircleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(DCDrawParser.NUM)
            else:
                return self.getToken(DCDrawParser.NUM, i)

        def IDENT(self):
            return self.getToken(DCDrawParser.IDENT, 0)

        def getRuleIndex(self):
            return DCDrawParser.RULE_circle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircle" ):
                listener.enterCircle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircle" ):
                listener.exitCircle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCircle" ):
                return visitor.visitCircle(self)
            else:
                return visitor.visitChildren(self)




    def circle(self):

        localctx = DCDrawParser.CircleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_circle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(DCDrawParser.T__1)
            self.state = 30
            self.match(DCDrawParser.NUM)
            self.state = 31
            self.match(DCDrawParser.NUM)
            self.state = 32
            self.match(DCDrawParser.NUM)
            self.state = 33
            self.match(DCDrawParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(DCDrawParser.NUM)
            else:
                return self.getToken(DCDrawParser.NUM, i)

        def IDENT(self):
            return self.getToken(DCDrawParser.IDENT, 0)

        def getRuleIndex(self):
            return DCDrawParser.RULE_rect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRect" ):
                listener.enterRect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRect" ):
                listener.exitRect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRect" ):
                return visitor.visitRect(self)
            else:
                return visitor.visitChildren(self)




    def rect(self):

        localctx = DCDrawParser.RectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(DCDrawParser.T__2)
            self.state = 36
            self.match(DCDrawParser.NUM)
            self.state = 37
            self.match(DCDrawParser.NUM)
            self.state = 38
            self.match(DCDrawParser.NUM)
            self.state = 39
            self.match(DCDrawParser.NUM)
            self.state = 40
            self.match(DCDrawParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(DCDrawParser.NUM)
            else:
                return self.getToken(DCDrawParser.NUM, i)

        def IDENT(self):
            return self.getToken(DCDrawParser.IDENT, 0)

        def getRuleIndex(self):
            return DCDrawParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = DCDrawParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(DCDrawParser.T__3)
            self.state = 43
            self.match(DCDrawParser.NUM)
            self.state = 44
            self.match(DCDrawParser.NUM)
            self.state = 45
            self.match(DCDrawParser.NUM)
            self.state = 46
            self.match(DCDrawParser.NUM)
            self.state = 47
            self.match(DCDrawParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





