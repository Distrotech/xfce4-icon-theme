Summary: 	Icons for xfce
Name: 		xfce4-icon-theme
Version: 	4.1.0
Release: 	1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	%{name}-%{version}.tar.gz
Group: 		Themes
BuildRoot: 	%{_tmppath}/%{name}-root
Requires:	xfce4-icon-theme

%description
Icon theme for XFce 4 DEsktop Environment.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README ChangeLog NEWS INSTALL COPYING AUTHORS
%{_datadir}/xfce4/xfce4-icon-theme/


