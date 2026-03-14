%global commit <LATEST_COMMIT_HASH> 
%global shortcommit %(c=%{commit}; echo ${c:0:7}) 
%global snapdate <YYYYMMDD>

Name:           hyprland
Version:        0.54.2
Release:        1%{?dist}
Summary:        A highly customizable dynamic tiling Wayland compositor

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/Hyprland
# We will use a locally generated tarball that includes the wlroots submodule
Source0:        https://github.com/hyprwm/Hyprland/releases/download/v%{version}/source-v%{version}.tar.gz

BuildRequires:  wayland-devel
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  glslang-devel
BuildRequires:  pixman-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libdrm-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  lcms2-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  git
BuildRequires:  udis86-devel
BuildRequires:  libuuid-devel
BuildRequires:  glib2-devel
BuildRequires:  re2-devel
BuildRequires:  muParser-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-errors-devel
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  libglvnd-devel
BuildRequires:  cmake
BuildRequires:  libX11-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel

# gdb is a runtime preference for debugging, but not strictly needed for building the package.
# gemini-3.1-pro cooked this and fixed it too.

%description
Hyprland is a dynamic tiling Wayland compositor that doesn't sacrifice on its looks.
This package is built with the required wlroots subprojects included.

%prep
# Extract the tarball
%autosetup -n Hyprland

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/Hyprland
%{_bindir}/hyprctl
%{_datadir}/wayland-sessions/hyprland.desktop
%{_datadir}/hyprland/
# Catch any other binary or shared data
%{_bindir}/*
%{_datadir}/*

%changelog
* Sat Mar 14 2026 noclog <noclog@example.com> - 0.54.2-1
- Initial Copr build fix
