
icondir = $(datadir)/icons/Rodent/48x48/filesystems

icon_DATA = \
gnome-fs-blockdev.png            gnome-fs-network.png\
gnome-fs-client.png              gnome-fs-nfs.png\
gnome-fs-desktop.png             gnome-fs-regular.png\
gnome-fs-directory-accept.png    gnome-fs-share.png\
gnome-fs-directory.png           gnome-fs-smb.png\
gnome-fs-directory-visiting.png  gnome-fs-ssh.png\
gnome-fs-executable.png          gnome-fs-trash-empty.png\
gnome-fs-file-broken.png         gnome-fs-trash-full.png\
blockdevice.png 	 	 chardevice.png\
core.png			 directory.png\
mount-point.png	 		 gnome-fs-ftp.png\
network_fs.png			 gnome-fs-home.png\
open_folder.png

install-data-local:
	$(mkinstalldirs) $(DESTDIR)$(icondir)
if !HAVE_CYGWIN
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:blockdevice.png ; \
	  $(LN_S) blockdevice.png mime-inode:blockdevice.png )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:chardevice.png ; \
	  $(LN_S) chardevice.png mime-inode:chardevice.png )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:directory.png ; \
	  $(LN_S) directory.png mime-inode:directory.png )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:mount-point.png ; \
	  $(LN_S) mount-point.png mime-inode:mount-point.png )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:core.png ; \
	  $(LN_S) core.png mime-inode:core.png )
endif
	
EXTRA_DIST =  $(icon_DATA)

