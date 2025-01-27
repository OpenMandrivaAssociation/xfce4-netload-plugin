%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	Netload plugin for the Xfce panel
Name:		xfce4-netload-plugin
Version:	1.4.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-netload-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4ui-2)
Obsoletes:	xfce-netload-plugin

%description
A netload panel plugin for the Xfce Desktop Environment.

%prep
%autosetup -p1

%build
%define Werror_cflags %nil

%configure
%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README* ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libnetload.so
%{_datadir}/xfce4/panel/plugins/netload.desktop
%{_iconsdir}/hicolor/*/apps/*.*g
