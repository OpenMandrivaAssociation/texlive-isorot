Name:		texlive-isorot
Version:	15878
Release:	2
Summary:	Rotation of document elements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isorot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The isorot package is for rotation of document elements. It is
a combination of the lscape package and an extension of the
rotating package. The package is designed for use with the iso
class but may be used with any normal class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/isorot/isorot.sty
%doc %{_texmfdistdir}/doc/latex/isorot/README
%doc %{_texmfdistdir}/doc/latex/isorot/rotman.pdf
%doc %{_texmfdistdir}/doc/latex/isorot/rotman.tex
#- source
%doc %{_texmfdistdir}/source/latex/isorot/isorot.dtx
%doc %{_texmfdistdir}/source/latex/isorot/isorot.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
