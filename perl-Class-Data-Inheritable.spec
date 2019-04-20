#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Data-Inheritable
Version  : 0.08
Release  : 18
URL      : http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/Class-Data-Inheritable-0.08.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/Class-Data-Inheritable-0.08.tar.gz
Summary  : Inheritable, overridable class data
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Class::Data::Inheritable - Inheritable, overridable class data
SYNOPSIS
package Stuff;
use base qw(Class::Data::Inheritable);

%package dev
Summary: dev components for the perl-Class-Data-Inheritable package.
Group: Development
Provides: perl-Class-Data-Inheritable-devel = %{version}-%{release}
Requires: perl-Class-Data-Inheritable = %{version}-%{release}

%description dev
dev components for the perl-Class-Data-Inheritable package.


%prep
%setup -q -n Class-Data-Inheritable-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Class/Data/Inheritable.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Data::Inheritable.3
