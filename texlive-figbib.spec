# revision 19388
# category Package
# catalog-ctan /macros/latex/contrib/figbib
# catalog-date 2006-10-19 22:42:58 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-figbib
Version:	20061019
Release:	5
Summary:	Organize figure databases with BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/figbib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figbib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/figbib.doc.tar.xz
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
%{_texmfdistdir}/bibtex/bst/figbib/figbib.bst
%{_texmfdistdir}/bibtex/bst/figbib/figbib1.bst
%{_texmfdistdir}/tex/latex/figbib/figbib.sty
%doc %{_texmfdistdir}/doc/latex/figbib/README
%doc %{_texmfdistdir}/doc/latex/figbib/figbib_doc.pdf
%doc %{_texmfdistdir}/doc/latex/figbib/figbib_doc.tex
%doc %{_texmfdistdir}/doc/latex/figbib/figbib_sample.bib
%doc %{_texmfdistdir}/doc/latex/figbib/figbib_sample.pdf
%doc %{_texmfdistdir}/doc/latex/figbib/figbib_sample.tex
%doc %{_texmfdistdir}/doc/latex/figbib/smiley.eps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061019-2
+ Revision: 751837
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061019-1
+ Revision: 718434
- texlive-figbib
- texlive-figbib
- texlive-figbib
- texlive-figbib

