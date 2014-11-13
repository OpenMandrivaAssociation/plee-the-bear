Summary:	Plee The Bear 2D platform game
Name:		plee-the-bear
Version:	0.6.0
Release:	3
License:	GPLv2+
Group:		Games/Arcade
URL:		http://plee-the-bear.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}-light.tar.gz
Source1:	%{name}.rpmlintrc
Patch0:		plee-the-bear-0.6.0-svnclawfix.patch
Patch1:		plee-the-bear-boost-1.50.patch
Patch2:		plee-the-bear-0.6.0-fpermissive.patch
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	libclaw-devel >= 1.7.0
BuildRequires:	pkgconfig(gl)
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
%patch1 -p1
%patch2 -p1

%build
%cmake -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} -DBEAR_FACTORY_INSTALL_LIBRARY_DIR=%{_lib} -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib}
%make

%install
%makeinstall_std -C build

%find_lang %{name} bear-factory bear-engine %{name}.lang

rm -f %{buildroot}%{_datadir}/menu/plee-the-bear

%files -f %{name}.lang
%{_bindir}/*
%{_libdir}/*.so
%{_datadir}/plee-the-bear
%{_datadir}/bear-factory
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*
%{_mandir}/*/*


%changelog
* Sat Jan 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.6.0-1
+ Revision: 760787
- New version 0.6.0, build against utf8 wxGTK2.8

* Wed Mar 16 2011 Funda Wang <fwang@mandriva.org> 0.5.1-1
+ Revision: 645493
- update file list
- new version 0.5.1
- rebuild for new boost

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 0.4.1-5mdv2011.0
+ Revision: 572542
- rebuild for new boost

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 0.4.1-4mdv2011.0
+ Revision: 566035
- rebuild for new boost

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0.4.1-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.4.1-2mdv2010.1
+ Revision: 500329
- rebuild for new boost

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2010.1
+ Revision: 492201
- add lang files
- rework linkage patch

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 0.4.1
    - spec file clean

* Mon Apr 20 2009 Funda Wang <fwang@mandriva.org> 0.3.1-7mdv2009.1
+ Revision: 368306
- refresh tarball

* Thu Mar 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-6mdv2009.1
+ Revision: 361490
- rebuild

* Thu Mar 26 2009 Funda Wang <fwang@mandriva.org> 0.3.1-5mdv2009.1
+ Revision: 361280
- rebuild

* Sun Dec 21 2008 Funda Wang <fwang@mandriva.org> 0.3.1-4mdv2009.1
+ Revision: 317043
- fix linkage and libs

* Sun Dec 14 2008 Adam Williamson <awilliamson@mandriva.org> 0.3.1-2mdv2009.1
+ Revision: 314032
- rebuild (this build doesn't work - crashes when you try to actually get
  into the tutorial - but the current one is uninstallable. this one wins!)
- use %%cmake macro
- temporarily disable the wxgtk dep so the level editor doesn't get built
  (it breaks the build)
- add gcc43.patch (fix build with gcc 4.3)
- rediff games.patch
- clean the spec a bit

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 0.3.1

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jan 14 2008 Olivier Blin <blino@mandriva.org> 0.1.1-1mdv2008.1
+ Revision: 151313
- remove debian-style menu
- package desktop file and icons
- 0.1.1
- split and fix patch installing in games directories
- fix libdir in x86_64 and install in games dir
- add ldconfig calls
- initial import
- create plee-the-bear

