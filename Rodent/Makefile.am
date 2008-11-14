
SUBDIRS = 48x48

indexdir = $(datadir)/icons/Rodent-2
index_in_files =							\
	index.theme.in

index_DATA = $(index_in_files:.in=)
@INTLTOOL_THEME_RULE@

EXTRA_DIST =								\
	$(index_in_files)

DISTCLEANFILES =							\
	$(index_DATA)

gtk_update_icon_cache = gtk-update-icon-cache -f -t $(datadir)/icons/Rodent-2

install-data-hook:
	@-if test -z "$(DESTDIR)"; then					\
                echo "Updating Gtk icon cache.";			\
                $(gtk_update_icon_cache);				\
        else								\
                echo "*** Icon cache not updated. Remember to run:";	\
		echo "***";						\
                echo "***   $(gtk_update_icon_cache)";			\
		echo "***";						\
        fi

# vi:set ts=8 sw=8 noet ai nocindent:
