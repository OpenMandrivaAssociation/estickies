%define	name	estickies
%define	version 0.0.1
%define release %mkrel 5

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	E17 Sticky notes application
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Toys
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	ecore-devel >= 0.9.9.050, etk-devel >= 0.1.0.042
Buildrequires:	edje-devel >= 0.5.0.050, edje >= 0.5.0.050
Buildrequires:	embryo-devel >= 0.9.9.050, embryo >= 0.9.9.050
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils


%description
Estickies is a sticky notes application that uses Etk.
uses Etk's runtime theming support to change the look
and feel of the windows and buttons.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall



mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cp -vf %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Graphics" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop


mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/images/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/images/%name.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 data/images/%name.png %buildroot%_miconsdir/%name.png

mkdir -p %buildroot%{_datadir}/pixmaps
cp data/images/%name.png %buildroot%{_datadir}/pixmaps/%name.png

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
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
%{_datadir}/applications/*
