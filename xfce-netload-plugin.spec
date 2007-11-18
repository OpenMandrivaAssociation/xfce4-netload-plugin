Summary:	Netload plugin for the Xfce panel
Name:		xfce-netload-plugin
Version:	0.4.0
Release:	%mkrel 5
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
Source0:	xfce4-netload-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	perl-XML-Parser
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A netload panel plugin for the Xfce Desktop Environment.

%prep
%setup -qn xfce4-netload-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#rm $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.a

%find_lang xfce4-netload-plugin

%clean
rm -rf %{buildroot}

%files -f xfce4-netload-plugin.lang
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*
