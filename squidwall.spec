# TODO: optflags
Summary:	squidwall - a fast and secure redirector for squid
Summary(pl.UTF-8):   squidwall - szybkie i bezpieczne przekierowywanie dla squida
Name:		squidwall
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.mcmilk.de/projects/squidwall/dl/%{name}-%{version}.tar.bz2
# Source0-md5:	ba09f24ed8a894d560fc2d1bdcdeed43
Patch0:		%{name}-Makefile.patch
URL:		http://www.mcmilk.de/projects/squidwall/
BuildRequires:	libowfat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Squidwall is a fast, small, and secure squid redirector. It is written
with security in mind. It enables the administrator to build an easy
to use Web interface for controlling user-, host-, or IP-based access
to squid. It also does pass-through antivirus scanning with clamav.

%description -l pl.UTF-8
Squidwall to szybkie, małe i bezpieczne narzędzie do przekierowywania
dla squida. Jest napisane z myślą o bezpieczeństwie. Umożliwia
administratorowi stworzenie łatwego w użyciu interfejsu WWW do
sterowania dostępem do squida w oparciu o użytkownika, host lub IP.
Wykonuje także przezroczyste skanowanie antywirusowe przy użyciu
clamava.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/var/log/squid}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(600,squid,squid) /var/log/squid/squidwall.log
