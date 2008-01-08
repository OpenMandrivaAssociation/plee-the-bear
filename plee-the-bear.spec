%define name plee-the-bear
%define version 0
%define svn 20080102
%define rel 1
%define release %mkrel 0.%{svn}.%{rel}
%define distname %{name}-%{svn}

Summary: Plee The Bear 2D platform game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/%{name}/%{distname}.tar.bz2
Patch0:	 plee-the-bear-20080102-default.patch
License: GPL
Group: Games/Arcade
Url: http://plee-the-bear.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: boost-devel cmake libclaw-devel mesagl-devel
BuildRequires: SDL_mixer-devel wxGTK-devel

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
%setup -q -n %{name}-%{svn}
%patch0 -p1 -b .default

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/ptb
%{_libdir}/lib*.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib*.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/game_description
%{_datadir}/%{name}/*.ra
