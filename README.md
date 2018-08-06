golang-dep-rpm
==============

An rpm package for [golang/dep: Go dependency tool](https://github.com/golang/dep) for CentOS 6 and 7.


Build RPM `golang-dep` :
========================

    git clone https://github.com/hnakamur/golang-dep-rpm

    mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

    cp golang-dep-rpm/SOURCES/dep-0.5.0.tar.gz ~/rpmbuild/SOURCES/
    
    rpmbuild -ba golang-dep-rpm/SPECS/golang-dep.spec

RPMS and SRPMS will be in `~/rpmbuild/RPMS/` and `~/rpmbuild/SRPMS/`


To update `dep` version from upstream
=====================================

To update `dep` version from upstream, and contribute a pull request to this repository:

1. Fork https://github.com/hnakamur/golang-dep-rpm
1. `git clone git@github.com:YOUR_GITHUB_NAME/golang-dep-rpm.git`

Then proceed to create the needed RPM source archive from upstream, updated. From example, here from `0.4.1` to `0.5.0`

    v=0.5.0

    # Delete previous sources
    rm -rf golang-dep-rpm/SOURCES/*
    pushd golang-dep-rpm/SOURCES

    # Prepare to install source dependencies in order to compile `dep`
    mkdir -p dep-$v/go/src/github.com/golang
    pushd dep-$v/go
    export GOPATH=`pwd`
    pushd "$GOPATH/src/github.com/golang"
    git clone https://github.com/golang/dep.git dep
    pushd dep
    export GITHUB_PROJECT_PATH=src/github.com/golang/dep
    git checkout v$v
    rm -rf .git

    # get (install locally) source dependencies in order to compile `dep` 
    dep ensure -vendor-only -v

    # Package everything as source archive for `rpmbuild`
    popd
    popd
    popd
    tar czf dep-$v.tar.gz dep-$v
    rm -rf dep-$v

    # Edit RPM spec to use source archive 0.5.0
    cd ..
    vi SPECS/golang-dep.spec 

At this point we get everything to build the RPM. You can `git rm`, `git add`, `git commit`, `git push` to contribute changes to this project

