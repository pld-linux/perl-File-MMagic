#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	MMagic
Summary:	A Perl module that guesses file types based on their contents
Summary(cs):	Modul pro Perl na zji��ov�n� typu souboru podle jeho obsahu
Summary(da):	En Perl-modul som gissar filtyper utg�ende fra deras indhold
Summary(de):	Ein Perl Modul, das eine Datei an ihrem Inhalt erkennt
Summary(es):	M�dulo Perl que conjetura tipos de ficheros basados en su contenido
Summary(fr):	Un module Perl qui devine les types de fichier en fonction de leur contenu
Summary(it):	Modulo Perl per individuare i tipi di file in base al contenuto
Summary(ja):	�ե���������Ƥ˴�Ť��ƥե����륿���פ��¬���� Perl �⥸�塼��
Summary(ko):	Perl ������ ������ ���뿡 �����ؼ� ���� ���¸� �����մϴ�
Summary(pl):	Modu� perla odgaduj�cy typ pliku na podstawie jego zawarto�ci
Summary(pt):	Um m�dulo de Perl que adivinha o tipo dos ficheiros a partir do conte�do
Summary(ru):	������ ��� Perl, ������� ���������� ��� ����� �� ��� �����������
Summary(sv):	En Perl-modul som gissar filtyper utg�ende fr�n deras inneh�ll
Summary(zh_CN):	һ�������Ȳ²��ļ����͵� Perl ģ�顣
Name:		perl-File-MMagic
Version:	1.20
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f1f7189c9f2a2c19157a756a0d177e5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The perl-File-MMagic package provides a Perl module for guessing a
file type from the contents of the file, similar to how the file(1)
command works.

%description -l cs
Bal��ek obsahuje modul pro Perl, kter� umo��uje zji��ovat typ souboru
podle jeho obsahu. Jeho �innost je podobn� programu file(1).

%description -l da
Pakken perl-File-MMagic tillhandah�ller en Perl-modul for at gissa
filtypen fra indholdet i filen, lignende hvordan kommandoen file(1)
fungerar.

%description -l de
Das Paket perl-File-MMagic liefert ein Perl-Modul zum Herausfinden
eines Dateityps an Hand des Inhalts der Datei, �hnlich wie die file(1)
arbeitet.

%description -l es
El conjunto de perl-File-MMagic proporciona a un m�dulo del Perl para
adivinar un tipo de fichero por el contenido del fichero, similar a
como el comando de file(1) funciona.

%description -l fr
Le paquetage Perl-File-MMagic fournit un module Perl permettant de
deviner le type d'un fichier � partir de son contenu, semblable � la
fa�on dont fonctionne la commande du file(1).

%description -l it
Il pacchetto perl-File-MMagic fornisce un modulo Perl per individuare
un tipo di file dal suo contenuto, in modo simile al comando file(1).

%description -l ja
perl-File-MMagic �ѥå������ϡ��ե���������Ƥ���ե�����Υ����פ��
¬���뤿��� Perl �⥸�塼����󶡤���file(1) ���ޥ�ɤ�Ʊ�ͤ�����
�̤����ޤ���

%description -l pl
Modu� ten rozpoznaje typ pliku na podstawie jego zawarto�ci podobnie
jak polecenie file(1).

%description -l pt
O pacote perl-File-MMagic oferece um m�dulo de Perl para adivinhar o
tipo dum ficheiro a partir do seu conte�do, de maneira semelhante �
que o comando file(1) funciona.

%description -l ru
����� perl-File-MMagic �������� ������ ��� Perl, ������� ��������
���������� ��� �����, �� ����������� �����, ������� ���� ��� ��������
������� file(1).

%description -l sv
Paketet perl-File-MMagic tillhandah�ller en Perl-modul f�r att gissa
filtypen fr�n inneh�llet i filen, liknande hur kommandot file(1)
fungerar.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.en ChangeLog
%{perl_vendorlib}/File/*
%{_mandir}/man3/*
