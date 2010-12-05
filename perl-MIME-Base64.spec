#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Base64
Summary:	Base64 and QuotedPrintable encoders/decoders for Perl
Summary(pl.UTF-8):	Funkcje dla Perla kodujące i dekodujące Base64 i QuotedPrintable
Name:		perl-MIME-Base64
Version:	3.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/GAAS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a555d807b328aee871c686a6b6bae5b4
URL:		http://search.cpan.org/dist/MIME-Base64/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Ten pakiet zawiera (de)kodery base64 i quoted-printable. Metody te
określone są w RFC 2045 - MIME (Multipurpose Internet Mail
Extensions).

Kod base64 zaprojektowano do reprezentowania określonej sekwencji
oktetów w formie, która nie musi być czytelna dla człowieka. Używany
jest 65-znakowy ([A-Za-z0-9+/=]) podzestaw z zestawu US-ASCII,
reprezentując każdy znak drukowalny sześcioma bitami.

Kod quoted-printable stosuje się do reprezentacji danych, które w
większości zawierają znaki drukowalne ASCII. Znaki niedrukowalne są
kodowane w triplety zawierające poprzedzone znakiem "=" dwie cyfry
szesnastkowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorarch}/MIME/Base64.pm
%{perl_vendorarch}/MIME/QuotedPrint.pm
%dir %{perl_vendorarch}/MIME
%dir %{perl_vendorarch}/auto/MIME
%dir %{perl_vendorarch}/auto/MIME/Base64
%{perl_vendorarch}/auto/MIME/Base64/Base64.bs
%attr(755,root,root) %{perl_vendorarch}/auto/MIME/Base64/Base64.so
%{_mandir}/man3/MIME::Base64.3pm*
%{_mandir}/man3/MIME::QuotedPrint.3pm*
