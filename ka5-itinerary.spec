#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		itinerary
Summary:	Itinerary and boarding pass management application
Name:		ka5-%{kaname}
Version:	22.08.1
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9ed78e3907cd282fa81b9c2f631dd778
URL:		https://community.kde.org/
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Location-devel
BuildRequires:	Qt5Network-devel >= 5.15.2
BuildRequires:	Qt5Positioning-devel >= 5.15.2
BuildRequires:	Qt5Qml-devel >= 5.15.2
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.5
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-kitinerary-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kosmindoormap-devel >= %{kdeappsver}
BuildRequires:	ka5-kpkpass-devel >= %{kdeappsver}
BuildRequires:	ka5-kpublictransport-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.88
BuildRequires:	kf5-karchive-devel >= 5.91.0
BuildRequires:	kf5-kauth-devel >= 5.93.0
BuildRequires:	kf5-kcalendarcore-devel >= 5.91.0
BuildRequires:	kf5-kcodecs-devel >= 5.93.0
BuildRequires:	kf5-kcompletion-devel >= 5.93.0
BuildRequires:	kf5-kconfig-devel >= 5.93.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.93.0
BuildRequires:	kf5-kcontacts-devel >= 5.91.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.93.0
BuildRequires:	kf5-kcrash-devel >= 5.88
BuildRequires:	kf5-kdbusaddons-devel >= 5.88
BuildRequires:	kf5-kholidays-devel >= 5.88
BuildRequires:	kf5-ki18n-devel >= 5.93.0
BuildRequires:	kf5-kio-devel >= 5.88
BuildRequires:	kf5-kitemviews-devel >= 5.93.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.93.0
BuildRequires:	kf5-knotifications-devel >= 5.88
BuildRequires:	kf5-kservice-devel >= 5.93.0
BuildRequires:	kf5-kunitconversion-devel >= 5.88
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.93.0
BuildRequires:	kf5-kxmlgui-devel >= 5.93.0
BuildRequires:	kf5-networkmanager-qt-devel >= 5.88
BuildRequires:	kf5-qqc2-desktop-style-devel >= 5.88
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	shared-mime-info >= 1.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Itinerary and boarding pass management application.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/itinerary
%attr(755,root,root) %{_libdir}/libSolidExtras.so
%attr(755,root,root) %{_libdir}/qt5/plugins/itinerarythumbnail.so
%dir %{_libdir}/qt5/qml/org/kde/solidextras
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/solidextras/libsolidextrasqmlplugin.so
%{_libdir}/qt5/qml/org/kde/solidextras/qmldir
%{_desktopdir}/org.kde.itinerary.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.itinerary.svg
%{_datadir}/knotifications5/itinerary.notifyrc
%{_datadir}/kservices5/itinerarythumbnail.desktop
%{_datadir}/metainfo/org.kde.itinerary.appdata.xml
%{_datadir}/qlogging-categories5/org_kde_itinerary.categories
%{_libdir}/qt5/plugins/kf5/kfilemetadata/kfilemetadata_itineraryextractor.so
%dir %{_libdir}/qt5/qml/org/kde/itinerary
%dir %{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons
%dir %{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/ClockElement.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/ClockFace.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/DateInput.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/DatePicker.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/DatePopup.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/DesktopDateInput.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/Hand.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/MobileDateInput.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/TimeInput.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/TimeLabel.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/TimePicker.qml
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/libitinerary-dateandtimeplugin.so
%{_libdir}/qt5/qml/org/kde/itinerary/kirigamiaddons/dateandtime/qmldir
