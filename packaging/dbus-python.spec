Name:           dbus-python
Version:        1.1.1
Release:        0
Summary:        Python bindings for D-Bus
License:        MIT
Group:          Development/Libraries/Python
Url:            http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0:        http://dbus.freedesktop.org/releases/dbus-python/dbus-python-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
Requires:       libxml2-python
Requires:       python-xml
Requires:       dbus >= %( echo `rpm -q --queryformat '%{VERSION}-%{RELEASE}' dbus`)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
D-Bus python bindings for use with python programs.

%package  devel
Summary:        Python bindings for D-Bus
Group:          Development/Libraries/Python
Requires:       dbus-python = %{version}
Requires:       dbus >= %( echo `rpm -q --queryformat '%{VERSION}-%{RELEASE}' dbus`)
Requires:       dbus-devel >= %( echo `rpm -q --queryformat '%{VERSION}-%{RELEASE}' dbus-devel`)

%description  devel
Developer files for Python bindings for D-Bus.

%prep
%setup -q 

%build
export CFLAGS="%{optflags} -fstack-protector -fno-strict-aliasing -fPIC"
%configure --docdir=%{_docdir}/dbus-python
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Install additional docs


%remove_docs
%fdupes -s %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*
%{python_sitearch}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
