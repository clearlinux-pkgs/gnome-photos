#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-photos
Version  : 3.34.1
Release  : 19
URL      : https://download.gnome.org/sources/gnome-photos/3.34/gnome-photos-3.34.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-photos/3.34/gnome-photos-3.34.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-photos-bin = %{version}-%{release}
Requires: gnome-photos-data = %{version}-%{release}
Requires: gnome-photos-lib = %{version}-%{release}
Requires: gnome-photos-libexec = %{version}-%{release}
Requires: gnome-photos-license = %{version}-%{release}
Requires: gnome-photos-locales = %{version}-%{release}
Requires: tracker-miners-data
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : gdk-pixbuf
BuildRequires : gegl-dev
BuildRequires : gettext
BuildRequires : gexiv2-dev
BuildRequires : itstool
BuildRequires : libjpeg-turbo-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(babl)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gegl-0.4)
BuildRequires : pkgconfig(geocode-glib-1.0)
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk+-unix-print-3.0)
BuildRequires : pkgconfig(libdazzle-1.0)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libgfbgraph-0.2)
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(libpng16)
BuildRequires : pkgconfig(tracker-control-2.0)
BuildRequires : pkgconfig(tracker-sparql-2.0)
BuildRequires : pygobject-python
BuildRequires : yelp-tools-dev

%description
Photos - access, organize and share your photos on GNOME
========================================================

%package bin
Summary: bin components for the gnome-photos package.
Group: Binaries
Requires: gnome-photos-data = %{version}-%{release}
Requires: gnome-photos-libexec = %{version}-%{release}
Requires: gnome-photos-license = %{version}-%{release}

%description bin
bin components for the gnome-photos package.


%package data
Summary: data components for the gnome-photos package.
Group: Data

%description data
data components for the gnome-photos package.


%package doc
Summary: doc components for the gnome-photos package.
Group: Documentation

%description doc
doc components for the gnome-photos package.


%package lib
Summary: lib components for the gnome-photos package.
Group: Libraries
Requires: gnome-photos-data = %{version}-%{release}
Requires: gnome-photos-libexec = %{version}-%{release}
Requires: gnome-photos-license = %{version}-%{release}

%description lib
lib components for the gnome-photos package.


%package libexec
Summary: libexec components for the gnome-photos package.
Group: Default
Requires: gnome-photos-license = %{version}-%{release}

%description libexec
libexec components for the gnome-photos package.


%package license
Summary: license components for the gnome-photos package.
Group: Default

%description license
license components for the gnome-photos package.


%package locales
Summary: locales components for the gnome-photos package.
Group: Default

%description locales
locales components for the gnome-photos package.


