html:

#	scholdoc webpage-settings.yml SummaryofPreviousWorks.md --citeproc --output=SummaryofPreviousWorks.html
#	scholdoc webpage-settings.yml lbmBasics.md --citeproc --output=lbmBasics.html
#	scholdoc webpage-settings.yml ginoReproduce.md --citeproc --output=ginoReproduce.html
#	scholdoc webpage-settings.yml monoVsPolydisperse.md --citeproc --output=monoVsPolydisperse.html
#	scholdoc webpage-settings.yml howToInstallScholdoc.md --citeproc --output=howToInstallScholdoc.html
#	scholdoc webpage-settings.yml HowToModifyWiki.md --citeproc --output=HowToModifyWiki.html
#	scholdoc webpage-settings.yml Dissolution-Model-Implementation.md --citeproc --output=Dissolution-Model-Implementation.html
#	scholdoc webpage-settings.yml ParticleTrackingDrugRelease.md --citeproc --output=ParticleTrackingDrugRelease.html
#	scholdoc webpage-settings.yml plannedMultiblockImplementation.md --citeproc --output=plannedMultiblockImplementation.html
#	scholdoc webpage-settings.yml Couette-Pseudo-Code.md --citeproc --output=Couette-Pseudo-Code.html
#	scholdoc webpage-settings.yml JanusSupercomputerTour.md --citeproc --output=JanusSupercomputerTour.html
#	scholdoc webpage-settings.yml newParticleDissolutionModel.md --citeproc --output=newParticleDissolutionModel.html
#	scholdoc webpage-settings.yml firstStudy.md --citeproc --output=firstStudy.html
#	scholdoc webpage-settings.yml Janus_Runs.md --citeproc --output=Janus_Runs.html
#	scholdoc webpage-settings.yml Paraview_Script.md --citeproc --output=Paraview_Script.html
	scholdoc webpage-settings.yml Strain_Rate_Correlations.md --citeproc --output=Strain_Rate_Correlations.html
	scholdoc webpage-settings.yml Motility_Concentration_Data.md --citeproc --output=Motility_Concentration_Data.html

latex:
	scholdoc plos-one-settings.yml lbmBasics.md --natbib --output=lbmBasics.tex

# Need the `latexmk` program to automate LaTeX builds (included with texlive)
pdf: latex
	pdflatex -pdf lbmBasics.tex

# Scholdoc native PDF output doesn't call bibtex
autopdf:
	scholdoc plos-one-settings.yml lbmBasics.md --citeproc --to=latex --output=lbmBasics_generatedByScholdoc.pdf

clean:
	-[[ -f "lbmBasics.aux" ]] && latexmk -c
	-[[ -f "lbmBasics.tex" ]] && rm lbmBasics.tex
	-[[ -f "lbmBasics.bbl" ]] && rm lbmBasics.bbl
	-[[ -f "lbmBasics.pdf" ]] && rm lbmBasics.pdf
	-[[ -f "lbmBasics.html" ]] && rm lbmBasics.html
	-[[ -f "lbmBasics_generatedByScholdoc.pdf" ]] && rm lbmBasics_generatedByScholdoc.pdf

.PHONY: html latex pdf autopdf clean


