indexdir = $(datadir)/icons/Rodent
SUBDIRS = 48x48 scalable
index_DATA = index.theme iconrc iconrc-png
EXTRA_DIST =  $(index_DATA) iconrc.in iconrc-png.in

distclean-local:
	rm -f iconrc iconrc-png
	
iconrc: Makefile iconrc.in
	@sed -e "s%DATADIR%$(datadir)%g" iconrc.in > iconrc

iconrc-png: Makefile iconrc-png.in
	@sed -e "s%DATADIR%$(datadir)%g" iconrc-png.in > iconrc-png
