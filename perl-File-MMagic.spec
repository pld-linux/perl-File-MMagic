%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	MMagic

Summary:	File-MMagic perl module
Summary(ja):	file¥³¥Þ¥ó¥ÉÉ÷perl5¥â¥¸¥å¡¼¥ë
Summary(pl):	Modu³ perla File-MMagic
Name:		perl-File-MMagic
Version:	1.15
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is to guess file type from its contents like file(1)
command.

%description -l ja
¤³¤Î¥â¥¸¥å¡¼¥ë¤Ï¡¢file(1)¥³¥Þ¥ó¥É¤ËÁêÅö¤¹¤ëµ¡Ç½¡¢¤¹¤Ê¤ï¤Á¥Õ¥¡¥¤¥ë¤ÎÆâ
ÍÆ¤«¤é¤½¤Î¼ïÎà¤ò¿äÂ¬¤¹¤ë¤¿¤á¤Î¤â¤Î¤Ç¤¹¡£

%description -l pl
Modu³ ten rozpoznaje typ pliku na podstawie jego kontekstu podobnie
jak komenda file(1).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
