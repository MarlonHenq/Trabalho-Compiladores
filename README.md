# DCDraw (SVGGen)

Compilador de uma linguagem declarativa de desenho geométrico que traduz comandos de texto em arquivos **SVG** válidos.

**Disciplina:** Construção de Compiladores – DC/UFSCar

**Alunos** - Marlon Henrique Sanches - RA819464 | Samuel Gerga Martins - RA821772


## O que é a linguagem?

DCDraw permite descrever formas geométricas simples em um arquivo de texto (`.dc`) e gerar uma imagem vetorial (`.svg`) pronta para abrir no navegador.

Exemplo:

```text
canvas 400 300
circle 100 100 40 red
rect 10 10 80 50 blue
line 0 0 200 150 black
```

Gera um SVG com um círculo vermelho, um retângulo azul e uma linha preta.

## Sintaxe

Cada linha é um comando (comentários começam com `#`):

| Comando  | Argumentos               | Significado                                    |
| -------- | ------------------------ | ---------------------------------------------- |
| `canvas` | `largura altura`         | tamanho da tela (obrigatório, único, primeiro) |
| `circle` | `cx cy r cor`            | círculo                                        |
| `rect`   | `x y largura altura cor` | retângulo                                      |
| `line`   | `x1 y1 x2 y2 cor`        | linha                                          |

### Paleta de cores

Cores são identificadores validados na tabela de símbolos:

`red`, `blue`, `green`, `black`, `white`, `yellow`, `orange`, `purple`, `gray`

### Regras semânticas

1. O comando `canvas` é **obrigatório**, **único** e deve ser o **primeiro** do arquivo.
2. Dimensões (`largura`, `altura`, `raio`) devem ser **positivas** (> 0).
3. A geometria não pode ultrapassar os limites do canvas.
4. A cor deve existir na paleta suportada.

## Pipeline do compilador

1. **Análise léxica** — tokens da linguagem (ANTLR4)
2. **Análise sintática** — estrutura dos comandos
3. **Análise semântica** — canvas, limites, dimensões e cores
4. **Geração de código** — arquivo `.svg` (somente se não houver erros)

Se houver erro, as mensagens vão para o arquivo de saída e também são impressas no terminal (não é gerado SVG).

## Dependências e como instalar

| Dependência             | Versão mínima | Instalação                                        |
| ----------------------- | ------------- | ------------------------------------------------- |
| Python                  | 3.10+         | `sudo apt install python3`                        |
| antlr4-tools            | 0.2+          | `pip install antlr4-tools`                        |
| antlr4-python3-runtime  | 4.13.x        | `pip install -r requirements.txt`                 |
| Java (JRE)              | 11+           | `sudo apt install default-jre` (usado pelo antlr4)|

> A versão do `antlr4-python3-runtime` deve ser compatível com o JAR do ANTLR.
> Recomenda-se `4.13.2`. Se necessário: `export ANTLR4_TOOLS_ANTLR_VERSION=4.13.2`.

## Como compilar o compilador

Gera o lexer, o parser e o visitor a partir da gramática:

```bash
pip install -r requirements.txt
pip install antlr4-tools
make generate
```

Ou diretamente:

```bash
antlr4 -Dlanguage=Python3 -visitor DCDraw.g4
```

Isso gera `DCDrawLexer.py`, `DCDrawParser.py`, `DCDrawVisitor.py` e `DCDrawListener.py`.

## Como executar

```bash
python3 main.py <entrada.dc> <saida.svg>
```

Exemplo:

```bash
python3 main.py exemplos/validos/basico.dc build/basico.svg
```

Via Makefile:

```bash
make run INPUT=exemplos/validos/basico.dc OUTPUT=build/basico.svg
```

Abra o arquivo `build/basico.svg` no navegador para visualizar o desenho.

## Testes

```bash
make test
```

O alvo `test`:

- compila os exemplos em `exemplos/validos/` e verifica se a saída contém `<svg`
- compila os exemplos em `exemplos/erro_sintatico/` e `exemplos/erro_semantico/` e verifica se a saída contém mensagem de erro

## Exemplos de erros

**Sintático** (`exemplos/erro_sintatico/palavra_desconhecida.dc`):

```text
Linha 3: erro sintatico proximo a triangle
Fim da compilacao
```

**Semântico — cor inválida** (`exemplos/erro_semantico/cor_invalida.dc`):

```text
Linha 3: cor 'blux' nao permitida
Fim da compilacao
```

**Semântico — fora dos limites** (`exemplos/erro_semantico/fora_limites.dc`):

```text
Linha 3: geometria fora dos limites do canvas
Fim da compilacao
```

## Limpeza

```bash
make clean
```

## Vídeo De Entrega

[VIDEO](https://drive.google.com/file/d/1PVitflSA3aXOsAKRTLtT685j83F3p4tj/view?usp=sharing)
