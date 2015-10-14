html:
	scholdoc webpage-settings.yml index.md --citeproc --output=index.html

latex:
	scholdoc plos-one-settings.yml index.md --natbib --output=index.tex

# Need the `latexmk` program to automate LaTeX builds (included with texlive)
pdf: latex
	pdflatex -pdf index.tex

# Scholdoc native PDF output doesn't call bibtex
autopdf:
	scholdoc plos-one-settings.yml index.md --citeproc --to=latex --output=index_generatedByScholdoc.pdf

clean:
	-[[ -f "index.aux" ]] && latexmk -c
	-[[ -f "index.tex" ]] && rm index.tex
	-[[ -f "index.bbl" ]] && rm index.bbl
	-[[ -f "index.pdf" ]] && rm index.pdf
	-[[ -f "index.html" ]] && rm index.html
	-[[ -f "index_generatedByScholdoc.pdf" ]] && rm index_generatedByScholdoc.pdf

.PHONY: html latex pdf autopdf clean
