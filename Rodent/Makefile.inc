
if DISABLE_DEPRECATED
icon_DATA = \
	$(icon_naming_spec_compatible_icons) \
	$(additional_icons)
else
icon_DATA = \
	$(icon_naming_spec_compatible_icons) \
	$(gtk_compatible_icons) \
	$(kde_compatible_icons)
	\
	$(additional_icons)
endif

EXTRA_DIST =  $(icon_DATA)
