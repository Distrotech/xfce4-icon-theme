SUBDIRS = Rodent mime

EXTRA_DIST = xfce4-icon-theme.spec 

distclean-local:
	rm -rf xfce4-icon-theme.spec *.cache *~

rpm: dist
	rpmbuild -ta $(PACKAGE)-$(VERSION).tar.gz
	@rm -f $(PACKAGE)-$(VERSION).tar.gz

