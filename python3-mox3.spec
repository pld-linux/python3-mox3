#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Mock object framework for Python 3
Summary(pl.UTF-8):	Szkielet obiektów atrap dla Pythona 3
Name:		python3-mox3
Version:	1.1.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mox3/
Source0:	https://files.pythonhosted.org/packages/source/m/mox3/mox3-%{version}.tar.gz
# Source0-md5:	0eff74d3a85ec4d4dc6acf7f524ca816
Patch0:		mox3-inspect-update.patch
URL:		https://pypi.org/project/mox3/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-testtools >= 2.2.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-openstackdocstheme >= 1.18.1
BuildRequires:	sphinx-pdg-3 >= 1.7.0
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mox3 is an unofficial port of the Google mox framework to Python 3. It
was meant to be as compatible with mox as possible, but small
enhancements have been made.

%description -l pl.UTF-8
Mox3 to nieoficjalny port szkieletu Google mox do Pythona 3. Ma być
możliwie zgodny z mox, ale zostały dodane niewielkie rozszerzenia.

%package apidocs
Summary:	API documentation for Python mox3 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona mox3
Group:		Documentation

%description apidocs
API documentation for Python mox3 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona mox3.

%prep
%setup -q -n mox3-%{version}
%patch -P0 -p1

%build
%py3_build

%if %{with tests}
stestr run
%endif

%if %{with doc}
sphinx-build-3 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/mox3/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/mox3
%{py3_sitescriptdir}/mox3-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,user,*.html,*.js}
%endif
