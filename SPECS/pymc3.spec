%{?scl:%scl_package pymc3}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}pymc3
Version:        3.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities

Group:          Development/Languages
License:        Apache
URL:            https://github.com/pymc-devs/pymc3
Source0:        https://github.com/pymc-devs/pymc3/archive/v%{version}/pymc3-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  scl-utils-build %{?scl_prefix}python-devel

%description
Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine
Learning with Theano

%prep
%setup -q -n pymc3-%{version}

%build
%{?scl:scl enable %{scl} - << \EOF}
%{python27__python2} setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{python27__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{?scl:EOF}

%files
%doc LICENSE README docs/source/index.rst
%{python_sitelib}/*
