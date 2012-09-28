%bcond_without	uclibc

Summary:	IBM JFS utility programs
Name:		jfsutils
Version:	1.1.15
Release:	2
License:	GPLv3
Group:		System/Kernel and hardware
URL:		http://jfs.sourceforge.net/
Source0:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/%{name}-%{version}.tar.gz
Patch0:		jfsutils-1.1.12-uuid.patch
Patch2:		jfsutils-1.1.15-string-literal.diff
%rename		jfsprogs
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(uuid)
%if %{with buildrequires}
BuildRequires:	uClibc-devel >= 0.9.33.2-9
%endif

%description
The jfsutils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in JFS
filesystems.
The following utilities are available:
* fsck.jfs - initiate replay of the JFS transaction log, and check and
  repair a JFS formatted device
* logdump  - dump a JFS formatted device's journal log
* logredo  - "replay" a JFS formatted device's journal log
* mkfs.jfs - create a JFS formatted partition
* xchkdmp  - dump the contents of a JFS fsck log file created with xchklog
* xchklog  - extract a log from the JFS fsck workspace into a file
* xpeek    - shell-type JFS file system editor

%package -n	uclibc-%{name}
Summary:	IBM JFS utility programs (uClibc build)
Group:		System/Kernel and hardware

%description -n	uclibc-%{name}
The jfsutils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in JFS
filesystems.
The following utilities are available:
* fsck.jfs - initiate replay of the JFS transaction log, and check and
  repair a JFS formatted device
* logdump  - dump a JFS formatted device's journal log
* logredo  - "replay" a JFS formatted device's journal log
* mkfs.jfs - create a JFS formatted partition
* xchkdmp  - dump the contents of a JFS fsck log file created with xchklog
* xchklog  - extract a log from the JFS fsck workspace into a file
* xpeek    - shell-type JFS file system editor

%prep
%setup -q
%patch0 -p1 -b .uuid~
%patch2 -p1 -b .literal~

%build
CONFIGURE_TOP=$PWD
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
%configure2_5x	CC=%{uclibc_cc} \
		CFLAGS="%{uclibc_cflags}" \
		--sbindir=%{uclibc_root}/sbin
%make
popd
%endif

mkdir -p system
pushd system
%configure2_5x	--sbindir=/sbin
%make
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc
%endif

%makeinstall_std -C system

%files
/sbin/*
%{_mandir}/*/*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}/sbin/*
%endif
