%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Netload plugin for the Xfce panel
Name:		xfce4-netload-plugin
Version:	1.0.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-netload-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.7
BuildRequires:	xfce4-panel-devel >= 4.7
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfcegui4-devel
Obsoletes:	xfce-netload-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A netload panel plugin for the Xfce Desktop Environment.

%prep
%setup -q

%build
%define Werror_cflags %nil
#define _disable_ld_as_needed 1

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#rm $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.a

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.*g
