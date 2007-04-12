%define module	Net-Proxy
%define	name	perl-%{module}
%define	version	0.06
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Framework for proxying network connections in many ways
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(LWP::UserAgent)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%doc README Changes
%{perl_vendorlib}/Net
%{_mandir}/*/*
%{_bindir}/*
