Name:           openclipart
Version:        0.18
Release:        1
Summary:        Open Clip Art Library
Group:          Graphics
License:        CC0
URL:            http://www.openclipart.org/
Source0:        http://www.openclipart.org/downloads/%{version}/openclipart-%{version}-svgonly.tar.bz2
# make linting happy
Source100:	openclipart.rpmlintrc
BuildRequires:  dos2unix
BuildArch:      noarch

%description
Openclipart Gallery contains thousand of SVG vector images that can be
freely used. SVG files can be opened in various tools including
Inkscape vector graphics editor, OpenOffice.org and Firefox web browser.


%prep
%setup -q -n openclipart-%{version}-svgonly
find . -name '*.svg' -exec dos2unix -k -q '{}' \;


%build
# nothing

%install
cd clipart
find . -name '*.svg' -exec sh -c '
        DIR="%{buildroot}%{_datadir}/clipart/%{name}/$(dirname "{}")";
        install -d "$DIR";
        install -m 644 "{}" "$DIR"' \;


%files
%doc AUTHORS ChangeLog NEWS README VERSION
%{_datadir}/clipart


