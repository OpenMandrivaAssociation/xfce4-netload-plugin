%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Netload plugin for the Xfce panel
Name:		xfce4-netload-plugin
Version:	1.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-netload-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.7
BuildRequires:	xfce4-panel-devel >= 4.7
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4ui-1)
Obsoletes:	xfce-netload-plugin

%description
A netload panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%define Werror_cflags %nil

%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.*g


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.1.0-2
+ Revision: 791570
- Rebuild

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-1
+ Revision: 789875
- update to new version 1.1.0
- drop old stuff from spec file

* Sun Dec 12 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 620599
- update to new version 1.0.0
- update buildrequires
- update URL for Source0
- update file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-11mdv2010.1
+ Revision: 543432
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.4.0-10mdv2010.0
+ Revision: 446105
- rebuild

* Sun Mar 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-9mdv2009.1
+ Revision: 360424
- disable checks for format-strings
- use _disable_ld_as_needed to make it build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-7mdv2009.0
+ Revision: 194670
- Patch0: fix wrong bar colors on some gtk themes

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-6mdv2008.1
+ Revision: 110126
- correct buildrequires
- do not package COPYING file
- new license policy
- use upstream tarball name as a real name
- use upstream name

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-5mdv2008.0
+ Revision: 33233
- spec file clean
- update url

