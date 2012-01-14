Summary:	Plee The Bear 2D platform game
Name:		plee-the-bear
Version:	0.6.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Games/Arcade
URL:		http://plee-the-bear.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}-light.tar.gz
Patch0:		plee-the-bear-0.6.0-svnclawfix.patch
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	libclaw-devel >= 1.7.0
BuildRequires:	mesagl-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	wxgtku-devel
BuildRequires:	docbook-to-man

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
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags}  -DBOOST_FILESYSTEM_VERSION=2"
%cmake -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib} -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%if %{mdvver} <= 201100
%find_lang %{name} %{name} bear-factory bear-engine
%else
%find_lang %{name} bear-factory bear-engine %{name}.lang
%endif

%__rm -f %{buildroot}%{_datadir}/menu/plee-the-bear

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so
%{_datadir}/plee-the-bear
%{_datadir}/bear-factory
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*
%{_mandir}/*/*
