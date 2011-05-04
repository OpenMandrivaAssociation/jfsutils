Summary:	IBM JFS utility programs
Name:		jfsutils
Version:	1.1.13
Release:	%manbo_mkrel 4
License:	GPLv3
Group:		System/Kernel and hardware
URL:		http://jfs.sourceforge.net/
Source0:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/%{name}-%{version}.tar.gz
Patch0:		jfsutils-1.1.12-uuid.patch
Patch1:		jfsutils-1.1.13-format_not_a_string_literal_and_no_format_arguments.diff
Obsoletes:	jfsprogs < %version-%release
Provides:	jfsprogs = %version-%release
BuildRequires:	libblkid-devel
BuildRequires:	libuuid-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The jfsutils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in JFS
filesystems.  The following utilities are available: fsck.jfs - initiate
replay of the JFS transaction log, and check and repair a JFS formatted
device; logdump - dump a JFS formatted device's journal log; logredo -
"replay" a JFS formatted device's journal log;  mkfs.jfs - create a JFS
formatted partition; xchkdmp - dump the contents of a JFS fsck log file
created with xchklog; xchklog - extract a log from the JFS fsck workspace
into a file;  xpeek - shell-type JFS file system editor.

%prep

%setup -q 
%patch0 -p1 -b .uuid
%patch1 -p1 -b .format_not_a_string_literal_and_no_format_arguments

%build
%configure2_5x	--sbindir=/sbin
%make 

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/sbin/*
%{_mandir}/*/*
