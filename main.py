#!/usr/bin/env python3
"""
CLI

Uso:
    python3 main.py <arquivo_entrada.dc> <arquivo_saida.svg>

Pipeline:
  1. Leitura do arquivo com FileStream (UTF-8).
  2. Análise léxica (DCDrawLexer).
  3. Análise sintática (DCDrawParser): primeiro erro interrompe.
  4. Análise semântica (VisitorSemantico): acumula todos os erros.
  5. Se não houver erros, executa o GeradorSVG para produzir o SVG.
"""
from __future__ import annotations

import sys
from pathlib import Path

from antlr4 import CommonTokenStream, FileStream
from antlr4.error.ErrorListener import ErrorListener

from DCDrawLexer import DCDrawLexer
from DCDrawParser import DCDrawParser

from tabela_simbolos import TabelaSimbolos
from visitor_semantico import VisitorSemantico
from gerador_svg import GeradorSVG


class ErroSintaticoException(Exception):
    """Sinaliza que o parser encontrou um erro """

    pass


class CustomErrorListener(ErrorListener):

    def __init__(self) -> None:
        super().__init__()
        self.mensagem_erro: str | None = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if self.mensagem_erro is not None:
            raise ErroSintaticoException()
        texto_token = offendingSymbol.text if offendingSymbol else "EOF"
        if texto_token == "<EOF>":
            texto_token = "EOF"
        self.mensagem_erro = f"Linha {line}: erro sintatico proximo a {texto_token}"
        raise ErroSintaticoException()


def gravar_saida(path: Path, conteudo: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(conteudo, encoding="utf-8")


def reportar_erros(path: Path, conteudo: str) -> None:
    gravar_saida(path, conteudo)
    sys.stderr.write(conteudo)
    if not conteudo.endswith("\n"):
        sys.stderr.write("\n")


def main() -> None:
    if len(sys.argv) != 3:
        sys.stderr.write("Uso: python3 main.py <arquivo_entrada> <arquivo_saida>\n")
        sys.exit(1)

    caminho_entrada = Path(sys.argv[1])
    caminho_saida = Path(sys.argv[2])

    # ── 1. Leitura e análise léxica ──────────────────────────────────────
    fluxo = FileStream(str(caminho_entrada), encoding="utf-8")
    lexer = DCDrawLexer(fluxo)
    lexer.removeErrorListeners()
    fts = CommonTokenStream(lexer)

    # ── 2. Análise sintática ──────────────────────────────────────────────
    parser = DCDrawParser(fts)
    parser.removeErrorListeners()
    lst = CustomErrorListener()
    parser.addErrorListener(lst)

    tree = None
    try:
        tree = parser.programa()
    except ErroSintaticoException:
        pass

    if lst.mensagem_erro:
        reportar_erros(
            caminho_saida,
            lst.mensagem_erro + "\nFim da compilacao\n",
        )
        return

    # ── 3. Análise semântica ──────────────────────────────────────────────
    ts = TabelaSimbolos()
    vis = VisitorSemantico(ts)
    vis.visit(tree)

    if vis.erros:
        reportar_erros(caminho_saida, vis.formatar_erros())
        return

    # ── 4. Geração de código SVG ──────────────────────────────────────────
    gerador = GeradorSVG()
    gerador.visit(tree)
    gravar_saida(caminho_saida, gerador.gerar())


if __name__ == "__main__":
    main()
