Summary:	squidwall - a fast and secure redirector for squid
Name:		squidwall
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.mcmilk.de/projects/squidwall/dl/%{name}-%{version}.tar.bz2
# Source0-md5:	4ce33f8eda6201faaf9b49cc1b32359e
Patch0:		%{name}-Makefile.patch
URL:		http://www.mcmilk.de/projects/squidwall/
BuildRequires:	libowfat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squidwall is a fast, small, and secure squid redirector. It is written
with security in mind. It enables the administrator to build an easy
to use Web interface for controlling user-, host-, or IP-based access
to squid. It also does pass-through antivirus scanning with clamav.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/var/log/squid

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(711,squid,squid) %{_bindir}/*
%attr(600,squid,squid) /var/log/squid/squidwall.log
