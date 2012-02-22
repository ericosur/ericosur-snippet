all: overview.gif overview.png overview.jpg overview.jpe

clean:
	rm -f *.png *.gif *.jpg *.jpe

%.png: %.dot
	dot -Tpng -o $@ $<

%.gif: %.dot
	neato -Tgif -o $@ $<

%.jpg: %.dot
	fdp -Tjpg -o $@ $<

%.jpe: %.dot
	twopi -Tjpg -o $@ $<

#test.png:	makefile printer.dot
#	@echo $@
#	@echo $<
#	@echo $?

#
# circo dot fdp neato twopi
#
# dot => png
# neato => gif
# fdp => jpg
# twopi => jpe
