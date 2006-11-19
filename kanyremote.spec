Summary:	kanyremote - bluetooth remote for KDE
Summary(pl):	kanyremote - pilot bluetooth dla KDE
Name:		kanyremote
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
# Source0-md5:	2b35d41a9cd07801c344b92db77992c7
URL:		http://anyremote.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The overall goal of this project is to provide wireless Bluetooth or
InfraRed remote control service for KDE. In contrast with other
Bluetooth remote control programs kAnyRemote is not limited to
SonyEriccson or JSR-82 capable phones. It was developed as just thin
"communication" layer beetween bluetooth-capabled phone and Linux, and
in principle could be configured to manage any software. But Bluetooth
is not the only way to use it. kAnyRemote could be used with:
- IR-capabled phone
- with cable connection
- it could accept incoming connection from network
- it could work with Java client written for JSR82 capabled phones
  (like Bemused)
- it have limited support for existing Bemused clients.

AnyRemote is its console equivalent (you can find it in
anyremote.spec).

%description -l pl
Ogólnym celem tego projektu jest dostarczenie zdalnego,
bezprzewodowego systemu kontroli nad Linuksem z u¿yciem Bluetootha lub
podczerwieni (IrDA). W odró¿nieniu od innych programów tego typu
kAnyRemote nie jest ograniczony do obs³ugi telefonów SonyEriccsona czy
JSR-82. Zosta³ zaprojektowany jako cienka warstwa "komunikacyjna"
miêdzy telefonem posiadaj±cym Bluetooth, a Linuksem i w zasadzie mo¿e
zostaæ skonfigurowany do obs³ugi ka¿dej aplikacji. Po³±czenia
Bluetooth nie s± jedynym sposobem by korzystaæ z programu. kAnyRemote
mo¿e byæ u¿ywany wraz z:
- telefonami posiadaj±cymi podczerwieñ (IrDA)
- telefonami z po³±czeniem kablowym
- mo¿e odbieraæ po³±czenia przychodz±ce z sieci
- clientem Javy napisanym dla telefonów obs³uguj±cych JSR82 (jak
  Bemused)
- z ju¿ istniej±cymi klientami Bemused (czê¶ciowa obs³uga).

Jego konsolowym odpowiednikiem jest AnyRemote (mo¿esz go znale¼æ w
anyremote.spec).

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kanyremote
%{_datadir}/applnk/Utilities/kanyremote.desktop
%{_datadir}/apps/kanyremote/kanyremoteui.rc
%{_iconsdir}/*/*/apps/kanyremote*.png
