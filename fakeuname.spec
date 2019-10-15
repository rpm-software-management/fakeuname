Summary: A small library that overrides the uname() system call to return a configured fake kernel release.
Name: fakeuname
Version: 1.0.0
Release: 1%{?dist}
License: LGPLv2+
Url: https://github.com/rpm-software-management/fakeuname
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

%global debug_package %{nil}

%prep
%autosetup

%build
%cmake .
%make_build

%install
%make_install

%files
%{_libdir}/libfakeuname.so
%{_bindir}/fakeuname

%description
Provides a libfakeuname.so library and a setup script that preloads the library
(using LD_PRELOAD) and runs a command with the kernel release overridden (via
the uname syscall) to a custom value.

%changelog
* Tue Oct 15 2019 Lukas Hrazky <lhrazky@redhat.com> - 1.0.0-1
- Initial package
