# revision 23239
# category Package
# catalog-ctan /macros/latex/contrib/moreenum
# catalog-date 2011-07-18 09:05:38 +0200
# catalog-license lppl1.3
# catalog-version 1.01
Name:		texlive-moreenum
Version:	1.01
Release:	1
Summary:	More enumeration options
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/moreenum
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreenum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/moreenum.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%{_texmfdistdir}/tex/latex/moreenum/moreenum.sty
%doc %{_texmfdistdir}/doc/latex/moreenum/README
%doc %{_texmfdistdir}/doc/latex/moreenum/testcase-moreenum.pdf
%doc %{_texmfdistdir}/doc/latex/moreenum/testcase-moreenum.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
