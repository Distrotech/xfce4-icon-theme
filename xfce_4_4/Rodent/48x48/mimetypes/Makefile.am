
icondir = $(datadir)/icons/Rodent/48x48/mimetypes

icon_DATA = \
application-msword.png                    application-x-kpresenter.png        image-x-psd.png\
application-octet-stream.png              application-x-kspread.png           image-x-rgb.png\
application-ogg.png                       application-x-kword.png             image-x-tga.png\
application-pdf.png                       application-x-lha.png               image-x-xbitmap.png\
application-pgp-encrypted.png             application-x-object.png            image-x-xcf.png\
application-pgp-keys.png                  application-x-perl.png              image-x-xfig.png\
application-pgp.png                       application-x-php.png               image-x-xpixmap.png\
application.png                           application-x-python-bytecode.png   image-x-xwindowdum.png\
application-postscript.png                application-x-python.png            text-css.png\
application-qif.png                       application-x-qw.png                text-html.png\
application-rhythmbox-effect.png          application-x-rar.png               text.png\
application-rhythmbox-playlist.png        application-x-reject.png            text-sgml.png\
application-rtf.png                       application-x-rpm.png               text-x-authors.png\
application-smil.png                      application-x-sharedlib.png         text-x-chdr.png\
application-vnd.ms-excel.png              application-x-share-library-la.png  text-x-c-header.png\
application-vnd.ms-powerpoint.png         application-x-shellscript.png       text-x-copying.png\
application-vnd.ms-word.png               application-x-shockwave-flash.png   text-x-c.png\
application-vnd.rn-realmedia.png          application-x-smil.png              text-x-c++.png\
application-vnd.stardivision.calc.png     application-x-tar.png               text-x-credits.png\
application-vnd.stardivision.chart.png    application-x-tex.png               text-x-csharp.png\
application-vnd.stardivision.impress.png  application-x-trash.png             text-x-csh.png\
application-vnd.stardivision.writer.png   application-zip.png                 text-x-c++src.png\
application-vnd.sun.xml.calc.png          audio-ac3.png                       text-x-csrc.png\
application-vnd.sun.xml.chart.png         audio-basic.png                     text-x-gettext-translation.png\
application-vnd.sun.xml.draw.png          audio-midi.png                      text-x-haskell.png\
application-vnd.sun.xml.impress.png       audio.png                           text-x-install.png\
application-vnd.sun.xml.writer.png        audio-x-aiff.png                    text-x-java.png\
application-x-abiword.png                 audio-x-it.png                      text-x-literate-haskell.png\
application-x-archive.png                 audio-x-midi.png                    text-x-log.png\
application-x-arj.png                     audio-x-mod.png                     text-x-lyx.png\
application-x-blender.png                 audio-x-mp3.png                     text-x-makefile.png\
application-x-bzip-compressed-tar.png     audio-x-mpegurl.png                 text-xml.png\
application-x-bzip.png                    audio-x-pn-realaudio.png            text-x-patch.png\
application-x-cd-image.png                audio-x-s3m.png                     text-x-readme.png\
application-x-compressed-tar.png          audio-x-stm.png                     text-x-scheme.png\
application-x-compress.png                audio-x-ulaw.png                    text-x-sh.png\
application-x-cpio-compressed.png         audio-x-voc.png                     text-x-tex.png\
application-x-cpio.png                    audio-x-wav.png                     text-x-troff-man.png\
application-x-deb.png                     audio-x-xi.png                      text-x-vcalendar.png\
application-x-desktop.png                 audio-x-xm.png                      text-x-vcard.png\
application-x-dia-diagram.png             image-bmp.png                       text-x-xslt.png\
application-x-dvi.png                     image-gif.png                       text-x-zsh.png\
application-x-executable.png              image-ief.png                       video-mpeg.png\
application-x-font-asm.png                image-jpeg.png                      video.png\
application-x-font-bdf.png                image.png                           video-quicktime.png\
application-x-font-linux-psf.png          image-png.png                       video-x-ms-asf.png\
application-x-font-pcf.png                image-svg.png                       video-x-msvideo.png\
application-x-font-ttf.png                image-svg+xml.png                   video-x-ms-wmv.png\
application-x-gettext-translation.png     image-tiff.png                      x-directory-nfs-server.png\
application-x-glade.png                   image-x-3ds.png                     x-directory-smb-server.png\
application-x-gnucash.png                 image-x-applix-graphic.png          x-directory-smb-share.png\
application-x-gnumeric.png                image-x-cmu-raster.png              x-directory-smb-workgroup.png\
application-x-gtktalog.png                image-x-portable-anymap.png         x-font-afm.png\
application-x-gzip.png                    image-x-portable-bitmap.png         x-gdesklets-display.png\
application-x-kde-app-info.png            image-x-portable-greymap.png\
application-x-killustrator.png            image-x-portable-pixmap.png

install-data-local:
	$(mkinstalldirs) $(DESTDIR)$(icondir)
if !HAVE_CYGWIN
	( cd $(DESTDIR)$(icondir) ; \
	  icons="$(icon_DATA)" ; \
	  for file in $$icons; do \
	      rm -f gnome-mime-$$file ; \
	      rm -f `echo mime-$$file | sed -e 's/mime-\([^-]*\)-/mime-\1:/'` ; \
	      $(LN_S) $$file  gnome-mime-$$file ; \
	      $(LN_S) $$file  `echo mime-$$file | sed -e 's/mime-\([^-]*\)-/mime-\1:/'` ; \
	  done \
	)
endif

EXTRA_DIST =  $(icon_DATA)

