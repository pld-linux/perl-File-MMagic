%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	MMagic

Summary:	File-MMagic perl module
Summary(ja):	file���ޥ����perl5�⥸�塼��
Summary(pl):	Modu� perla File-MMagic
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
���Υ⥸�塼��ϡ�file(1)���ޥ�ɤ��������뵡ǽ�����ʤ���ե��������
�Ƥ��餽�μ�����¬���뤿��Τ�ΤǤ���

%description -l pl
Modu� ten rozpoznaje typ pliku na podstawie jego kontekstu podobnie
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
