%global tl_name figbib
%global tl_revision 19388

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Organize figure databases with BibTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/figbib
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figbib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/figbib.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
FigBib lets you organize your figures in BibTeX databases. Some FigBib
features are: Store and manage figures in a BibTeX database; Include
figures in your LaTeX document with one short command; Generate a List
of Figures containing more/other information than the figure captions;
Control with one switch where to output the figures, either as usual
float objects or in a separate part at the end of your document.

