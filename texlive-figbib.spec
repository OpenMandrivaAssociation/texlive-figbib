Name:		texlive-figbib
Version:	19388
Release:	1
Summary:	Organize figure databases with BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/figbib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figbib.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
FigBib lets you organize your figures in BibTeX databases. Some
FigBib features are: - Store and manage figures in a BibTeX
database; - Include figures in your LaTeX document with one
short command; - Generate a List of Figures containing
more/other information than the figure captions; - Control with
one switch where to output the figures, either as usual float
objects or in a separate part at the end of your document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/figbib
%{_texmfdistdir}/tex/latex/figbib
%doc %{_texmfdistdir}/doc/latex/figbib

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
