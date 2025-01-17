Name:		texlive-moreenum
Version:	24479
Release:	2
Summary:	More enumeration options
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/moreenum
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreenum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreenum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the following new enumerate styles: -
\greek for lowercase Greek letters; - \Greek for uppercase
Greek letters; - \enumHex for uppercase hexadecimal
enumeration; - \enumhex for lowercase hexadecimal enumeration;
- \enumbinary for binary enumeration; - \enumoctal for octal
enumeration; - \levelnth for "1st", "2nd", "3rd" etc., with the
"nth"s on the baseline; - raisenth for "1st", "2nd", "3rd"
etc., with the "nth"s raised; - \nthwords for "first",
"second", "third" etc.; - \Nthwords for "First", "Second",
"Third" etc.; - \NTHWORDS for "FIRST", "SECOND", "THIRD" etc.;
- \nwords for "one", "two", "three" etc.; - \Nwords for "One",
"Two", "Three" etc.; and - \NWORDS for "ONE", "TWO", "THREE"
etc. Each of these works with enumitem's "starred variant"
feature. So \begin{enumerate}[label=\enumhex*] will output a
hex enumerated list. Enumitem provides a start=0 option for
starting your enumerations at 0. The package requires amsmath,
alphalph, enumitem (of course), binhex and nth, all of which
are widely available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/moreenum/moreenum.sty
%doc %{_texmfdistdir}/doc/latex/moreenum/README
%doc %{_texmfdistdir}/doc/latex/moreenum/moreenum-doc.pdf
%doc %{_texmfdistdir}/doc/latex/moreenum/moreenum-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
