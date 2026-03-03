%undefine __cmake_in_source_build

Summary: Library that overrides the uname() system call to a fake kernel release
Name: fakeuname
Version: 1.0.1
Release: 1%{?dist}
License: LGPL-2.1-or-later
Url: https://github.com/rpm-software-management/fakeuname
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake >= 3.5.0
BuildRequires: gcc

%global debug_package %{nil}

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libfakeuname.so
%{_bindir}/fakeuname

%description
Provides a libfakeuname.so library and a setup script that preloads the library
(using LD_PRELOAD) and runs a command with the kernel release overridden (via
the uname system call) to a custom value.

%changelog
* Fri Apr 16 2021 Lukas Hrazky <lhrazky@redhat.com> - 1.0.1-1
- 1.0.1 bump

* Tue Oct 15 2019 Lukas Hrazky <lhrazky@redhat.com> - 1.0.0-1
- Initial package
