#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-photos
Version  : 3.28.0
Release  : 3
URL      : https://download.gnome.org/sources/gnome-photos/3.28/gnome-photos-3.28.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-photos/3.28/gnome-photos-3.28.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-photos-bin
Requires: gnome-photos-data
Requires: gnome-photos-doc
Requires: gnome-photos-locales
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
BuildRequires : pkgconfig(geocode-glib-1.0)
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk+-unix-print-3.0)
BuildRequires : pkgconfig(libdazzle-1.0)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libgfbgraph-0.2)
BuildRequires : pkgconfig(libpng16)
BuildRequires : pkgconfig(tracker-control-2.0)
BuildRequires : pkgconfig(tracker-sparql-2.0)
BuildRequires : pygobject-python

%description
Photos - access, organize and share your photos on GNOME
========================================================

%package bin
Summary: bin components for the gnome-photos package.
Group: Binaries
Requires: gnome-photos-data

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


%package locales
Summary: locales components for the gnome-photos package.
Group: Default

%description locales
locales components for the gnome-photos package.


%prep
%setup -q -n gnome-photos-3.28.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523770775
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1523770775
rm -rf %{buildroot}
%make_install
%find_lang gnome-photos

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-photos
/usr/libexec/gnome-photos-thumbnailer

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Photos.desktop
/usr/share/dbus-1/services/org.gnome.Photos.service
/usr/share/glib-2.0/schemas/org.gnome.photos.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Photos.search-provider.ini
/usr/share/icons/hicolor/16x16/apps/org.gnome.Photos.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.Photos.png
/usr/share/icons/hicolor/24x24/apps/org.gnome.Photos.png
/usr/share/icons/hicolor/256x256/apps/org.gnome.Photos.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.Photos.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.Photos.png
/usr/share/icons/hicolor/scalable/apps/org.gnome.Photos-symbolic.svg
/usr/share/metainfo/org.gnome.Photos.appdata.xml

%files doc
%defattr(-,root,root,-)
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

%files locales -f gnome-photos.lang
%defattr(-,root,root,-)

