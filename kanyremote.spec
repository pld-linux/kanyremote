Summary:	kanyremote - bluetooth remote for KDE
Summary(pl.UTF-8):	kanyremote - pilot bluetooth dla KDE
Name:		kanyremote
Version:	2.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
# Source0-md5:	0fdce52c32d5eb37a405de3f583c2090
Patch0:		%{name}-autotools.patch
URL:		http://anyremote.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The overall goal of this project is to provide wireless Bluetooth or
InfraRed remote control service for KDE. In contrast with other
Bluetooth remote control programs kAnyRemote is not limited to
SonyEricsson or JSR-82 capable phones. It was developed as just thin
"communication" layer beetween bluetooth-capabled phone and Linux, and
in principle could be configured to manage any software. But Bluetooth
is not the only way to use it. kAnyRemote could be used with:
- IR-capabled phone
- with cable connection
- it could accept incoming connection from network
- it could work with Java client written for JSR82 capabled phones
  (like Bemused)
- it have limited support for existing Bemused clients.

AnyRemote is its console equivalent (you can find it in anyremote
package).

%description -l pl.UTF-8
Ogólnym celem tego projektu jest dostarczenie zdalnego,
bezprzewodowego systemu kontroli nad Linuksem z użyciem Bluetootha lub
podczerwieni (IrDA). W odróżnieniu od innych programów tego typu
kAnyRemote nie jest ograniczony do obsługi telefonów SonyEricssona czy
JSR-82. Został zaprojektowany jako cienka warstwa "komunikacyjna"
między telefonem posiadającym Bluetooth, a Linuksem i w zasadzie może
zostać skonfigurowany do obsługi każdej aplikacji. Połączenia
Bluetooth nie są jedynym sposobem by korzystać z programu. kAnyRemote
może być używany wraz z:
- telefonami posiadającymi podczerwień (IrDA)
- telefonami z połączeniem kablowym
- może odbierać połączenia przychodzące z sieci
- klientem Javy napisanym dla telefonów obsługujących JSR82 (jak
  Bemused)
- już istniejącymi klientami Bemused (częściowa obsługa).

Jego konsolowym odpowiednikiem jest AnyRemote (można go znaleźć w
pakiecie anyremote).

%prep
%setup -q
%patch0 -p0

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}/kde}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities,%{_desktopdir}/kde}/kanyremote.desktop

install src/pix/kanyremote*.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/kanyremote
%{_datadir}/apps/kanyremote
%{_desktopdir}/kde/kanyremote.desktop
%{_pixmapsdir}/kanyremote*.png
