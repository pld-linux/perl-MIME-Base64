%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Base64
Summary:	Base64 and QuotedPrintable encoders/decoders for Perl
Summary(pl):	Funkcje dla Perla koduj±ce i dekoduj±ce Base64 i QuotedPrintable
Name:		perl-MIME-Base64
Version:	2.18
Release:	3
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Encode)'

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
Ten pakiet zawiera (de)kodery base64 i quoted-printable. Metody te
okre¶lone s± w RFC 2045 - MIME (Multipurpose Internet Mail
Extensions).

Kod base64 zaprojektowano do reprezentowania okre¶lonej sekwencji
oktetów w formie, która nie musi byæ czytelna dla cz³owieka. U¿ywany
jest 65-znakowy ([A-Za-z0-9+/=]) podzestaw z zestawu US-ASCII,
reprezentuj±c ka¿dy znak drukowalny sze¶cioma bitami.

Kod quoted-printable stosuje siê do reprezentacji danych, które w
wiêkszo¶ci zawieraj± znaki drukowalne ASCII. Znaki niedrukowalne s±
kodowane w triplety zawieraj±ce poprzedzone znakiem "=" dwie cyfry
szesnastkowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
