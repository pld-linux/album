%include	/usr/lib/rpm/macros.perl
Summary:	HTML photo album generator
Summary(pl):	Generator albumów fotograficznych w HTML-u
Name:		album
Version:	3.07
Release:	1
License:	distributable
Group:		Applications/Graphics
Source0:	http://marginalhacks.com/bin/%{name}.tar.gz
# Source0-md5:	a874e2ca14bb808308c63140862c8e16
URL:		http://marginalhacks.com/Hacks/album/
BuildArch:	noarch
BuildRequires:	rpm-perlprov >= 3.0.3-18
Requires:	ImageMagick
%requires_eq	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML photo album generator that supports themes. It takes a
directory of images and creates all the thumbnails and HTML that you
need. It's fast, easy to use, and very powerful.
Features:
- You can use themes to choose or redesign the album "look and feel."
- Recursively descends directories to make a hierarchy of photo albums
- Maintains aspect ratio while constraining size of thumbnails

%description -l pl
Generator albumów fotograficznych z obs³ug± motywów. Przyjmuje katalog
ze zdjêciami i tworzy wszystkie potrzebne miniaturki oraz pliki HTML.
Jest szybki, prosty w u¿yciu i ma du¿e mo¿liwo¶ci.
Mo¿liwo¶ci:
- pozwala na u¿ywanie motywów do wybrania lub zmiany "look and feel"
  albumu
- rekurencyjnie przegl±da katalogi tworz±c hierarchiê albumów
  fotograficznych
- zachowuje proporcje przy ograniczaniu rozmiaru miniaturek.

%prep
%setup -q
REAL_VERSION=`./album --version 2>&1 | grep '^This' | awk '/This\ is\ album/ { print $4 }'`
if [ "$REAL_VERSION" != "v%{version}" ] ; then
	echo "Package/Source version mismatch!"
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install album $RPM_BUILD_ROOT%{_bindir}
install album.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Docs/* License.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
