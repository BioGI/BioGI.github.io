html:
	scholdoc webpage-settings.yml Scholarly-Markdown-Guide.md --citeproc --output=Scholarly-Markdown-Guide.html

latex:
	scholdoc plos-one-settings.yml Scholarly-Markdown-Guide.md --natbib --output=Scholarly-Markdown-Guide.tex

# Need the `latexmk` program to automate LaTeX builds (included with texlive)
pdf: latex
	pdflatex -pdf Scholarly-Markdown-Guide.tex

# Scholdoc native PDF output doesn't call bibtex
autopdf:
	scholdoc plos-one-settings.yml Scholarly-Markdown-Guide.md --citeproc --to=latex --output=Scholarly-Markdown-Guide_generatedByScholdoc.pdf

clean:
	-[[ -f "Scholarly-Markdown-Guide.aux" ]] && latexmk -c
	-[[ -f "Scholarly-Markdown-Guide.tex" ]] && rm Scholarly-Markdown-Guide.tex
	-[[ -f "Scholarly-Markdown-Guide.bbl" ]] && rm Scholarly-Markdown-Guide.bbl
	-[[ -f "Scholarly-Markdown-Guide.pdf" ]] && rm Scholarly-Markdown-Guide.pdf
	-[[ -f "Scholarly-Markdown-Guide.html" ]] && rm Scholarly-Markdown-Guide.html
	-[[ -f "Scholarly-Markdown-Guide_generatedByScholdoc.pdf" ]] && rm Scholarly-Markdown-Guide_generatedByScholdoc.pdf

.PHONY: html latex pdf autopdf clean
