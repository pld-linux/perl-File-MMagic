#
# Conditional build:
%bcond_without	tests # do not perform "make test"

%define		pdir	File
%define		pnam	MMagic
%include	/usr/lib/rpm/macros.perl
Summary:	A Perl module that guesses file types based on their contents
Summary(cs.UTF-8):	Modul pro Perl na zjišťování typu souboru podle jeho obsahu
Summary(da.UTF-8):	En Perl-modul som gissar filtyper utgående fra deras indhold
Summary(de.UTF-8):	Ein Perl Modul, das eine Datei an ihrem Inhalt erkennt
Summary(es.UTF-8):	Módulo Perl que conjetura tipos de ficheros basados en su contenido
Summary(fr.UTF-8):	Un module Perl qui devine les types de fichier en fonction de leur contenu
Summary(it.UTF-8):	Modulo Perl per individuare i tipi di file in base al contenuto
Summary(ja.UTF-8):	ファイルの内容に基づいてファイルタイプを推測する Perl モジュール
Summary(ko.UTF-8):	Perl 모줄은 파일의 내용에 기초해서 파일 형태를 추축합니다
Summary(pl.UTF-8):	Moduł Perla odgadujący typ pliku na podstawie jego zawartości
Summary(pt.UTF-8):	Um módulo de Perl que adivinha o tipo dos ficheiros a partir do conteúdo
Summary(ru.UTF-8):	Модуль для Perl, который определяет тип файла по его содержимому
Summary(sv.UTF-8):	En Perl-modul som gissar filtyper utgående från deras innehåll
Summary(zh_CN.UTF-8):	一个根灸谌猜测文件类型的 Perl 模块。
Name:		perl-File-MMagic
Version:	1.30
Release:	1
License:	BSD-like/Apache
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a0157c71d5872fa07102a2ffaf7979ec
URL:		http://search.cpan.org/dist/File-MMagic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The perl-File-MMagic package provides a Perl module for guessing a
file type from the contents of the file, similar to how the file(1)
command works.

%description -l cs.UTF-8
Balíček obsahuje modul pro Perl, který umožňuje zjišťovat typ souboru
podle jeho obsahu. Jeho činnost je podobná programu file(1).

%description -l da.UTF-8
Pakken perl-File-MMagic tillhandahåller en Perl-modul for at gissa
filtypen fra indholdet i filen, lignende hvordan kommandoen file(1)
fungerar.

%description -l de.UTF-8
Das Paket perl-File-MMagic liefert ein Perl-Modul zum Herausfinden
eines Dateityps an Hand des Inhalts der Datei, ähnlich wie die file(1)
arbeitet.

%description -l es.UTF-8
El conjunto de perl-File-MMagic proporciona a un módulo del Perl para
adivinar un tipo de fichero por el contenido del fichero, similar a
como el comando de file(1) funciona.

%description -l fr.UTF-8
Le paquetage Perl-File-MMagic fournit un module Perl permettant de
deviner le type d'un fichier à partir de son contenu, semblable à la
façon dont fonctionne la commande du file(1).

%description -l it.UTF-8
Il pacchetto perl-File-MMagic fornisce un modulo Perl per individuare
un tipo di file dal suo contenuto, in modo simile al comando file(1).

%description -l ja.UTF-8
perl-File-MMagic パッケージは、ファイルの内容からファイルのタイプを推
測するための Perl モジュールを提供し、file(1) コマンドと同様の役割を
果たします。

%description -l pl.UTF-8
Moduł ten rozpoznaje typ pliku na podstawie jego zawartości podobnie
jak polecenie file(1).

%description -l pt.UTF-8
O pacote perl-File-MMagic oferece um módulo de Perl para adivinhar o
tipo dum ficheiro a partir do seu conteúdo, de maneira semelhante à
que o comando file(1) funciona.

%description -l ru.UTF-8
Пакет perl-File-MMagic содержит модуль для Perl, которые пытается
определить тип файла, по содержимому файла, подобно тому как работает
команда file(1).

%description -l sv.UTF-8
Paketet perl-File-MMagic tillhandahåller en Perl-modul för att gissa
filtypen från innehållet i filen, liknande hur kommandot file(1)
fungerar.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.en ChangeLog
%{perl_vendorlib}/File/*
%{_mandir}/man3/*
