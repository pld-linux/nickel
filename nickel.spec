Summary:	Nickel - a library for hierarchical maps and .ini files
Summary(pl.UTF-8):	Nickel - biblioteka do map hierarchicznych oraz plików .ini
Name:		nickel
Version:	1.1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/chazomaticus/bohr/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4f1003e297dbacc11fed2085a6fe683b
URL:		https://github.com/chazomaticus/bohr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nickel is a library for hierarchical maps and .ini files. It's one of
the Bohr Game Libraries.

%description -l pl.UTF-8
Nickel to biblioteka do map hierarchicznych oraz plików .ini. Jest to
jedna z bibliotek Bohr do gier (Bohr Game Libraries).

%package devel
Summary:	Header files for Nickel library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Nickel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Nickel library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Nickel.

%prep
%setup -q -n bohr-nickel-%{version}

%build
%{__make} -C src \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir}

ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libnickel.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libnickel.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libnickel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnickel.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnickel.so
%dir %{_includedir}/bohr
%{_includedir}/bohr/ni.h
