
icondir = $(datadir)/icons/Rodent/scalable/filesystems

icon_DATA = \
gnome-fs-blockdev.svg            gnome-fs-network.svg\
gnome-fs-client.svg              gnome-fs-nfs.svg\
gnome-fs-desktop.svg             gnome-fs-regular.svg\
gnome-fs-directory-accept.svg    gnome-fs-share.svg\
gnome-fs-directory.svg           gnome-fs-smb.svg\
gnome-fs-directory-visiting.svg  gnome-fs-ssh.svg\
gnome-fs-executable.svg          gnome-fs-trash-empty.svg\
gnome-fs-file-broken.svg         gnome-fs-trash-full.svg\
gnome-fs-ftp.svg                 network_fs.svg\
gnome-fs-home.svg                open_folder.svg

install-data-local:
	$(mkinstalldirs) $(DESTDIR)$(icondir)
	( cd $(DESTDIR)$(icondir) ; \
	  ln -sf gnome-fs-blockdev.svg mime-inode:blockdevice.svg ; \
	  ln -sf gnome-fs-blockdev.svg mime-inode:chardevice.svg ; \
	  ln -sf gnome-fs-directory.svg mime-inode:directory.svg ; \
	  ln -sf gnome-fs-directory.svg mime-inode:mount-point.svg ; \
	  ln -sf gnome-fs-file-broken.svg mime-inode:core.svg \
	)

EXTRA_DIST =  $(icon_DATA)

