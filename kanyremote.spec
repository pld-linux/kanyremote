Summary:	kanyremote - bluetooth remote for KDE
Summary(pl.UTF-8):	kanyremote - pilot bluetooth dla KDE
Name:		kanyremote
Version:	5.12
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
# Source0-md5:	1871cc2df33b7e4928a14585e5f64bbe
URL:		http://anyremote.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	kde4-kdelibs-devel >= 4.3
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	python-PyKDE4
Requires:	python-bluetooth
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

%build
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

# fix locale names
mv $RPM_BUILD_ROOT%{_datadir}/locale/cs{_CZ,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/de{_DE,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/es{_ES,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/fi{_FI,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/fr{_FR,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/hu{_HU,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/it{_IT,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/nl{_NL,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/pl{_PL,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/ru{_RU,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/sk{_SK,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/sv{_SE,}

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/kanyremote
%{_desktopdir}/kanyremote.desktop
%{_pixmapsdir}/kanyremote*.png
%{_pixmapsdir}/kanyremote*.svg
