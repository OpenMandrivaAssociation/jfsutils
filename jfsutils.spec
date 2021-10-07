%global optflags %optflags -fcommon
Summary:	IBM JFS utility programs
Name:		jfsutils
Version:	1.1.15
Release:	17
License:	GPLv3
Group:		System/Kernel and hardware
Url:		http://jfs.sourceforge.net/
Source0:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/%{name}-%{version}.tar.gz
Patch0:		jfsutils-1.1.12-uuid.patch
Patch1:		jfsutils-glibc-2.28.patch
Patch2:		jfsutils-1.1.15-string-literal.diff
Patch3:		jfsutils-1.1.15-add-stdint-for-c99-types.patch

BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(uuid)
%rename		jfsprogs

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

%prep
%autosetup -p1

%build
%configure \
	--sbindir=/sbin
%make_build

%install
%make_install

%files
/sbin/*
%{_mandir}/*/*
