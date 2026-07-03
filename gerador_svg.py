"""
Gerador de código SVG a partir da AST da linguagem DCDraw.

Percorre a árvore sintática (gerada pelo ANTLR4) e emite um arquivo SVG
válido, pronto para abrir em qualquer navegador.

Mapeamento DCDraw → SVG:
  canvas w h              →  <svg width="w" height="h" ...>
  circle cx cy r cor      →  <circle cx="..." cy="..." r="..." fill="..."/>
  rect x y w h cor        →  <rect x="..." y="..." width="..." height="..." fill="..."/>
  line x1 y1 x2 y2 cor    →  <line x1="..." y1="..." x2="..." y2="..." stroke="..."/>
"""
from __future__ import annotations

from DCDrawParser import DCDrawParser
from DCDrawVisitor import DCDrawVisitor


class GeradorSVG(DCDrawVisitor):
    """
    Visitor de geração de código: traduz comandos DCDraw em tags SVG.

    Estado interno:
      _linhas   – lista de strings que formam o SVG final
      _largura  – largura do canvas (preenchida ao visitar canvas)
      _altura   – altura do canvas
    """

    def __init__(self) -> None:
        super().__init__()
        self._linhas: list[str] = []
        self._largura: int = 0
        self._altura: int = 0

    def gerar(self) -> str:
        """Monta o documento SVG completo a partir das linhas acumuladas."""
        partes = [
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{self._largura}" height="{self._altura}">',
            *self._linhas,
            "</svg>",
            "",
        ]
        return "\n".join(partes)

    def _num(self, ctx_num) -> str:
        """Extrai o texto de um token NUM."""
        return ctx_num.getText()

    def visitPrograma(self, ctx: DCDrawParser.ProgramaContext):
        for cmd in ctx.comando():
            self.visit(cmd)

    def visitCanvas(self, ctx: DCDrawParser.CanvasContext):
        self._largura = int(ctx.NUM(0).getText())
        self._altura = int(ctx.NUM(1).getText())

    def visitCircle(self, ctx: DCDrawParser.CircleContext):
        cx = self._num(ctx.NUM(0))
        cy = self._num(ctx.NUM(1))
        r = self._num(ctx.NUM(2))
        cor = ctx.IDENT().getText()
        self._linhas.append(
            f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{cor}"/>'
        )

    def visitRect(self, ctx: DCDrawParser.RectContext):
        x = self._num(ctx.NUM(0))
        y = self._num(ctx.NUM(1))
        w = self._num(ctx.NUM(2))
        h = self._num(ctx.NUM(3))
        cor = ctx.IDENT().getText()
        self._linhas.append(
            f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{cor}"/>'
        )

    def visitLine(self, ctx: DCDrawParser.LineContext):
        x1 = self._num(ctx.NUM(0))
        y1 = self._num(ctx.NUM(1))
        x2 = self._num(ctx.NUM(2))
        y2 = self._num(ctx.NUM(3))
        cor = ctx.IDENT().getText()
        self._linhas.append(
            f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{cor}" stroke-width="2"/>'
        )
