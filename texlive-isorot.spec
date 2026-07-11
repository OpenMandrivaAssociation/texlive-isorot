%global tl_name isorot
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Rotation of document elements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/isorot
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/isorot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is for rotation of document elements. It is a combination of
the lscape package and an extension of the rotating package. The package
is designed for use with the iso class but may be used with any normal
class.

