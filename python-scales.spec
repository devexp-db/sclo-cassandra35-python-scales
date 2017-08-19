%if 0%{?rhel}
%bcond_with python3
%else
%bcond_without python3
%endif

%global commit c0602416b6f8c688409f811c51a2962b75e78935

Name:           python-scales
Version:        1.0.5
Release:        11%{?dist}
Summary:        Stats for Python processes

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/Cue/scales
Source0:        https://github.com/Cue/scales/archive/%{commit}/scales-%{commit}.tar.gz

# https://github.com/Cue/scales/pull/25
Patch0:         0001-Fix-syntax-error-on-bad-if-else-elif.patch

# Not upstreamable
Patch1:         0001-Compatibility-with-six-1.3.0.patch
Patch2:         0002-Compatibility-with-more-recent-simplejson.patch

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-six
BuildRequires:  python-simplejson
BuildRequires:  python-nose
%if %with python3
BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-simplejson
BuildRequires:  python3-nose
%endif
BuildRequires:  python-setuptools

%global _description\
Tracks server state and statistics, allowing you to see what your server is\
doing. It can also send metrics to Graphite for graphing or to a file for crash\
forensics.\


%description %_description

%package -n python2-scales
Summary: %summary
Requires:       python-six
Requires:       python-simplejson
%{?python_provide:%python_provide python2-scales}

%description -n python2-scales %_description

%if %with python3
%package -n python3-scales
Summary:        Stats for Python 3 processes
Group:          Development/Libraries
Requires:       python3-six
Requires:       python3-simplejson

%description -n python3-scales
Tracks server state and statistics, allowing you to see what your server is
doing. It can also send metrics to Graphite for graphing or to a file for crash
forensics.
%endif


%prep
%setup -q -n scales-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%if %with python3
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python2} setup.py build

%if %with python3
cd %{py3dir}
%{__python3} setup.py build
%endif



%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%if %with python3
cd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif


%check
%{__python2} setup.py test

%if %with python3
cd %{py3dir}
%{__python3} setup.py test
%endif


%files -n python2-scales
%{python2_sitelib}/greplin/
%{python2_sitelib}/scales*.egg-info/
%{python2_sitelib}/scales*.pth
%doc AUTHORS LICENSE README.md


%if %with python3
%files -n python3-scales
%{python3_sitelib}/greplin/
%{python3_sitelib}/scales*.egg-info
%{python3_sitelib}/scales*.pth
%doc AUTHORS LICENSE README.md
%endif


%changelog
* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.5-11
- Python 2 binary package renamed to python2-scales
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 23 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.0.5-1
- Update to 1.0.5
- Add Python 3 support
- Run tests

* Thu Mar 27 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.0.3-1
- Initial packaging
