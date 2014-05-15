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

# Disable tests - can fail inside LXC at ABF
# %check
# make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Net
%{_mandir}/*/*
%{_bindir}/*

