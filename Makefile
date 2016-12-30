BASEDIR=$(CURDIR)
INPUT_DIR=$(BASEDIR)/blog
OUTPUT_DIR=$(BASEDIR)/_site

SERVE_PORT=8080


help:
	@echo 'Makefile for the PyLadies blog, written with Mynt                       '
	@echo '                                                                        '
	@echo 'Usage:                                                                  '
	@echo '   make generate                    generate the web site               '
	@echo '   make clean                       remove the generated files          '
	@echo '   make serve                       serve site at http://localhost:8080 '
	@echo '   make watch                       auto-regenerate after changes       '
	@echo '   make test                        run the (simple) tests              '
	@echo '                                                                        '


clean:
	[ ! -d $(OUTPUT_DIR) ] || find $(OUTPUT_DIR) -mindepth 1 -delete

test:
	python test_www.py

generate: clean
	mynt gen -f blog _site

watch: clean
	mynt watch -f blog _site

serve: generate
	mynt serve -p $(SERVE_PORT) $(OUTPUT_DIR)


.PHONY: check test regenerate watch serve
