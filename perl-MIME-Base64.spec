%include	/usr/lib/rpm/macros.perl
Summary:	Perl MIME-Base64 module
Summary(pl):	Modu³ Perla MIME-Base64
Name:		perl-MIME-Base64
Version:	2.11
Release:	4
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME-Base64-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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

%prep
%setup -q -n MIME-Base64-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/MIME/Base64/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

strip --strip-unneeded $RPM_BUILD_ROOT%{perl_sitearch}/auto/*/*/*.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/MIME/*.pm

%dir %{perl_sitearch}/auto/MIME/Base64

%{perl_sitearch}/auto/MIME/Base64/*.bs
%{perl_sitearch}/auto/MIME/Base64/.packlist
%attr(755,root,root) %{perl_sitearch}/auto/MIME/Base64/*.so

%{_mandir}/man3/*
