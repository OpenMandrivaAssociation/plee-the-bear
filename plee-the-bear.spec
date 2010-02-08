Summary:	Plee The Bear 2D platform game
Name:		plee-the-bear
Version:	0.4.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Games/Arcade
URL:		http://plee-the-bear.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch2:		plee-the-bear-0.4.1-linkage.patch
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	libclaw-devel
BuildRequires:	mesagl-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	wxGTK2.8-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Plee The Bear is a 2D platform game like those we found on consoles in
the beginning of the 90's. The basis of the scenario fit in few lines:

4 PM or so, Plee wakes up, tired. He has dreamed again about that
awesome period when he went across the entire world together with his
belle. He puts his leg in the honey pot... empty! Moreover every
single honey pot in the house is empty. "One more trick of that kid",
he thinks. "I'm going to give him such a wallop of which hesure will
remember".

Following honey drops on the ground, Plee reaches the edge of the
forest. Beginning of the game.

%prep
%setup -q -n %{name}-%{version}
%patch2 -p0 -b .linkage

%build
%cmake -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%_lib -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%_lib -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%_lib
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %name %name bear-factory

rm -f %{buildroot}%{_datadir}/menu/plee-the-bear

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so
%{_datadir}/plee-the-bear
%{_datadir}/bear-factory
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*
