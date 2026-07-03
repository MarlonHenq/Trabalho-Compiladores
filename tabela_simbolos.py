from __future__ import annotations

from dataclasses import dataclass


# Paleta mínima suportada pelo compilador.
CORES_PADRAO: frozenset[str] = frozenset(
    {
        "red",
        "blue",
        "green",
        "black",
        "white",
        "yellow",
        "orange",
        "purple",
        "gray",
    }
)


@dataclass
class CanvasInfo:
    """Dimensões da tela de desenho declaradas pelo comando canvas"""

    largura: int
    altura: int


class TabelaSimbolos:
    def __init__(self) -> None:
        # Mapa nome → True (presença basta para validar a cor)
        self._cores: dict[str, bool] = {c: True for c in CORES_PADRAO}
        self.canvas: CanvasInfo | None = None

    def cor_permitida(self, nome: str) -> bool:
        """Retorna True se a cor existe na paleta suportada."""
        return nome in self._cores

    def definir_canvas(self, largura: int, altura: int) -> None:
        """Registra as dimensões do canvas."""
        self.canvas = CanvasInfo(largura=largura, altura=altura)

    def tem_canvas(self) -> bool:
        """Indica se o canvas já foi declarado."""
        return self.canvas is not None
