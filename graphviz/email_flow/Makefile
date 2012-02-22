include dotlist.mak

all: $(FILES)

# if using ''nmake'', all explicit rule must be written

##smtp.png:	smtp.dot
##	dot -Tpng -o $@ smtp.dot
###	start $@
##
##smtp_proc.png:	smtp_proc.dot
##	dot -Tpng -o $@ smtp_proc.dot
###	start $@
##
##smtp_scan.png:	smtp_scan.dot
##	dot -Tpng -o $@ smtp_scan.dot
###	start $@
##
##smtp_parse_header.png: smtp_parse_header.dot
##	dot -Tpng -o $@ smtp_parse_header.dot
###	start $@
##
##smtp_frame.png: smtp_frame.dot
##	dot -Tpng -o $@ smtp_frame.dot
###	start $@

clean:
	rm -f *.png *.gif *.jpg *.jpe

%.png: %.dot
	dot -Tpng -o $@ $<

%.gif: %.dot
	dot -Tgif -o $@ $<
#	neato -Tgif -o $@ $<

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
