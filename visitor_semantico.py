"""
Visitor semântico da linguagem DCDraw.

Percorre a AST gerada pelo ANTLR4 e acumula erros semânticos sem
interromper a análise. Ao final, os erros são ordenados por linha/coluna.

Verificações implementadas:
  1. Canvas obrigatório, único e no início do arquivo.
  2. Dimensões positivas (largura, altura, raio > 0).
  3. Geometria dentro dos limites do canvas.
  4. Cor presente na paleta (tabela de símbolos).
"""
from __future__ import annotations

from antlr4.Token import Token

from DCDrawParser import DCDrawParser
from DCDrawVisitor import DCDrawVisitor
from tabela_simbolos import TabelaSimbolos


class VisitorSemantico(DCDrawVisitor):
    """
    Visitor principal: percorre a AST e acumula erros semânticos.

    Estado interno:
      tb            – tabela de símbolos (paleta + canvas)
      erros         – lista de (linha, coluna, mensagem)
      _viu_comando  – True após o primeiro comando (para exigir canvas no início)
      _qtd_canvas   – contagem de comandos canvas encontrados
    """

    def __init__(self, ts: TabelaSimbolos) -> None:
        super().__init__()
        self.tb = ts
        self.erros: list[tuple[int, int, str]] = []
        self._viu_comando: bool = False
        self._qtd_canvas: int = 0

    def _erro(self, tok: Token | None, msg: str) -> None:
        """Registra um erro semântico com linha e coluna."""
        if tok is None:
            return
        self.erros.append((tok.line, tok.column, msg))

    def formatar_erros(self) -> str:
        """Ordena os erros e devolve a string de saída com 'Fim da compilacao'."""
        ordenado = sorted(self.erros, key=lambda x: (x[0], x[1], x[2]))
        linhas = [f"Linha {ln}: {msg}" for ln, _c, msg in ordenado]
        linhas.append("Fim da compilacao")
        return "".join(x + "\n" for x in linhas)

    def _num(self, tok: Token) -> int:
        """Converte o texto de um token NUM para int."""
        return int(tok.text)

    def _checar_cor(self, tok: Token) -> None:
        """Verifica se a cor está na paleta da tabela de símbolos."""
        nome = tok.text
        if not self.tb.cor_permitida(nome):
            self._erro(tok, f"cor '{nome}' nao permitida")

    def _checar_ponto_no_canvas(self, tok: Token, x: int, y: int) -> None:
        """Verifica se o ponto (x, y) está dentro dos limites do canvas."""
        if not self.tb.tem_canvas():
            return
        w = self.tb.canvas.largura
        h = self.tb.canvas.altura
        if x < 0 or x > w or y < 0 or y > h:
            self._erro(tok, f"coordenada ({x},{y}) fora dos limites do canvas")

    # ─────────────────────────── programa ─────────────────────────────────

    def visitPrograma(self, ctx: DCDrawParser.ProgramaContext):
        """Visita todos os comandos e, ao final, exige ao menos um canvas."""
        for cmd in ctx.comando():
            self.visit(cmd)

        # Se nenhum canvas foi declarado em lugar nenhum
        if self._qtd_canvas == 0:
            # Usa o primeiro token do programa como referência de linha
            tok = ctx.start
            self._erro(tok, "canvas obrigatorio no inicio do arquivo")

    # ─────────────────────────── canvas ───────────────────────────────────

    def visitCanvas(self, ctx: DCDrawParser.CanvasContext):
        """
        Valida o comando canvas:
          - deve ser o primeiro comando do arquivo
          - deve aparecer uma única vez
          - largura e altura devem ser positivas
        """
        tok = ctx.start
        self._qtd_canvas += 1

        # Canvas duplicado tem prioridade sobre "não é o primeiro"
        if self._qtd_canvas > 1:
            self._erro(tok, "canvas deve ser unico")
            self._viu_comando = True
            return

        if self._viu_comando:
            self._erro(tok, "canvas deve ser o primeiro comando do arquivo")
            self._viu_comando = True
            return

        self._viu_comando = True

        largura = self._num(ctx.NUM(0).symbol)
        altura = self._num(ctx.NUM(1).symbol)

        if largura <= 0 or altura <= 0:
            self._erro(tok, "dimensao deve ser positiva")
            return

        self.tb.definir_canvas(largura, altura)

    # ─────────────────────────── circle ───────────────────────────────────

    def visitCircle(self, ctx: DCDrawParser.CircleContext):
        """Valida círculo: dimensões positivas, limites e cor."""
        tok = ctx.start
        self._viu_comando = True

        cx = self._num(ctx.NUM(0).symbol)
        cy = self._num(ctx.NUM(1).symbol)
        r = self._num(ctx.NUM(2).symbol)
        cor_tok = ctx.IDENT().symbol

        if r <= 0:
            self._erro(tok, "dimensao deve ser positiva")

        self._checar_cor(cor_tok)

        if self.tb.tem_canvas() and r > 0:
            w = self.tb.canvas.largura
            h = self.tb.canvas.altura
            if cx - r < 0 or cx + r > w or cy - r < 0 or cy + r > h:
                self._erro(tok, "geometria fora dos limites do canvas")

    # ─────────────────────────── rect ─────────────────────────────────────

    def visitRect(self, ctx: DCDrawParser.RectContext):
        """Valida retângulo: dimensões positivas, limites e cor."""
        tok = ctx.start
        self._viu_comando = True

        x = self._num(ctx.NUM(0).symbol)
        y = self._num(ctx.NUM(1).symbol)
        largura = self._num(ctx.NUM(2).symbol)
        altura = self._num(ctx.NUM(3).symbol)
        cor_tok = ctx.IDENT().symbol

        if largura <= 0 or altura <= 0:
            self._erro(tok, "dimensao deve ser positiva")

        self._checar_cor(cor_tok)

        if self.tb.tem_canvas() and largura > 0 and altura > 0:
            w = self.tb.canvas.largura
            h = self.tb.canvas.altura
            if x < 0 or y < 0 or x + largura > w or y + altura > h:
                self._erro(tok, "geometria fora dos limites do canvas")

    # ─────────────────────────── line ─────────────────────────────────────

    def visitLine(self, ctx: DCDrawParser.LineContext):
        """Valida linha: ambos os pontos dentro do canvas e cor válida."""
        tok = ctx.start
        self._viu_comando = True

        x1 = self._num(ctx.NUM(0).symbol)
        y1 = self._num(ctx.NUM(1).symbol)
        x2 = self._num(ctx.NUM(2).symbol)
        y2 = self._num(ctx.NUM(3).symbol)
        cor_tok = ctx.IDENT().symbol

        self._checar_cor(cor_tok)

        if self.tb.tem_canvas():
            w = self.tb.canvas.largura
            h = self.tb.canvas.altura
            fora = (
                x1 < 0
                or x1 > w
                or y1 < 0
                or y1 > h
                or x2 < 0
                or x2 > w
                or y2 < 0
                or y2 > h
            )
            if fora:
                self._erro(tok, "geometria fora dos limites do canvas")
