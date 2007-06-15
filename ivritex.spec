%define	name	ivritex
%define	version	1.2.1
%define	release	%mkrel 1

%define texmfdir %{_datadir}/texmf
%define updmap /usr/share/texmf/fonts/map/dvips/updmap

Summary:	Files for processing Hebrew LaTeX documents
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://downloads.sourceforge.net/ivritex/%{name}-%{version}.tar.bz2
License:	LPPL
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
URL:		http://ivritex.sourceforge.net/
Requires:	tetex
BuildRequires:	tetex-afm
BuildRequires:	tetex-latex
BuildRequires:	fonts-type1-hebrew
BuildArch:	noarch
# to have it auto-selected when choosing Hebrew at install time
Requires:	locales-he
Requires:	fonts-type1-hebrew
# last release using tetex-latex-heb name was 2007 Spring
Obsoletes:	tetex-latex-heb
Provides:	tetex-latex-heb

%description
IvriTeX provides Hebrew support for LaTeX. The project provides Hebrew
support for babel, Hebrew fonts, and HebClass - a collection of 
classes and styles that will hopefully be useful to Hebrew authors.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
# modern font paths
perl -pi -e 's,/usr/X11R6/lib/X11/fonts/Type1,/usr/share/fonts/Type1/hebrew,g' fonts/culmus/Makefile
# we use .pfb fonts, not .pfa
perl -pi -e 's,pfa,pfb,g' fonts/culmus/Makefile
# elatex doesn't exist any more
perl -pi -e 's,HEBLATEX=elatex,HEBLATEX=latex,g' ivritex.mk
# use_symlinks makes symlinks to the files from fonts-type1-hebrew
# rather than copying: saves space and ensures they'll stay up-to-date
make TEX_ROOT=%{buildroot}%{texmfdir} use_symlinks=1 install

%post
updmap-sys --quiet
mktexlsr

%postun
updmap-sys --quiet
mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,0755)  
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
