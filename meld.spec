Summary:          Visual diff and merge tool.
Name:             meld
Version:          0.8.5
Release:          0.fdr.1.rh90
Epoch:            0
URL:              http://meld.sourceforge.net/
License:          GPL
Group:            Applications/Editors  
Source0:          http://download.sf.net/sourceforge/meld/meld-0.8.5.tgz
Source1:          meld.desktop
Source2:          meld
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         pygtk2 >= 0:1.99.14
Requires:         gnome-python2 >= 0:1.99.14
Requires:         pygtk2-libglade
Requires:         gnome-python2-canvas
Requires:         gnome-python2-gconf
BuildRequires:    desktop-file-utils
BuildArch:        noarch

%description
Meld is a GNOME 2 visual diff and merge tool. It integrates especially well
with CVS. The diff viewer lets you edit files in place (diffs update
dynamically), and a middle column shows detailed changes and allows merges. The
margins show location of changes for easy navigation, and it also features a
tabbed interface that allows you to open many diffs at once.



%prep
%setup -q



%build



%install
rm -rf ${RPM_BUILD_ROOT}

install -d -m0755 ${RPM_BUILD_ROOT}%{_datadir}/meld/glade2/pixmaps/

install -p -D -m0755 meld ${RPM_BUILD_ROOT}%{_datadir}/meld/meld
install -p -D -m0644 *.py ${RPM_BUILD_ROOT}%{_datadir}/meld/
install -p -D -m0644 glade2/*.glade ${RPM_BUILD_ROOT}%{_datadir}/meld/glade2/
install -p -D -m0644 glade2/*.strings ${RPM_BUILD_ROOT}%{_datadir}/meld/glade2/
install -p -D -m0644 glade2/pixmaps/* ${RPM_BUILD_ROOT}%{_datadir}/meld/glade2/pixmaps/
install -p -D -m0644 glade2/pixmaps/icon.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/meld.png
install -p -D -m0644 manual/index.html ${RPM_BUILD_ROOT}%{_datadir}/meld/manual/index.html
install -p -D -m0644 manual/stylesheet.css ${RPM_BUILD_ROOT}%{_datadir}/meld/manual/stylesheet.css

install -p -D -m0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_datadir}/applications/meld.desktop
install -p -D -m0755 %{SOURCE2} ${RPM_BUILD_ROOT}%{_bindir}/meld

desktop-file-install --vendor fedora --delete-original  \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications       \
  --add-category X-Fedora                               \
  --add-category Application                            \
  --add-category Utility                                \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop



%clean
rm -rf ${RPM_BUILD_ROOT}



%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING TODO.txt
%{_bindir}/meld
%{_datadir}/meld
%{_datadir}/applications/fedora-meld.desktop
%{_datadir}/pixmaps/meld.png



%changelog
* Mon Sep 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.5-0.fdr.1
- Updated to 0.8.5.

* Wed Aug 13 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.4-0.fdr.3
- dropped tidyxml.py.

* Mon Aug 11 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.4-0.fdr.2
- Moved manual so the help feature will work.

* Thu Jul 31 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.4-0.fdr.1
- Updated to 0.8.4.
- now install files under %%{_datadir} rather than %%{_libdir}.

* Wed May 28 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.1-0.fdr.3
- Package now contains verifiable source.

* Tue May 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.1-0.fdr.2
- Cleaned out libdir/meld.
- fixed file permissions.

* Sun May 25 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.8.1-0.fdr.1
- Updated to 0.8.1.
- buildroot -> RPM_BUILD_ROOT.

* Wed Apr 16 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.7.1-0.fdr.1
- Updated to 0.7.1.

* Wed Apr 09 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.7.0-0.fdr.3
- Updated Requires.

* Tue Apr 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.7.0-0.fdr.2
- Changed category to X-Fedora-Extra.
- Added desktop-file-utils to BuildRequires.
- Added missing Requires fields.
- Added Epoch:0.

* Thu Mar 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.7.0-0.fdr.1
- Initial RPM release.
