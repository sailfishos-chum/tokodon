Name:           tokodon
Version:        23.04.2
Release:        1%{?dist}
License:        GPLv3 and CC0 and BSD and LGPLv2+ and GPLv3+ and GPLv2
# For a breakdown of the licensing, see PACKAGE-LICENSING
Summary:        Kirigami-based mastodon client
Url:            https://invent.kde.org/network/tokodon
Source0:        %{name}-%{version}.tar.bz2
Source1:        org.kde.tokodon-86.png
Source2:        org.kde.tokodon-108.png
Source3:        org.kde.tokodon-128.png
Source4:        org.kde.tokodon-256.png

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  opt-kf5-kconfig-devel
BuildRequires:  opt-kf5-kcoreaddons-devel
BuildRequires:  opt-kf5-kdbusaddons-devel
BuildRequires:  opt-kf5-ki18n-devel
BuildRequires:  opt-kf5-kio-devel
BuildRequires:  opt-kf5-kirigami2-devel
BuildRequires:  opt-kf5-kirigami-addons
BuildRequires:  opt-kf5-knotifications-devel
BuildRequires:  opt-kf5-kwindowsystem-devel
BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qtkeychain-devel
BuildRequires:  opt-qt5-qtmultimedia-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel
BuildRequires:  opt-qt5-qtsvg-devel
BuildRequires:  opt-qt5-qtwebsockets-devel

Requires:       opt-kf5-kirigami2
Requires:       opt-kf5-kirigami-addons
Requires:       qt-runner
Requires:       opt-qt5-qtmultimedia
Requires:       opt-qt5-qtwebsockets

%{?opt_kf5_default_filter}

%description
Tokodon is a Mastodon client for Plasma and Plasma Mobile.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
%make_build
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

#Rmove the appsteam metadata file
rm %{buildroot}/usr/share/metainfo/org.kde.tokodon.appdata.xml

# copy icons
install -p -m644 -D %{SOURCE1} \
	%{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE2} \
	%{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE3} \
	%{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/org.kde.%{name}.png
install -p -m644 -D %{SOURCE4} \
	%{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/org.kde.%{name}.png


%files
%doc README.md
%license LICENSES/
%{_bindir}/%{name}
%{_datadir}/locale/
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_datadir}/knotifications5/tokodon.notifyrc
%{_datadir}/qlogging-categories5/tokodon.categories
