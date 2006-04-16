dnl $Id$
dnl
dnl Copyright (c) 2004-2006
dnl         The Xfce development team. All rights reserved.
dnl
dnl Written for Xfce by François Le Clainche  <fleclainche@wanadoo.fr>.
dnl

dnl Version information
m4_define([xit_version_major], [4])
m4_define([xit_version_minor], [3])
m4_define([xit_version_micro], [90])
m4_define([xit_version_nano], [1])
m4_define([xit_version], [xit_version_major().xit_version_minor().xit_version_micro().xit_version_nano()])


dnl # DO NOT MODIFY ANYTHING BELOW THIS LINE, UNLESS YOU KNOW WHAT
dnl # YOU ARE DOING.


dnl Initialize autoconf
AC_COPYRIGHT([Copyright (c) 2004-2006
        The Xfce development team. All rights reserved.

Created for Xfce by François Le Clainche  <fleclainche@wanadoo.fr>.])
AC_INIT([xfce4-icon-theme], [xit_version], [xfce4-dev@xfce.org])
AC_REVISION([$Id$])
AC_PROG_MAKE_SET()

dnl Initialize automake
AM_INIT_AUTOMAKE([AC_PACKAGE_TARNAME()], [AC_PACKAGE_VERSION()])
AM_MAINTAINER_MODE()

dnl Check for required programs
AC_PROG_INSTALL()
AC_PROG_INTLTOOL([0.31], [no-xml])
AC_PROG_LN_S()

dnl I18n support
XDT_I18N([ca de el et fi he hu ja ko pl ru sk zh_CN zh_TW])

dnl Don't install translations
USE_NLS="no"
AC_SUBST([USE_NLS])

AC_OUTPUT([
xfce4-icon-theme.spec
Makefile
mime/Makefile
po/Makefile.in
xfce4-icon-theme-1.0.pc
Rodent/Makefile
Rodent/48x48/Makefile
Rodent/48x48/apps/Makefile
Rodent/48x48/devices/Makefile
Rodent/48x48/filesystems/Makefile
Rodent/48x48/emblems/Makefile
Rodent/48x48/mimetypes/Makefile
Rodent/48x48/misc/Makefile
Rodent/48x48/stock/Makefile
Rodent/scalable/Makefile
Rodent/scalable/apps/Makefile
Rodent/scalable/devices/Makefile
Rodent/scalable/filesystems/Makefile
Rodent/scalable/emblems/Makefile
Rodent/scalable/mimetypes/Makefile
Rodent/scalable/misc/Makefile
Rodent/scalable/stock/Makefile
])

