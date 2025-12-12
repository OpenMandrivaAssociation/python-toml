%global pypi_name toml

Name:		python-%{pypi_name}
Version:	0.10.2
Release:	4
Summary:	Python Library for Tom's Obvious, Minimal Language
Group:		Development/Python
License:	MIT
URL:		https://github.com/uiri/toml
Source0:	https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
#BuildRequires:  python3dist(pytest)

%{?python_provide:%python_provide python-%{pypi_name}}

%description
A Python library for parsing and creating TOML.

%prep -a
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py%{py_ver}.egg-info
