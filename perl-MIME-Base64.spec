%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Base64
Summary:	Perl MIME::Base64 module
Summary(cs):	Modul MIME::Base64 pro Perl
Summary(da):	Perlmodul MIME::Base64
Summary(de):	MIME::Base64 Perl Modul
Summary(es):	Módulo de Perl MIME::Base64
Summary(fr):	Module Perl MIME::Base64
Summary(it):	Modulo di Perl MIME::Base64
Summary(ja):	MIME::Base64 Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	MIME::Base64 ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul MIME::Base64
Summary(pl):	Modu³ Perla MIME::Base64
Summary(pt):	Módulo de Perl MIME::Base64
Summary(pt_BR):	Módulo Perl MIME::Base64
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl MIME::Base64
Summary(sv):	MIME::Base64 Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl MIME::Base64
Summary(zh_CN):	MIME::Base64 Perl Ä£¿é
Name:		perl-MIME-Base64
Version:	2.16
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a base64 encoder/decoder and a quoted-printable
encoder/decoder. These encoding methods are specified in RFC 2045 -
MIME (Multipurpose Internet Mail Extensions).

The Base64 encoding is designed to represent arbitrary sequences of
octets in a form that need not be humanly readable. A 65-character
subset ([A-Za-z0-9+/=]) of US-ASCII is used, enabling 6 bits to be
represented per printable character.

The quoted-printable encoding is intended to represent data that
largely consists of bytes that correspond to printable characters in
the ASCII character set. Non-printable characters are represented by a
triplet consisting of the character "=" followed by two hexadecimal
digits.

%description -l pl
Modu³ perla wspomagaj±cy algorytm MIME Base64.
Ten pakiet zawiera (de)koder base64 i quoted-printable. Metody te
okre¶lone s± w RFC 2045 - MIME (Multipurpose Internet Mail Extensions).

Kod base64 zaprojektowano do reprezentowania okre¶lonej sekwencji
oktetów w formie, która nie musi byæ czytelna dla cz³owieka. U¿ywany
jest 65-znakowy ([A-Za-z0-9+/=]) podzestaw z zestawu US-ASCII,
reprezentuj±c ka¿dy znak drukowalny sze¶cioma bitami.

Kod quoted-printable stosuje siê do reprezentacji danych, które w
wiêkszo¶ci zawieraj± znaki drukowlne ASCII. Znaki niedrukowalne s±
kodowane w triplety zawieraj±ce poprzedzone znakiem "=" dwie cyfry
szesnastkowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/MIME/*.pm
%dir %{perl_sitearch}/MIME
%dir %{perl_sitearch}/auto/MIME
%dir %{perl_sitearch}/auto/MIME/Base64
%{perl_sitearch}/auto/MIME/Base64/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/MIME/Base64/*.so
%{_mandir}/man3/*
