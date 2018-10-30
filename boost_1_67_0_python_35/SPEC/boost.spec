%define _topdir   /search/odin/spgoal/projects/rpm_learning/boost_1_67_0_python_35 
%define name      boost
%define version   1_67_0

Name:           %{name}_python35
Version:        %{version}
Release:        1%{?dist}
Summary:        Boost.Python for produce c/c++ lib in python3.5
License:        GPLv3+
Source:         boost_%{version}.tar.gz
Prefix:         %{_prefix}
URL:            https://dl.bintray.com/boostorg/release/1.67.0/source/boost_1_67_0.tar.gz
#Source0:        
#
#BuildRequires:  
#Requires(pre):  /bin/sh

Packager:       spgoal

%description
The boost for python3.5 use, first version using 1.67.0, build from sources.

%prep
%autosetup -n boost_%{version}

%build
#echo "using mpi ;
#using gcc :  : g++ ;
#using python : 3.5 : /usr/local/bin/python3.5 : /usr/local/include/python3.5m : /usr/local/lib ;" > ~/user-config.jam
sed -i 's/python$(version) ;/python$(version)m ;/g' tools/build/src/tools/python.jam

%install
#./bootstrap.sh --with-python=/usr/local/bin/python3.5 --with-python-version=3.5 --with-python-root=/usr/local/lib/python3.5 --prefix=%{buildroot}%{_prefix} --with-libraries=system,thread,python
./bootstrap.sh --with-python=/usr/local/bin/python3.5 --prefix=%{buildroot}%{_prefix}
./b2 install

#%pre

%post
echo "export CPLUS_INCLUDE_PATH=\$CPLUS_INCLUDE_PATH:"%{_prefix}"/include" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:"%{_prefix}"/lib" >> ~/.bashrc
source ~/.bashrc

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/*

%files
%defattr (777,root,root,755)
%{_prefix}/lib/libboost*
%{_prefix}/include

%changelog
* Fri Oct 26 2018 spgoal <gejx2010@gmail.com> - 1.67.0
- Init at 1.67.0 for python 3.5
