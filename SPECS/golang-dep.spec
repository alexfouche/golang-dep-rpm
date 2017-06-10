%define debug_package %{nil}

%global commit             ba5773dd0be10249a867d207cb4f57f690db6a6a
%global shortcommit        %(c=%{commit}; echo ${c:0:7})

Name:	        golang-dep
Version:	0.1.0
Release:	2.1.git%{shortcommit}%{?dist}
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
* Sun Jun 11 2017 <hnakamur@gmail.com> - 0.1.0-2.1.gitba5773d
- Update to commit ba5773dd0be10249a867d207cb4f57f690db6a6a

* Sun Jun 11 2017 <hnakamur@gmail.com> - 0.1.0-1
- Update to v0.1.0

* Tue May  2 2017 <hnakamur@gmail.com> - 0-0.2.gitbba3159
- Update to commit bba3159e387acbffff1e61735d2415e86a5f93b9

* Tue Apr 11 2017 <hnakamur@gmail.com> - 0-0.1.git3ef7bf8
- Initial release
