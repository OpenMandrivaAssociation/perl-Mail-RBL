%define	upstream_name	 Mail-RBL
%define	upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension to access RBL-style host verification services
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(NetAddr::IP)
BuildRequires:	perl(Net::DNS)
BuildArch:	noarch

%description
This module eases the task of checking if a given host is in the list. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# some RBL can't be queries from build host
export SKIP_RBL_TESTS=1
make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Mail
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 403843
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.10-4mdv2009.0
+ Revision: 257692
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.10-3mdv2009.0
+ Revision: 245778
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.10-1mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2008.0
+ Revision: 48616
- update to new version 1.10
- skip RBL tests


* Mon Dec 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2007.0
+ Revision: 94825
- new version
- Import perl-Mail-RBL

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-4mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.04-3mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.04-2mdk
- Add BuildRequires

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdk
- new version 
- spec cleanup
- fix directory ownership
- re-enale tests

* Tue Jul 05 2005 Oden Eriksson <oeriksson@mandriva.com> 1.02-2mdk
- rebuild

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.02-1mdk
- 1.02
- disable test for now
- cosmetics

