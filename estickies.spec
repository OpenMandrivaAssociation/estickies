%define	name	estickies
%define	version 0.0.1
%define release %mkrel 10

Summary: 	E17 Sticky notes application
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Toys
URL: 		https://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	ecore-devel >= 0.9.9.050, etk-devel >= 0.1.0.042
Buildrequires:	edje-devel >= 0.9.9.050, edje >= 0.9.9.050
Buildrequires:	embryo-devel >= 0.9.9.050, embryo >= 0.9.9.050
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils


%description
Estickies is a sticky notes application that uses Etk.
uses Etk's runtime theming support to change the look
and feel of the windows and buttons.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
# fix libtool issue on release < 2009.1
%if %mdkversion < 200910
perl -pi -e "s/^ECHO.*/ECHO='echo'\necho='echo'\n/" libtool
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if %mdkversion < 200900
%post 
%{update_menus} 
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
