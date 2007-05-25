%define	name	estickies
%define	version	0.0.1
%define release %mkrel 1

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
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	ecore-devel >= 0.9.9.038, etk-devel >= 0.1.0.003


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

mkdir -p $RPM_BUILD_ROOT%{_menudir}

cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):\
        needs="X11" \
        section="Toys" \
        title="%name" \
        longtitle="Estickies is a sticky notes application" \
        command="%{_bindir}/%name" \
        icon="%name.png" \
        startup_notify="true" \
        xdg="true"
EOF

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/images/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/images/%name.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 data/images/%name.png %buildroot%_miconsdir/%name.png

mkdir -p %buildroot%{_datadir}/pixmaps
cp data/images/%name.png %buildroot%{_datadir}/pixmaps/%name.png

%post 
%{update_menus} 

%postun 
%{clean_menus} 


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/%name
%{_menudir}/*
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
