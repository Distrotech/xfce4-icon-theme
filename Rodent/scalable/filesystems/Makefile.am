
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
blockdevice.svg	 		 chardevice.svg\
core.svg		 	 directory.svg\
mount-point.svg	 		 gnome-fs-home.svg\
open_folder.svg

install-data-local:
	$(mkinstalldirs) $(DESTDIR)$(icondir)
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:blockdevice.svg ; \
	  $(LN_S) blockdevice.svg mime-inode:blockdevice.svg )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:chardevice.svg ; \
	  $(LN_S) chardevice.svg mime-inode:chardevice.svg )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:directory.svg ; \
	  $(LN_S) directory.svg mime-inode:directory.svg )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:mount-point.svg ; \
	  $(LN_S) mount-point.svg mime-inode:mount-point.svg )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:core.svg ; \
	  $(LN_S) core.svg mime-inode:core.svg )

EXTRA_DIST =  $(icon_DATA)

