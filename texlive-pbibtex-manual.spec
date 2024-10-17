Name:		texlive-pbibtex-manual
Version:	66181
Release:	1
Summary:	Documentation files for (u)pBibTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pbibtex-manual
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbibtex-manual.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pbibtex-manual.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains documentation files for Japanese pBibTeX
and upBibTeX. For historical reasons, this also contains old
documentation files for JBibTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/pbibtex-manual

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
