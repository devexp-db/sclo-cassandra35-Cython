%if 0%{?fedora}
%global with_python3 1
%endif

%global srcname Cython

%bcond_without check

Name:		Cython
Version:	0.23.4
##Release:	4.b3%{?dist}
Release:	3%{?dist}
Summary:	A language for writing Python extension modules

%global upstreamversion %{version}
##%%global upstreamversion %{version}b3

Group:		Development/Tools
License:	Python
URL:		http://www.cython.org
Source:		http://www.cython.org/release/%{srcname}-%{upstreamversion}.tar.gz
Patch0:	gcc6.patch
Patch1: gcc6.2.patch
BuildRequires:	python-devel python-setuptools
%if 0%{?with_python3}
BuildRequires:	python3-devel
%endif # if with_python3

%if %{with check}
BuildRequires:	libtool
BuildRequires:	numpy
# Coverage tests fail
#BuildRequires:	python-coverage
%endif

Provides:	python2-%{srcname} = %{version}-%{release}

%description
This is a development version of Pyrex, a language
for writing Python extension modules.

For more info, see:

    Doc/About.html for a description of the language
    INSTALL.txt	   for installation instructions
    USAGE.txt	   for usage instructions
    Demos	   for usage examples

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:	A language for writing Python extension modules
Group:		Development/Tools
%if %{with check}
# Coverage tests fail
#BuildRequires:	python3-coverage
BuildRequires:	python3-numpy
%endif

%description -n python3-%{srcname}
This is a development version of Pyrex, a language
for writing Python extension modules.

For more info, see:

    Doc/About.html for a description of the language
    INSTALL.txt	   for installation instructions
    USAGE.txt	   for usage instructions
    Demos	   for usage examples
%endif # with_python3

%prep
%setup -q -n %{name}-%{upstreamversion}
%patch0 -p1
%patch1 -p1

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif # with_python3


%install
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
%py3_install
mv $RPM_BUILD_ROOT/usr/bin/cython $RPM_BUILD_ROOT/usr/bin/cython3
mv $RPM_BUILD_ROOT/usr/bin/cythonize $RPM_BUILD_ROOT/usr/bin/cythonize3
mv $RPM_BUILD_ROOT/usr/bin/cygdb $RPM_BUILD_ROOT/usr/bin/cygdb3
rm -rf %{buildroot}%{python3_sitelib}/setuptools/tests
%endif

%py2_install
rm -rf %{buildroot}%{python_sitelib}/setuptools/tests


%if %{with check}
%check
%{__python} runtests.py -vv ##|| gcc -pthread -fno-strict-aliasing -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DNDEBUG -O2 -g -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -I/builddir/build/BUILD/Cython-0.23.4/tests/run -I/usr/include/python2.7 -c $$(find . -name complex_numbers_c89_T398.cpp) -o /builddir/build/BUILD/Cython-0.23.4/BUILD/run/cpp/complex_numbers_c89_T398/complex_numbers_c89_T398.o -DCYTHON_REFNANNY=1

%if 0%{?with_python3}
# asyncio test fails
%{__python3} runtests.py -vv || :
%endif # with_python3
%endif


%files
%{!?_licensedir:%global license %doc}
%license LICENSE.txt
%doc *.txt Demos Doc Tools
%{_bindir}/cython
%{_bindir}/cygdb
%{_bindir}/cythonize
%{python_sitearch}/%{srcname}
%{python_sitearch}/cython.py*
%{python_sitearch}/pyximport
%{python_sitearch}/%{srcname}*egg-info

%if 0%{?with_python3}
%files -n python3-%{srcname}
%license LICENSE.txt
%doc *.txt Demos Doc Tools
%{python3_sitearch}/*
%{_bindir}/cython3
%{_bindir}/cythonize3
%{_bindir}/cygdb3
%endif # with_python3


%changelog
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Orion Poplawski <orion@cora.nwra.com> - 0.23.4-1
- Update to 0.23.4
- Ship cythonize3
- Modernize and cleanup spec
- Run tests, one python3 test fails with 3.5

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 0.23-2
- Rebuilt for Python3.5 rebuild

* Wed Aug 12 2015 Neal Becker <ndbecker2@gmail.com> - 0.23-2
- Update to 0.23

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 nbecker <ndbecker2@gmail.com> - 0.22-1
- oops, that should be 0.22 not 0.22.1

* Fri Feb 13 2015 nbecker <ndbecker2@gmail.com> - 0.22.1-1
- Update to 0.22

* Sat Nov 22 2014 nbecker <ndbecker2@gmail.com> - 0.21.1-1
- Update to 0.21.1 (br #1164297)

* Mon Sep 15 2014 nbecker <ndbecker2@gmail.com> - 0.21-5
- Add /bin/cythonize

* Mon Sep 15 2014 nbecker <ndbecker2@gmail.com> - 0.21-1
- Update to 0.21

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Thomas Spura <tomspur@fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 0.20.1-2
- Rebuild for Python 3.4

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 0.20.1-1
- Update to 0.20.1

* Mon Jan 20 2014 nbecker <ndbecker2@gmail.com> - 0.20-1
- Update to 0.20

* Thu Oct 17 2013 nbecker <ndbecker2@gmail.com> - 0.19.2-2
- Fix BR 1019498

* Sun Oct 13 2013 nbecker <ndbecker2@gmail.com> - 0.19-2
- Update to 0.19.2

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 nbecker <ndbecker2@gmail.com> - 0.19-1
- Update to 0.19

* Tue Jan 29 2013 Neal Becker <ndbecker2@gmail.com> - 0.18-1
- update to 0.18

* Sat Dec 15 2012 Neal Becker <ndbecker2@gmail.com> - 0.17.3-1
- Update to 0.17.3

* Wed Nov 21 2012 Neal Becker <ndbecker2@gmail.com> - 0.17.2-1
- update to 0.17.2

* Wed Sep 26 2012 Neal Becker <ndbecker2@gmail.com> - 0.17.1-1
- Update to 0.17.1

* Mon Sep  3 2012 Neal Becker <ndbecker2@gmail.com> - 0.17-1
- Update to 0.17

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

