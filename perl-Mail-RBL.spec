%define	module	Mail-RBL
%define	name	perl-%{module}
%define	version	1.09
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension to access RBL-style host verification services
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(NetAddr::IP)
BuildRequires:  perl(Net::DNS)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module eases the task of checking if a given host is in the list. 

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Mail
%{_mandir}/*/*