%prep
%setup -q -n gnome-photos-3.34.1
cd %{_builddir}/gnome-photos-3.34.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584970538
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-photos
cp %{_builddir}/gnome-photos-3.34.1/COPYING %{buildroot}/usr/share/package-licenses/gnome-photos/31a3d460bb3c7d98845187c716a30db81c44b615
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-photos

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-photos

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Photos.desktop
/usr/share/dbus-1/services/org.gnome.Photos.service
/usr/share/glib-2.0/schemas/org.gnome.photos.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Photos.search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Photos.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Photos-symbolic.svg
/usr/share/metainfo/org.gnome.Photos.appdata.xml

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gnome\-photos/*
/usr/share/help/C/gnome-photos/favorites-set.page
/usr/share/help/C/gnome-photos/favorites.page
/usr/share/help/C/gnome-photos/index.page
/usr/share/help/C/gnome-photos/legal.xml
/usr/share/help/C/gnome-photos/media/logo1.png
/usr/share/help/C/gnome-photos/view-album.page
/usr/share/help/C/gnome-photos/view-favorites.page
/usr/share/help/C/gnome-photos/view-photos.page
/usr/share/help/C/gnome-photos/view.page
/usr/share/help/ca/gnome-photos/favorites-set.page
/usr/share/help/ca/gnome-photos/favorites.page
/usr/share/help/ca/gnome-photos/index.page
/usr/share/help/ca/gnome-photos/legal.xml
/usr/share/help/ca/gnome-photos/media/logo1.png
/usr/share/help/ca/gnome-photos/view-album.page
/usr/share/help/ca/gnome-photos/view-favorites.page
/usr/share/help/ca/gnome-photos/view-photos.page
/usr/share/help/ca/gnome-photos/view.page
/usr/share/help/cs/gnome-photos/favorites-set.page
/usr/share/help/cs/gnome-photos/favorites.page
/usr/share/help/cs/gnome-photos/index.page
/usr/share/help/cs/gnome-photos/legal.xml
/usr/share/help/cs/gnome-photos/media/logo1.png
/usr/share/help/cs/gnome-photos/view-album.page
/usr/share/help/cs/gnome-photos/view-favorites.page
/usr/share/help/cs/gnome-photos/view-photos.page
/usr/share/help/cs/gnome-photos/view.page
/usr/share/help/da/gnome-photos/favorites-set.page
/usr/share/help/da/gnome-photos/favorites.page
/usr/share/help/da/gnome-photos/index.page
/usr/share/help/da/gnome-photos/legal.xml
/usr/share/help/da/gnome-photos/media/logo1.png
/usr/share/help/da/gnome-photos/view-album.page
/usr/share/help/da/gnome-photos/view-favorites.page
/usr/share/help/da/gnome-photos/view-photos.page
/usr/share/help/da/gnome-photos/view.page
/usr/share/help/de/gnome-photos/favorites-set.page
/usr/share/help/de/gnome-photos/favorites.page
/usr/share/help/de/gnome-photos/index.page
/usr/share/help/de/gnome-photos/legal.xml
/usr/share/help/de/gnome-photos/media/logo1.png
/usr/share/help/de/gnome-photos/view-album.page
/usr/share/help/de/gnome-photos/view-favorites.page
/usr/share/help/de/gnome-photos/view-photos.page
/usr/share/help/de/gnome-photos/view.page
/usr/share/help/el/gnome-photos/favorites-set.page
/usr/share/help/el/gnome-photos/favorites.page
/usr/share/help/el/gnome-photos/index.page
/usr/share/help/el/gnome-photos/legal.xml
/usr/share/help/el/gnome-photos/media/logo1.png
/usr/share/help/el/gnome-photos/view-album.page
/usr/share/help/el/gnome-photos/view-favorites.page
/usr/share/help/el/gnome-photos/view-photos.page
/usr/share/help/el/gnome-photos/view.page
/usr/share/help/es/gnome-photos/favorites-set.page
/usr/share/help/es/gnome-photos/favorites.page
/usr/share/help/es/gnome-photos/index.page
/usr/share/help/es/gnome-photos/legal.xml
/usr/share/help/es/gnome-photos/media/logo1.png
/usr/share/help/es/gnome-photos/view-album.page
/usr/share/help/es/gnome-photos/view-favorites.page
/usr/share/help/es/gnome-photos/view-photos.page
/usr/share/help/es/gnome-photos/view.page
/usr/share/help/fr/gnome-photos/favorites-set.page
/usr/share/help/fr/gnome-photos/favorites.page
/usr/share/help/fr/gnome-photos/index.page
/usr/share/help/fr/gnome-photos/legal.xml
/usr/share/help/fr/gnome-photos/media/logo1.png
/usr/share/help/fr/gnome-photos/view-album.page
/usr/share/help/fr/gnome-photos/view-favorites.page
/usr/share/help/fr/gnome-photos/view-photos.page
/usr/share/help/fr/gnome-photos/view.page
/usr/share/help/fur/gnome-photos/favorites-set.page
/usr/share/help/fur/gnome-photos/favorites.page
/usr/share/help/fur/gnome-photos/index.page
/usr/share/help/fur/gnome-photos/legal.xml
/usr/share/help/fur/gnome-photos/media/logo1.png
/usr/share/help/fur/gnome-photos/view-album.page
/usr/share/help/fur/gnome-photos/view-favorites.page
/usr/share/help/fur/gnome-photos/view-photos.page
/usr/share/help/fur/gnome-photos/view.page
/usr/share/help/gl/gnome-photos/favorites-set.page
/usr/share/help/gl/gnome-photos/favorites.page
/usr/share/help/gl/gnome-photos/index.page
/usr/share/help/gl/gnome-photos/legal.xml
/usr/share/help/gl/gnome-photos/media/logo1.png
/usr/share/help/gl/gnome-photos/view-album.page
/usr/share/help/gl/gnome-photos/view-favorites.page
/usr/share/help/gl/gnome-photos/view-photos.page
/usr/share/help/gl/gnome-photos/view.page
/usr/share/help/hu/gnome-photos/favorites-set.page
/usr/share/help/hu/gnome-photos/favorites.page
/usr/share/help/hu/gnome-photos/index.page
/usr/share/help/hu/gnome-photos/legal.xml
/usr/share/help/hu/gnome-photos/media/logo1.png
/usr/share/help/hu/gnome-photos/view-album.page
/usr/share/help/hu/gnome-photos/view-favorites.page
/usr/share/help/hu/gnome-photos/view-photos.page
/usr/share/help/hu/gnome-photos/view.page
/usr/share/help/ko/gnome-photos/favorites-set.page
/usr/share/help/ko/gnome-photos/favorites.page
/usr/share/help/ko/gnome-photos/index.page
/usr/share/help/ko/gnome-photos/legal.xml
/usr/share/help/ko/gnome-photos/media/logo1.png
/usr/share/help/ko/gnome-photos/view-album.page
/usr/share/help/ko/gnome-photos/view-favorites.page
/usr/share/help/ko/gnome-photos/view-photos.page
/usr/share/help/ko/gnome-photos/view.page
/usr/share/help/nl/gnome-photos/favorites-set.page
/usr/share/help/nl/gnome-photos/favorites.page
/usr/share/help/nl/gnome-photos/index.page
/usr/share/help/nl/gnome-photos/legal.xml
/usr/share/help/nl/gnome-photos/media/logo1.png
/usr/share/help/nl/gnome-photos/view-album.page
/usr/share/help/nl/gnome-photos/view-favorites.page
/usr/share/help/nl/gnome-photos/view-photos.page
/usr/share/help/nl/gnome-photos/view.page
/usr/share/help/pl/gnome-photos/favorites-set.page
/usr/share/help/pl/gnome-photos/favorites.page
/usr/share/help/pl/gnome-photos/index.page
/usr/share/help/pl/gnome-photos/legal.xml
/usr/share/help/pl/gnome-photos/media/logo1.png
/usr/share/help/pl/gnome-photos/view-album.page
/usr/share/help/pl/gnome-photos/view-favorites.page
/usr/share/help/pl/gnome-photos/view-photos.page
/usr/share/help/pl/gnome-photos/view.page
/usr/share/help/pt_BR/gnome-photos/favorites-set.page
/usr/share/help/pt_BR/gnome-photos/favorites.page
/usr/share/help/pt_BR/gnome-photos/index.page
/usr/share/help/pt_BR/gnome-photos/legal.xml
/usr/share/help/pt_BR/gnome-photos/media/logo1.png
/usr/share/help/pt_BR/gnome-photos/view-album.page
/usr/share/help/pt_BR/gnome-photos/view-favorites.page
/usr/share/help/pt_BR/gnome-photos/view-photos.page
/usr/share/help/pt_BR/gnome-photos/view.page
/usr/share/help/ro/gnome-photos/favorites-set.page
/usr/share/help/ro/gnome-photos/favorites.page
/usr/share/help/ro/gnome-photos/index.page
/usr/share/help/ro/gnome-photos/legal.xml
/usr/share/help/ro/gnome-photos/media/logo1.png
/usr/share/help/ro/gnome-photos/view-album.page
/usr/share/help/ro/gnome-photos/view-favorites.page
/usr/share/help/ro/gnome-photos/view-photos.page
/usr/share/help/ro/gnome-photos/view.page
/usr/share/help/sv/gnome-photos/favorites-set.page
/usr/share/help/sv/gnome-photos/favorites.page
/usr/share/help/sv/gnome-photos/index.page
/usr/share/help/sv/gnome-photos/legal.xml
/usr/share/help/sv/gnome-photos/media/logo1.png
/usr/share/help/sv/gnome-photos/view-album.page
/usr/share/help/sv/gnome-photos/view-favorites.page
/usr/share/help/sv/gnome-photos/view-photos.page
/usr/share/help/sv/gnome-photos/view.page

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-photos/libgnome-photos.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-photos-thumbnailer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-photos/31a3d460bb3c7d98845187c716a30db81c44b615

%files locales -f gnome-photos.lang
%defattr(-,root,root,-)

