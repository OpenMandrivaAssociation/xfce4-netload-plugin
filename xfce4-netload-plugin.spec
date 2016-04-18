%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	Netload plugin for the Xfce panel
Name:		xfce4-netload-plugin
Version:	1.2.4
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-netload-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.7
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4ui-1)
Obsoletes:	xfce-netload-plugin

%description
A netload panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%define Werror_cflags %nil

%configure
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libnetload.so
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.*g
