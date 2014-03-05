%define texmfdir %{_datadir}/texmf-dist
%define updmap %{texmfdir}/fonts/map/dvips/updmap

Summary:	Files for processing Hebrew LaTeX documents
Name:		ivritex
Version:	1.2.1
Release:	5
License:	LPPL
Group:		Publishing
Url:		http://ivritex.sourceforge.net/
Source0:	http://downloads.sourceforge.net/ivritex/%{name}-%{version}.tar.bz2
Requires:	tetex
BuildRequires:	tetex-afm
BuildRequires:	tetex-latex
BuildRequires:	fonts-type1-hebrew
BuildRequires:	texlive-collection-fontutils
# Just to make sure all deps are installed
BuildRequires:	texlive-scheme-full
# to have it auto-selected when choosing Hebrew at install time
Requires:	locales-he
Requires:	fonts-type1-hebrew
BuildArch:	noarch

%description
IvriTeX provides Hebrew support for LaTeX. The project provides Hebrew
support for babel, Hebrew fonts, and HebClass - a collection of 
classes and styles that will hopefully be useful to Hebrew authors.

%files
%doc README example/tests/hebhello.tex ChangeLog
%{texmfdir}/bibtex/%{name}
%{texmfdir}/doc/generic/0%{name}
%{texmfdir}/doc/latex/hebclass/hebtech.ps
%{texmfdir}/dvips/base/culmus-he8.enc
%{texmfdir}/dvips/config/culmus.map
%{texmfdir}/fontname/culmus.map
%{texmfdir}/fonts/afm/culmus
%{texmfdir}/fonts/tfm/culmus
%{texmfdir}/fonts/type1/culmus
%{texmfdir}/fonts/vf/culmus
%{texmfdir}/tex/generic/0%{name}
%{texmfdir}/tex/latex/hebclass

%post
updmap-sys --quiet
mktexlsr

%postun
updmap-sys --quiet
mktexlsr

#----------------------------------------------------------------------------

%prep
%setup -q

%build

%install
# modern font paths
perl -pi -e 's,/usr/X11R6/lib/X11/fonts/Type1,/usr/share/fonts/Type1/hebrew,g' fonts/culmus/Makefile
# we use .pfb fonts, not .pfa
perl -pi -e 's,pfa,pfb,g' fonts/culmus/Makefile
# elatex doesn't exist any more
perl -pi -e 's,HEBLATEX=elatex,HEBLATEX=latex,g' ivritex.mk
# use_symlinks makes symlinks to the files from fonts-type1-hebrew
# rather than copying: saves space and ensures they'll stay up-to-date
make TEX_ROOT=%{buildroot}%{texmfdir} use_symlinks=1 install



