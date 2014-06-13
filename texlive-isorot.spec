# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/isorot
# catalog-date 2007-01-08 13:31:52 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-isorot
Version:	20070108
Release:	7
Summary:	Rotation of document elements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/isorot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070108-2
+ Revision: 752823
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070108-1
+ Revision: 718740
- texlive-isorot
- texlive-isorot
- texlive-isorot
- texlive-isorot

