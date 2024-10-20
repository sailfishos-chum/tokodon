Name:           tokodon
Version:        24.08.2
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
Patch0:         0002-use-qtrunner.patch
Patch1:         0003-add-sailfish-support.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils

BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-ki18n-devel
#BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kirigami-addons-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtkeychain-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  mpv-devel
BuildRequires:  qt6-qtkeychain-devel
BuildRequires:  kf6-kitemmodels-devel
BuildRequires:  kf6-sonnet-devel
BuildRequires:  kf6-kcolorscheme-devel

Requires:       kf6-kirigami
Requires:       kf6-kirigami-addons
Requires:       qt-runner-qt6
Requires:       qt6-qtmultimedia
Requires:       qt6-qtwebsockets
Requires:       mpv
Requires:       qt6-qtkeychain
Requires:       kf6-purpose


%description
Tokodon is a Mastodon client for Plasma and Plasma Mobile.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 \
		-DSAILFISHOS=ON \
		-DUSE_QTMULTIMEDIA=YES
%cmake_build

%install
%cmake_install

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
