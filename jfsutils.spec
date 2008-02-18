%define	name	jfsutils
%define	version	1.1.12
%define	release	%manbo_mkrel 1

Summary:	IBM JFS utility programs
Name:		%{name}
Version:	%{version}
Release:	%{release}
Url:		http://jfs.sourceforge.net/
Source0:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Kernel and hardware
Obsoletes:	jfsprogs
Provides:	jfsprogs
BuildRequires:	e2fsprogs-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
IBM's journaled file system technology, currently used in IBM
enterprise servers, is designed for high-throughput
server environments, key to running intranet and other
high-performance e-business file servers. IBM is
contributing this technology to the Linux open source
community with the hope that some or all of it will be
useful in bringing the best of journaling capabilities to
the Linux operating system.

%prep
%setup -q 

%build
%configure2_5x	--sbindir=/sbin
%make 

%install
rm -rf %{buildroot}

%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/sbin/*
%{_mandir}/*/*
