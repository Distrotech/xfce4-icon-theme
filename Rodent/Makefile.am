@SET_MAKE@

SUBDIRS =								\
	48x48								\
	scalable

indexdir = $(datadir)/icons/Rodent
index_in_files =							\
	index.theme.in							\
	iconrc.in							\
	iconrc-png.in
index_DATA = $(index_in_files:.in=)
@INTLTOOL_THEME_RULE@


iconrc: $(top_srcdir)/Rodent/iconrc.in
	@sed -e "s%DATADIR%$(datadir)%g" $(top_srcdir)/Rodent/iconrc.in > iconrc

iconrc-png: $(top_srcdir)/Rodent/iconrc-png.in
	@sed -e "s%DATADIR%$(datadir)%g" $(top_srcdir)/Rodent/iconrc-png.in > iconrc-png


EXTRA_DIST =								\
	$(index_in_files)

DISTCLEANFILES =							\
	$(index_DATA)

