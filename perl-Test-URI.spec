#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	URI
Summary:	Test::URI - Check Uniform Resource Identifiers
Summary(pl.UTF-8):	Test::URI - sprawdzanie URI (Uniform Resource Identifiers)
Name:		perl-Test-URI
Version:	1.087
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/B/BR/BRIANDFOY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0b2b50012aa21eeda851bf37170e4c8f
URL:		http://search.cpan.org/dist/Test-URI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-URI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check various parts of Uniform Resource Locators.

%description -l pl.UTF-8
Sprawdzanie różnych części URL-i (Uniform Resource Locators).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README.pod
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
