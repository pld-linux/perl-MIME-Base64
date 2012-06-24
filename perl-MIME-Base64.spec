Summary:	Perl MIME-Base64 module
Summary(pl):	Modu� Perla MIME-Base64
Name:		perl-MIME-Base64
Version:	2.11
Release:	0.1
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/MIME-Base64-%{version}.tar.gz
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Provides access to the MIME Base64 algorithm.

%description -l pl
Modu� perla wspomagaj�cy algorytm MIME Base64.

%prep
%setup -q -n MIME-Base64-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_sitearch} \
	$RPM_BUILD_ROOT%{_mandir}/man3 \
	$RPM_BUILD_ROOT/%{perl_archlib}

make \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
	install

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/MIME/Base64/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/MIME

%dir %{perl_sitearch}/auto/MIME
%dir %{perl_sitearch}/auto/MIME/Base64

%{perl_sitearch}/auto/*/*/*.bs
%{perl_sitearch}/auto/*/*/.packlist
%attr(755,root,root) %{perl_sitearch}/auto/*/*/*.so

%{_mandir}/man3/*
