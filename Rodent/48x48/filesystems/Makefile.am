
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
gnome-fs-ftp.png                 network_fs.png\
gnome-fs-home.png                open_folder.png

install-data-local:
	$(mkinstalldirs) $(DESTDIR)$(icondir)
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:blockdevice.png ; \
	  ln -s gnome-fs-blockdev.png mime-inode:blockdevice.png )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:chardevice.png ; \
	  ln -s gnome-fs-blockdev.png mime-inode:chardevice.png )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:directory.png ; \
	  ln -s gnome-fs-directory.png mime-inode:directory.png )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:mount-point.png ; \
	  ln -s gnome-fs-directory.png mime-inode:mount-point.png )
	( cd $(DESTDIR)$(icondir) ; \
	  rm -f mime-inode:core.png ; \
	  ln -s gnome-fs-file-broken.png mime-inode:core.png )
	
EXTRA_DIST =  $(icon_DATA)

