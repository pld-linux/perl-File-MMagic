%include	/usr/lib/rpm/macros.perl
Summary:	File-MMagic perl module
Summary(pl):	Modu³ perla File-MMagic
Name:		perl-File-MMagic
Version:	1.13
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-MMagic-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is to guess file type from its contents like file(1)
command.

%description -l pl
Modul ten rozpoznaje typ pliku na podstawie jego kontekstu podobnie
jak komenda file.

%prep
%setup -q -n File-MMagic-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README.en ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/File/*
