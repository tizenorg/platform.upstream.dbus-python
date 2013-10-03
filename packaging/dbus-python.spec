Name:           dbus-python
Version:        1.1.1
Release:        0
Summary:        Python bindings for D-Bus
License:        MIT
Group:          System/Libraries
Url:            http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0:        http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz
Source1001: 	dbus-python.manifest
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
Requires:       libxml2-python
Requires:       python-xml

%description
D-Bus python bindings for use with python programs.

%package  devel
Summary:        Python bindings for D-Bus
Requires:       dbus-python = %{version}

%description  devel
Developer files for Python bindings for D-Bus.

%prep
%setup -q 
cp %{SOURCE1001} .

%build
export CFLAGS="%{optflags} -fstack-protector -fno-strict-aliasing -fPIC"
%configure --docdir=%{_docdir}/dbus-python
make %{?_smp_mflags}

%install
%make_install


%remove_docs
%fdupes -s %{buildroot}

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{python_sitelib}/*
%{python_sitearch}/*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
