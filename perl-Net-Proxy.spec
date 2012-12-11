%define upstream_name	 Net-Proxy
%define	upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Framework for proxying network connections in many ways
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::Pod)
BuildArch:	noarch

%description
A Net::Proxy object represents a proxy that accepts connections and then relays
the data transfered between the source and the destination.
The goal of this module is to abstract the different methods used to connect 
from the proxy to the destination.

A proxy is a program that transfer data across a network boundary between a 
client and a server. Net::Proxy introduces the concept of "connectors" 
(implemented as Net::Proxy::Connector subclasses), which abstract the server 
part (connected to the client) and the client part (connected to the server) 
of the proxy.
This architecture makes it easy to implement specific techniques to cross a 
given network boundary, possibly by using a proxy on one side of the network 
fence, and a reverse-proxy on the other side of the fence.

This package also contains utilities such as connect-tunnel and sslh.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Net
%{_mandir}/*/*
%{_bindir}/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 406173
- rebuild using %%perl_convert_version

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.12-1mdv2009.0
+ Revision: 140693
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2008.1
+ Revision: 104564
- update to new version 0.12

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.1
+ Revision: 97520
- update to new version 0.10

* Tue May 01 2007 Michael Scherer <misc@mandriva.org> 0.08-1mdv2008.0
+ Revision: 19962
- add missing BuildRequires
- update to 0.08


* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.0
- New release 0.06
- spec cleanup
- fix directory ownership

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Tue Apr 18 2006 Michael Scherer <misc@mandriva.org> 0.05-1mdk
- New release 0.05

* Tue Mar 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- Add BuildRequires

* Fri Feb 03 2006 Michael Scherer <misc@mandriva.org> 0.04-1mdk
- First Mandriva package

