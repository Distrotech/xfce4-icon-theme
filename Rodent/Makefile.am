indexdir = $(datadir)/icons/Rodent
SUBDIRS = 48x48 scalable
index_DATA = index.theme iconrc iconrc-png
EXTRA_DIST =  index.theme iconrc.in iconrc-png.in

distclean-local:
	rm -f iconrc iconrc-png
	
iconrc: $(top_srcdir)/Rodent/iconrc.in
	@sed -e "s%DATADIR%$(datadir)%g" $(top_srcdir)/Rodent/iconrc.in > iconrc

iconrc-png: $(top_srcdir)/Rodent/iconrc-png.in
	@sed -e "s%DATADIR%$(datadir)%g" $(top_srcdir)/Rodent/iconrc-png.in > iconrc-png
