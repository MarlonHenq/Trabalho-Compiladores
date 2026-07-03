# Makefile — Compilador DCDraw → SVG
# Targets: generate, run, test, clean, help

PY          = python3
ANTLR       = antlr4
GRAMMAR     = DCDraw.g4
BUILD_DIR   = build
EXEMPLOS    = exemplos

.PHONY: help generate run test clean

help:
	@echo "=== Compilador DCDraw → SVG ==="
	@echo "  make generate                    # antlr4 -visitor DCDraw.g4"
	@echo "  make run INPUT=... OUTPUT=...    # executa o compilador"
	@echo "  make test                        # roda os exemplos de teste"
	@echo "  make clean                       # remove artefatos gerados"

# Gera DCDrawLexer.py, DCDrawParser.py, DCDrawVisitor.py e DCDrawListener.py
generate: $(GRAMMAR)
	$(ANTLR) -Dlanguage=Python3 -visitor $(GRAMMAR)
	@echo "[OK] Artefatos ANTLR gerados."

run:
	@if [ -z "$(INPUT)" ] || [ -z "$(OUTPUT)" ]; then \
		echo "Uso: make run INPUT=arquivo.dc OUTPUT=arquivo.svg"; exit 1; \
	fi
	$(PY) main.py "$(INPUT)" "$(OUTPUT)"

# Testa exemplos validos (devem gerar SVG) e invalidos (devem gerar erro)
test: generate
	@$(PY) -c "import antlr4" 2>/dev/null || { \
		echo "Erro: antlr4-python3-runtime nao instalado."; \
		echo "Rode: pip install -r requirements.txt"; \
		exit 1; \
	}
	@mkdir -p "$(BUILD_DIR)"
	@total=0; passou=0; falhou=0; \
	for entrada in $(EXEMPLOS)/validos/*.dc; do \
		[ -f "$$entrada" ] || continue; \
		base=$$(basename "$$entrada" .dc); \
		saida="$(BUILD_DIR)/$$base.svg"; \
		total=$$((total + 1)); \
		if ! $(PY) main.py "$$entrada" "$$saida" 2>"$(BUILD_DIR)/$$base.log"; then \
			echo "[FAIL] validos/$$base.dc (compilacao falhou — veja $(BUILD_DIR)/$$base.log)"; \
			falhou=$$((falhou + 1)); \
		elif grep -q '<svg' "$$saida" 2>/dev/null; then \
			echo "[OK]   validos/$$base.dc"; \
			passou=$$((passou + 1)); \
		else \
			echo "[FAIL] validos/$$base.dc (esperava SVG)"; \
			falhou=$$((falhou + 1)); \
		fi; \
	done; \
	for entrada in $(EXEMPLOS)/erro_sintatico/*.dc $(EXEMPLOS)/erro_semantico/*.dc; do \
		[ -f "$$entrada" ] || continue; \
		base=$$(basename "$$entrada" .dc); \
		dir=$$(basename $$(dirname "$$entrada")); \
		saida="$(BUILD_DIR)/$$base.err"; \
		total=$$((total + 1)); \
		if ! $(PY) main.py "$$entrada" "$$saida" 2>"$(BUILD_DIR)/$$base.log"; then \
			echo "[FAIL] $$dir/$$base.dc (compilacao falhou — veja $(BUILD_DIR)/$$base.log)"; \
			falhou=$$((falhou + 1)); \
		elif grep -qiE 'erro|nao |deve |fora |obrigatorio|permitida|Fim da compilacao' "$$saida" 2>/dev/null \
		   && ! grep -q '<svg' "$$saida" 2>/dev/null; then \
			echo "[OK]   $$dir/$$base.dc"; \
			passou=$$((passou + 1)); \
		else \
			echo "[FAIL] $$dir/$$base.dc (esperava mensagem de erro)"; \
			falhou=$$((falhou + 1)); \
		fi; \
	done; \
	echo ""; \
	echo "=== $$passou/$$total OK, $$falhou falharam ==="; \
	if [ $$falhou -ne 0 ]; then exit 1; fi

clean:
	rm -f DCDrawLexer.py DCDrawParser.py DCDrawListener.py DCDrawVisitor.py
	rm -f DCDraw.tokens DCDrawLexer.tokens DCDraw.interp DCDrawLexer.interp DCDrawParser.interp
	rm -rf __pycache__
	rm -rf "$(BUILD_DIR)"
	@echo "[OK] Limpo."
