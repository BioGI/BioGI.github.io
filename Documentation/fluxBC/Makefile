html:
	scholdoc webpage-settings.yml fluxBC.md --citeproc --output=fluxBC.html

latex:
	scholdoc plos-one-settings.yml fluxBC.md --natbib --output=fluxBC.tex

# Need the `latexmk` program to automate LaTeX builds (included with texlive)
pdf: latex
	pdflatex -pdf fluxBC.tex

# Scholdoc native PDF output doesn't call bibtex
autopdf:
	scholdoc plos-one-settings.yml fluxBC.md --citeproc --to=latex --output=fluxBC_generatedByScholdoc.pdf

clean:
	-[[ -f "fluxBC.aux" ]] && latexmk -c
	-[[ -f "fluxBC.tex" ]] && rm fluxBC.tex
	-[[ -f "fluxBC.bbl" ]] && rm fluxBC.bbl
	-[[ -f "fluxBC.pdf" ]] && rm fluxBC.pdf
	-[[ -f "fluxBC.html" ]] && rm fluxBC.html
	-[[ -f "fluxBC_generatedByScholdoc.pdf" ]] && rm fluxBC_generatedByScholdoc.pdf

.PHONY: html latex pdf autopdf clean
