%define version 2.20.1
%define name zenity
Summary: Zenity is a basic rewrite of gdialog, with simplicity of use in mind.
Name: %{name}
Version: %{version}
Release: 1
Vendor: N/A
URL: http://ftp.gnome.org/pub/GNOME/sources/zenity/%{version}/
Source: http://ftp.gnome.org/pub/GNOME/sources/zenity/%{version}/%{name}-%{version}.tar.bz2
License: LGPL
Group: Applications/System
Packager: Mihai Lazarescu <mihai@email.it>
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: bzip2
BuildRequires: fileutils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: glibc-devel
BuildRequires: gtk+ >= 2.0.0
BuildRequires: gzip
BuildRequires: info
BuildRequires: intltool
BuildRequires: libglade >= 2.0.0
BuildRequires: libgnomecanvas >= 2.0.0
BuildRequires: libtool
BuildRequires: make
BuildRequires: popt
BuildRequires: scrollkeeper
BuildRequires: sh-utils
BuildRequires: tar
Requires: gtk+ >= 2.0.0
Requires: libglade >= 2.0.0
Requires: libgnomecanvas >= 2.0.0
Provides: %{name}

%define rpm_prefix /usr

%description
Zenity is a basic rewrite of gdialog, without the pain involved
of trying to figure out commandline parsing.  Zenity is
zen-like; simple and easy to use.

Zenity Dialogs: Calendar, Text Entry, Error, Informational,
File Selection, List, Progress, Question, Text Information,
and Warning.

Zenity is especially useful in scripts.


%prep
%setup -q
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT


%build
./configure --prefix=%{rpm_prefix}
%{__make} all


%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{rpm_prefix} install


%clean
%{__rm} -rf $RPM_BUILD_ROOT%{rpm_prefix}


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog HACKING INSTALL
%doc NEWS README THANKS TODO help

%{rpm_prefix}


%changelog
* Thu Mar 6 2003 Glynn Foster <glynn.foster@sun.com>
- Fix up the %defines. Not sure if this makes a difference but it
  seems cleaner to me

* Thu Feb 1 2003 Mihai Lazarescu <mihai@email.it>
- first release for version 1.0
