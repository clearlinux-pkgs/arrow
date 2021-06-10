#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : arrow
Version  : 1.1.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/0a/97/e58a3cd2207cb9cb7aa9b91f3bc4df3b4e13eafc88d75b1a9f4535ea6e1f/arrow-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0a/97/e58a3cd2207cb9cb7aa9b91f3bc4df3b4e13eafc88d75b1a9f4535ea6e1f/arrow-1.1.0.tar.gz
Summary  : Better dates & times for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: arrow-python = %{version}-%{release}
Requires: arrow-python3 = %{version}-%{release}
Requires: Sphinx
Requires: python-dateutil
Requires: pytz
Requires: simplejson
Requires: typing_extensions
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : pytz
BuildRequires : simplejson
BuildRequires : tox
BuildRequires : typing_extensions
BuildRequires : virtualenv

%description
======================================
        
        .. start-inclusion-marker-do-not-remove

%package python
Summary: python components for the arrow package.
Group: Default
Requires: arrow-python3 = %{version}-%{release}

%description python
python components for the arrow package.


%package python3
Summary: python3 components for the arrow package.
Group: Default
Requires: python3-core
Provides: pypi(arrow)
Requires: pypi(python_dateutil)

%description python3
python3 components for the arrow package.


%prep
%setup -q -n arrow-1.1.0
cd %{_builddir}/arrow-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623346857
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*