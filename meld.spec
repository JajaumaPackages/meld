Name:		meld
Version:	1.1.5
Release:	5%{?dist}
Summary:	Visual diff and merge tool

Group:		Development/Tools
License:	GPLv2+
URL:		http://meld.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/gnome/sources/meld/1.1/meld-%{version}.tar.bz2
Patch0:		desktop.patch
Patch1:		%{name}-scrollkeeper.patch
Patch2:		%{name}-%{version}-git.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	scrollkeeper
BuildRequires:	perl(XML::Parser)

Requires:	gnome-python2 >= 2.6.0
Requires:	gnome-python2-canvas
Requires:	gnome-python2-gconf
Requires:	gnome-python2-gtksourceview
Requires:	pygtk2 >= 2.6.0
Requires:	pygtk2-libglade

Requires(post):	scrollkeeper
Requires(postun): scrollkeeper

BuildArch:	noarch

%description
Meld is a GNOME 2 visual diff and merge tool. It integrates especially well
with CVS. The diff viewer lets you edit files in place (diffs update
dynamically), and a middle column shows detailed changes and allows merges. The
margins show location of changes for easy navigation, and it also features a
tabbed interface that allows you to open many diffs at once.


%prep
%setup -q
%patch0 -p1 -b .desktop
%patch1 -p1 -b .scrollkeeper
%patch2 -p1 -b .git


%build
make prefix=%{_prefix} libdir=%{_datadir}


%install
rm -rf ${RPM_BUILD_ROOT}

make prefix=%{_prefix} libdir=%{_datadir} \
  DESTDIR=${RPM_BUILD_ROOT} install


desktop-file-install --vendor fedora                    \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications       \
  --delete-original                                     \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :


%postun
scrollkeeper-update -q || :


%clean
rm -rf ${RPM_BUILD_ROOT}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/*.pyc
%{_datadir}/%{name}/*.pyo
%dir %{_datadir}/%{name}/vc
%{_datadir}/%{name}/vc/*.py
%{_datadir}/%{name}/vc/*.pyc
%{_datadir}/%{name}/vc/*.pyo
%{_datadir}/%{name}/glade2/
%{_datadir}/applications/fedora-%{name}.desktop
%{_datadir}/application-registry/%{name}*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/


%changelog
* Tue Jun  3 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-5
- Backport git support (#449250).

* Wed Nov 14 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-4
- Add Requires on gnome-python2-gtksourceview to enable syntax coloring. (#382041)

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-3
- Update license tag.

* Sun Jun 10 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-2
- Drop requires on yelp.

* Sat Jun  9 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5.
- Drop gettext patch.  fixed upstream.

* Sat Jun  9 2007 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-7
- Add requires on yelp.

* Sat Dec  9 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-6
- Drop X-Fedora category from desktop file.
- Add patch to fix rejects from new version of gettext.

* Fri Dec  8 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-5
- Rebuild against new python.

* Wed Sep  6 2006 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-4
- Don't ghost *.pyo files.
- Add BR for intltool and perl(XML::Parser).
- Rebuild for FC6.

* Sun Jun 11 2006 Brian Pepple <bdpepple@ameritech.net> - 1.1.4-3
- Update to 1.1.4.

* Thu Feb 16 2006 Brian Pepple <bdpepple@ameritech.net> - 1.1.3-4
- Remove unnecessary BR (intltool).

* Mon Feb 13 2006 Brian Pepple <bdpepple@ameritech.net> - 1.1.3-3
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb  5 2006 Brian Pepple <bdpepple@ameritech.net> - 1.1.3-2
- Update to 1.1.3.
- Update scrollkeeper scriptlet.
- Update versions required for pygtk2 & gnome-python2.
- Add patch to disable scrollkeeper in Makefile.
- Ghost the *.pyo.

* Sun Nov 13 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.1.2-1
- Update to 1.1.2.

* Mon Jul 25 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.0-1
- Update to 1.0.0.
- Include fix for upstream bug #309408.

* Wed Jun  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.6-1
- Remove unused meld shell script from src.rpm.
- Add scriptlets for scrollkeeper-update.
- Use %%find_lang macro.
- Simplify %%install (let included Makefile do the installation).
- Update to 0.9.6 (fixes manual).
- BR scrollkeeper (#156235).

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.9.5-2
- rebuilt

* Sun Feb 06 2005 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.9.5-1
- 0.9.5.

* Thu Nov 11 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.9.4.1-0.fdr.3
- Clean up spec/Bump release.

* Sat Jul 31 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.4.1-0.fdr.2
- Group now Development/Tools.

* Wed Jul 21 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.4.1-0.fdr.1
- Updated to 0.9.4.1.

* Fri May 28 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.3-0.fdr.1
- Updated to 0.9.3.

* Wed Apr 07 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.2.1-0.fdr.2
- BuildReqs intltool & gettext (#1459).

* Tue Apr 06 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.2.1-0.fdr.1
- Updated to 0.9.2.1.

* Thu Dec 04 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.1-0.fdr.2
- Include translations.

* Sat Nov 22 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.1-0.fdr.1
- Updated to 0.9.1.

* Thu Oct 23 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.0-0.fdr.2
- Reuire pygtk2 >= 0:1.99.15.

* Sun Oct 12 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.9.0-0.fdr.1
- Updated to 0.9.0.

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
