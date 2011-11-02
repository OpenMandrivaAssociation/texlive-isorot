Name:		texlive-isorot
Version:	20070108
Release:	1
Summary:	Rotation of document elements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isorot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The isorot package is for rotation of document elements. It is
a combination of the lscape package and an extension of the
rotating package. The package is designed for use with the iso
class but may be used with any normal class.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
