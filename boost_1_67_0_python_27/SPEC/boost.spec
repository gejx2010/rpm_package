%define _topdir   /search/odin/gejx2010/projects/rpm_learning/boost_1_67_0_python_27
%define name      boost
%define version   1_67_0
%define prefix    %{_usr}

Name:           %{name}
Version:        %{version}
Release:        1%{?dist}
Summary:        Boost.Python for produce c/c++ lib in python
License:        GPLv3+
Source:         %{name}_%{version}.tar.gz
Prefix:         %{_prefix}
URL:            https://dl.bintray.com/boostorg/release/1.67.0/source/boost_1_67_0.tar.gz
#Source0:        
#
#BuildRequires:  
#Requires(pre):  /bin/sh

Packager:       spgoal

%description
The boost for python use, first version using 1.67.0, build from sources.


%prep
%autosetup -n %{name}_%{version}


#%build

%install
./bootstrap.sh --with-python=PYTHON --with-libraries=system,thread,python --prefix=%{buildroot}/%{_prefix}
./b2 install
./b2 cxxflags=-fPIC cflags=-fPIC --c++11

%post
echo "export CPLUS_INCLUDE_PATH=\$CPLUS_INCLUDE_PATH:"%{_prefix}"/include" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:"%{_prefix}"/lib" >> ~/.bashrc
source ~/.bashrc

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/*

%files
%defattr (777,root,root,755)
%{_prefix}/include
%{_prefix}/lib/*

%changelog
* Fri Oct 26 2018 spgoal <gejx2010@gmail.com> - 1.67.0
- Init at 1.67.0 for python 2
