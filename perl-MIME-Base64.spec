Summary:	Perl MIME-Base64 module
Summary(pl):	Modu³ Perla MIME-Base64
Name:		perl-MIME-Base64
Version:	2.11
Release:	3
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME-Base64-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Provides access to the MIME Base64 algorithm.

%description -l pl
Modu³ perla wspomagaj±cy algorytm MIME Base64.

%prep
%setup -q -n MIME-Base64-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

make install \
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
