Summary:	Netload plugin for the Xfce panel
Name:		xfce4-netload-plugin
Version:	0.4.0
Release:	%mkrel 8
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-netload-plugin/%{name}-%{version}.tar.bz2
Patch0:		01_fix-bar-colors.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-netload-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A netload panel plugin for the Xfce Desktop Environment.

%prep
%setup -q
%patch0 -p0

%build
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
