
%define svn	0
%define rel	4
%if %{svn}
%define release		%mkrel 0.%{svn}.%{rel}
%define distname	%{name}-%{svn}
%else
%define release		%mkrel %{rel}
%define distname	%{name}-%{version}
%endif

Summary:	Plee The Bear 2D platform game
Name:		plee-the-bear
Version:	0.3.1
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/%{name}/%{distname}.tar.bz2
Patch0:		plee-the-bear-0.3.1-games.patch
Patch1:		plee-the-bear-0.3.1-gcc43.patch
Patch2:		plee-the-bear-0.3.1-linkage.patch
License:	GPLv2
Group:		Games/Arcade
URL:		http://plee-the-bear.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	libclaw-devel
BuildRequires:	mesagl-devel
BuildRequires:	SDL_mixer-devel
# Dropped temporarily: if it's present, the level editor gets built.
# As of 0.3.1, the level editor dies in a fire during linking with
# a ton of wxGTK undefined references. - AdamW 2008/12
#BuildRequires:	wxGTK2.8-devel

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
%setup -q -n %{distname}
%patch0 -p1 -b .games
%patch1 -p1 -b .gcc43
%patch2 -p0 -b .linkage

%build
%cmake
%make

%install
rm -rf %{buildroot}
pushd build
%makeinstall_std
popd
rm -f %{buildroot}%{_datadir}/menu/plee-the-bear

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_gamesbindir}/%{name}
%{_gamesbindir}/running-bear
%{_libdir}/lib*.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib*.so
%{_gamesdatadir}/%{name}
%{_datadir}/applications/plee-the-bear.desktop
%{_datadir}/icons/hicolor/*/apps/ptb.png
%{_datadir}/pixmaps/ptb.*
