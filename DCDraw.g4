/*
 * Gramática da linguagem DCDraw (SVGGen)
 * ========================================
 * Compilador declarativo de desenho geométrico → SVG
 *
 * A gramática é propositalmente permissiva quanto ao canvas:
 * a obrigatoriedade, unicidade e posição do comando 'canvas'
 * são verificadas na análise semântica (não na sintaxe).
 *
 * Comandos suportados:
 *   canvas  largura altura
 *   circle  cx cy r cor
 *   rect    x y largura altura cor
 *   line    x1 y1 x2 y2 cor
 *
 * Cores são IDENT (ex: red, blue) e validadas na tabela de símbolos.
 */
grammar DCDraw;

/* Ponto de entrada: um ou mais comandos */
programa
    : comando+ EOF
    ;

comando
    : canvas
    | circle
    | rect
    | line
    ;

/* Define o tamanho da tela de desenho */
canvas
    : 'canvas' NUM NUM
    ;

/* Círculo: centro (cx, cy), raio r e cor */
circle
    : 'circle' NUM NUM NUM IDENT
    ;

/* Retângulo: canto superior esquerdo (x, y), largura, altura e cor */
rect
    : 'rect' NUM NUM NUM NUM IDENT
    ;

/* Linha: ponto inicial (x1, y1), ponto final (x2, y2) e cor */
line
    : 'line' NUM NUM NUM NUM IDENT
    ;

/* ── Tokens léxicos ─────────────────────────────────────────────── */

/* Números inteiros não negativos (dimensões e coordenadas) */
NUM
    : [0-9]+
    ;

/* Identificadores: usados para nomes de cores */
IDENT
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

/* Comentários de linha iniciados por '#' */
COMENTARIO
    : '#' ~[\r\n]* -> skip
    ;

/* Espaços em branco e quebras de linha */
WS
    : [ \t\r\n]+ -> skip
    ;
