# $Id$
# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Small and fast GUI web browser
Name: dillo
Version: 0.8.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.dillo.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.dillo.org/download/dillo-%{version}.tar.bz2
Source1: dillo48.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, zlib-devel, libjpeg-devel
Provides: webclient

%description
Dillo is a very small and fast web browser using GTK.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Dillo Web Browser
Comment=Browse the Internet
Exec=dillo
Icon=dillo.png
Terminal=false
Type=Application
Categories=Network;Application;
EOF

%build
%configure \
	--enable-cookies \
	--enable-ipv6
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/dillo.png

### Remove buildroot from config files
%{__perl} -pi -e 's|%{buildroot}||g' %{buildroot}%{_sysconfdir}/*

%if %{dfi}
        %{__install} -D -m0644 dillo.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/dillo.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		dillo.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README doc/
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/dillo/
%{_datadir}/pixmaps/*.png
%if %{dfi}
	%{_datadir}/gnome/apps/Internet/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Wed Feb 11 2004 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Remove %%{buildroot} occurances in configuration files. (Andre Costa)

* Tue Feb 10 2004 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 0.7.3-0
- Initial package. (using DAR)
