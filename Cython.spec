%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}


Name:		Cython
Version:	0.17
Release:	4.b3%{?dist}
##Release:	3%{?dist}
Summary:	A language for writing Python extension modules

##%%define upstreamversion %{version}
%define upstreamversion %{version}b3

Group:		Development/Tools
License:	Python
URL:		http://www.cython.org
Source:		http://www.cython.org/Cython-%{upstreamversion}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python-devel python-setuptools
BuildRequries:  numpy		# only for check!
Requires:	python

%description
This is a development version of Pyrex, a language
for writing Python extension modules.

For more info, see:

    Doc/About.html for a description of the language
    INSTALL.txt	   for installation instructions
    USAGE.txt	   for usage instructions
    Demos	   for usage examples


%prep
%setup -q -n %{name}-%{upstreamversion}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%check
%{__python} runtests.py -x numpy

%files
%defattr(-,root,root,-)
%{_bindir}/cython
%{_bindir}/cygdb
%{python_sitearch}/Cython
%{python_sitearch}/cython.py*
%{python_sitearch}/pyximport
%if 0%{?fedora} >= 9 || 0%{?rhel} >= 6
%{python_sitearch}/Cython*egg-info
%endif
%doc *.txt Demos Doc Tools


%changelog
* Tue Aug 28 2012 Neal Becker <ndbecker2@gmail.com> - 0.17-3.b3
- Turn on check (temporarily)
- Add br numpy from check

* Tue Aug 28 2012 Neal Becker <ndbecker2@gmail.com> - 0.17-1.b3
- Test 0.17b3

* Fri Aug 24 2012 David Malcolm <dmalcolm@redhat.com> - 0.16-3
- generalize egg-info logic to support RHEL (rhbz#851528)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Neal Becker <ndbecker2@gmail.com> - 0.16-1
- Update to 0.16

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Neal Becker <ndbecker2@gmail.com> - 0.15.1-1
- Update to 0.15.1

* Sat Aug  6 2011 Neal Becker <ndbecker2@gmail.com> - 0.15-1
- Update to 0.15

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb  5 2011 Neal Becker <ndbecker2@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Wed Dec 15 2010 Neal Becker <ndbecker2@gmail.com> - 0.14-2
- Add cygdb

* Wed Dec 15 2010 Neal Becker <ndbecker2@gmail.com> - 0.14-1
- Update to 0.14

* Wed Aug 25 2010 Neal Becker <ndbecker2@gmail.com> - 0.13-1
- Update to 0.13

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Feb  5 2010 Neal Becker <ndbecker2@gmail.com> - 0.12.1-4
- Disable check for now as it fails on PPC

* Tue Feb  2 2010 Neal Becker <ndbecker2@gmail.com> - 0.12.1-2
- typo
- stupid rpm comments

* Mon Nov 23 2009 Neal Becker <ndbecker2@gmail.com> - 0.12-1.rc1
- Make that 0.12

* Mon Nov 23 2009 Neal Becker <ndbecker2@gmail.com> - 0.12.1-1.rc1
- Update to 0.12.1

* Sun Sep 27 2009 Neal Becker <ndbecker2@gmail.com> - 0.11.3-1.rc1
- Update to 0.11.3rc1
- Update to 0.11.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Neal Becker <ndbecker2@gmail.com> - 0.11.2-1
- Update to 0.11.2

* Thu Apr 16 2009 Neal Becker <ndbecker2@gmail.com> - 0.11.1-1
- Update to 0.11.1

* Sat Mar 14 2009 Neal Becker <ndbecker2@gmail.com> - 0.11-2
- Missed cython.py*

* Sat Mar 14 2009 Neal Becker <ndbecker2@gmail.com> - 0.11-1
- Update to 0.11
- Exclude numpy from tests so we don't have to BR it

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Neal Becker <ndbecker2@gmail.com> - 0.10.3-1
- Update to 0.10.3

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10.2-2
- Rebuild for Python 2.6

* Mon Dec  1 2008 Neal Becker <ndbecker2@gmail.com> - 0.10.2-1
- Update to 0.10.2

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10.1-2
- Rebuild for Python 2.6

* Wed Nov 19 2008 Neal Becker <ndbecker2@gmail.com> - 0.10.1-1
- Update to 0.10.1

* Sun Nov  9 2008 Neal Becker <ndbecker2@gmail.com> - 0.10-3
- Fix typo

* Sun Nov  9 2008 Neal Becker <ndbecker2@gmail.com> - 0.10-1
- Update to 0.10

* Fri Jun 13 2008 Neal Becker <ndbecker2@gmail.com> - 0.9.8-2
- Install into python_sitearch
- Add %%check

* Fri Jun 13 2008 Neal Becker <ndbecker2@gmail.com> - 0.9.8-1
- Update to 0.9.8

* Mon Apr 14 2008 José Matos <jamatos[AT]fc.up.pt> - 0.9.6.13.1-3
- Remove remaining --record.
- Add more documentation (Doc and Tools).
- Add correct entry for egg-info (F9+).

* Mon Apr 14 2008 Neal Becker <ndbecker2@gmail.com> - 0.9.6.13.1-2
- Change License to Python
- Install About.html
- Fix mixed spaces/tabs
- Don't use --record

* Tue Apr  8 2008 Neal Becker <ndbecker2@gmail.com> - 0.9.6.13.1-1
- Update to 0.9.6.13.1

* Mon Apr  7 2008 Neal Becker <ndbecker2@gmail.com> - 0.9.6.13-1
- Update to 0.9.6.13
- Add docs

* Tue Feb 26 2008 Neal Becker <ndbecker2@gmail.com> - 0.9.6.12-1
- Initial version

