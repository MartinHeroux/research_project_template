FILE=notes

# Rule to generate manuscript. Unecessary files are deleted and $(FILE).pdf is copied to ../../doc/$(FILE)/
$(FILE).pdf: $(FILE).tex
	pdflatex $(FILE)
	bibtex $(FILE)
	pdflatex $(FILE)
	pdflatex $(FILE)
	rm -f $(FILE).log $(FILE).aux $(FILE).bbl $(FILE).blg $(FILE).out $(FILE).synctex.gz
	cp $(FILE).pdf ../../doc/$(FILE)/
	evince ../../doc/$(FILE)/$(FILE).pdf &

# Rule to delete $(FILE).pdf in root folder
.PHONY = clean
clean:
	rm $(FILE).pdf
