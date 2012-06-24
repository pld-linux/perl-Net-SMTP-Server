#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	SMTP-Server
Summary:	Net::SMTP::Server perl module
Summary(cs):	Modul Net::SMTP::Server pro Perl
Summary(da):	Perlmodul Net::SMTP::Server
Summary(de):	Net::SMTP::Server Perl Modul
Summary(es):	M�dulo de Perl Net::SMTP::Server
Summary(fr):	Module Perl Net::SMTP::Server
Summary(it):	Modulo di Perl Net::SMTP::Server
Summary(ja):	Net::SMTP::Server Perl �⥸�塼��
Summary(ko):	Net::SMTP::Server �� ����
Summary(no):	Perlmodul Net::SMTP::Server
Summary(pl):	Modu� perla Net::SMTP::Server
Summary(pt_BR):	M�dulo Perl Net::SMTP::Server
Summary(pt):	M�dulo de Perl Net::SMTP::Server
Summary(ru):	������ ��� Perl Net::SMTP::Server
Summary(sv):	Net::SMTP::Server Perlmodul
Summary(uk):	������ ��� Perl Net::SMTP::Server
Summary(zh_CN):	Net::SMTP::Server Perl ģ��
Name:		perl-Net-SMTP-Server
Version:	1.1
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a complete, RFC 821 compliant, SMTP server implementation
written entirely in Perl.  It has powerful extensively and customization
facilities that allow for a variety of potential uses.

%description -l pl
Ten modu� oferuje kompletn�, zgodn� z RFC 821 implementacj� serwera
SMTP, napisan� ca�kowicie w Perlu.  Serwer ma du�e mo�liwo�ci rozbudowy
i dostosowania do w�asnych potrzeb, co umo�liwia u�ycie go w wielu
zastosowaniach.

%prep
%setup -q -n %{pnam}-%{version}

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
%{perl_vendorlib}/Net/SMTP/Server*
# empty autosplit.ix files
#%%{perl_vendorlib}/auto/Net/SMTP
%{_mandir}/man3/*
