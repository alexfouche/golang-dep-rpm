%define debug_package %{nil}

%global commit             3ef7bf880f6f67548f7a0d2ab3b8d4ebd1803d8e
%global shortcommit        %(c=%{commit}; echo ${c:0:7})

Name:	        golang-dep
Version:	0
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	Go dependency tool

Group:		Development/Tools
License:	BSD-3-Clause License
URL:		https://github.com/golang/dep

Source0:	https://github.com/golang/dep/archive/%{commit}.tar.gz#/dep-%{commit}.tar.gz

BuildRoot:      %{name}
BuildRequires:  golang >= 1.8

%description
Dep is a prototype dependency management tool. It requires Go 1.7 or newer to compile.

dep is NOT an official tool. Yet. Check out the Roadmap!

%prep
%setup -c -n %{name}/go/src/github.com/golang
cd %{_builddir}/%{name}/go/src/github.com/golang
%{__mv} dep-%{commit} dep

%build
export GOPATH=%{_builddir}/%{name}/go
cd "$GOPATH/src/github.com/golang/dep"
go install ./...

%install
%{__rm} -rf %{buildroot}
%{__install} -pD -m 755 "%{_builddir}/%{name}/go/bin/dep" %{buildroot}%{_bindir}/dep
%{__install} -pD -m 755 "%{_builddir}/%{name}/go/bin/licenseok" %{buildroot}%{_bindir}/licenseok

%files
%defattr(0755,root,root,-)
%{_bindir}/dep
%{_bindir}/licenseok

%changelog
* Tue Apr 11 2017 <hnakamur@gmail.com> - 0-0.1.git3ef7bf8.el7.centos
- Initial release
