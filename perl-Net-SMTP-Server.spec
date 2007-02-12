#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SMTP-Server
Summary:	Net::SMTP::Server perl module
Summary(cs.UTF-8):   Modul Net::SMTP::Server pro Perl
Summary(da.UTF-8):   Perlmodul Net::SMTP::Server
Summary(de.UTF-8):   Net::SMTP::Server Perl Modul
Summary(es.UTF-8):   Módulo de Perl Net::SMTP::Server
Summary(fr.UTF-8):   Module Perl Net::SMTP::Server
Summary(it.UTF-8):   Modulo di Perl Net::SMTP::Server
Summary(ja.UTF-8):   Net::SMTP::Server Perl モジュール
Summary(ko.UTF-8):   Net::SMTP::Server 펄 모줄
Summary(nb.UTF-8):   Perlmodul Net::SMTP::Server
Summary(pl.UTF-8):   Moduł perla Net::SMTP::Server
Summary(pt_BR.UTF-8):   Módulo Perl Net::SMTP::Server
Summary(pt.UTF-8):   Módulo de Perl Net::SMTP::Server
Summary(ru.UTF-8):   Модуль для Perl Net::SMTP::Server
Summary(sv.UTF-8):   Net::SMTP::Server Perlmodul
Summary(uk.UTF-8):   Модуль для Perl Net::SMTP::Server
Summary(zh_CN.UTF-8):   Net::SMTP::Server Perl 模块
Name:		perl-Net-SMTP-Server
Version:	1.1
Release:	6
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	29539763294a4cbe88d3e520b3de45c1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a complete, RFC 821 compliant, SMTP server implementation
written entirely in Perl.  It has powerful extensively and customization
facilities that allow for a variety of potential uses.

%description -l pl.UTF-8
Ten moduł oferuje kompletną, zgodną z RFC 821 implementację serwera
SMTP, napisaną całkowicie w Perlu.  Serwer ma duże możliwości rozbudowy
i dostosowania do własnych potrzeb, co umożliwia użycie go w wielu
zastosowaniach.

%prep
%setup -q -n %{pnam}-%{version}

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
%{perl_vendorlib}/Net/SMTP/Server*
# empty autosplit.ix files
#%%{perl_vendorlib}/auto/Net/SMTP
%{_mandir}/man3/*
