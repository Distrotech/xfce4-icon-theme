SUBDIRS = Rodent mime

distclean-local:
	rm -rf xfce4-icon-theme.spec *.cache *~

rpm: dist
	rpmbuild -ta $(PACKAGE)-$(VERSION).tar.gz
	@rm -f $(PACKAGE)-$(VERSION).tar.gz

install-data-local:
	$(mkinstalldirs) $(DESTDIR)$(datadir)/icons
	( cd $(DESTDIR)$(datadir)/icons; \
	  rm -f Rodent-svg; \
	)

EXTRA_DIST =								\
	AUTHORS								\
	COPYING								\
	ChangeLog							\
	INSTALL								\
	NEWS								\
	NOTES								\
	README								\
	TODO								\
	xfce4-icon-theme.spec 



dist-bz2: dist
	zcat $(PACKAGE)-$(VERSION).tar.gz | bzip2 --best -c > $(PACKAGE)-$(VERSION).tar.bz2

distcheck-bz2: distcheck
	zcat $(PACKAGE)-$(VERSION).tar.gz | bzip2 --best -c > $(PACKAGE)-$(VERSION)$.tar.bz2
