%include	/usr/lib/rpm/macros.perl
Summary:	HTML photo album generator
Summary(pl):	Generator album�w foto
Name:		album
Version:	2.35
Release:	1
License:	distributable
Group:		Applications/Graphics
Source0:	http://marginalhacks.com/bin/%{name}.tar.gz
Patch0:		%{name}-OS.patch
URL:		http://marginalhacks.com/Hacks/album/
Buildarch:	noarch
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


%prep
%setup -qc %{name}-%{version}
REAL_VERSION=`./album --version | awk '/album version/ { print $5 }'`
if [ "$REAL_VERSION" != "%{version}" ] ; then
	echo "Package/Source version mismatch!"
	exit 1
fi
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install album caption_index  $RPM_BUILD_ROOT%{_bindir}
cp -R Themes $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
