Summary:	VCS repository manipulation tool
Name:		reposurgeon
Version:	3.36
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	http://www.catb.org/~esr/reposurgeon/%{name}-%{version}.tar.xz
# Source0-md5:	6580579ec266d8ec3b2ed1fcbfa024d4
URL:		http://www.catb.org/~esr/reposurgeon/
BuildRequires:	asciidoc
BuildRequires:	docbook-dtd412-xml
BuildRequires:	pylint
BuildRequires:	python-devel >= 1:2.7.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto
BuildRequires:	xz
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reposurgeon enables risky operations that version-control systems
don't want to let you do, such as editing past comments and metadata
and removing commits. It works with any version control system that
can export and import git fast-import streams, including git, hg,
fossil, bzr, CVS and RCS. It can also read Subversion dump files
directly and can thus be used to script production of very
high-quality conversions from Subversion to any supported DVCS.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix} \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md AUTHORS COPYING NEWS TODO *.html
%attr(755,root,root) %{_bindir}/repocutter
%attr(755,root,root) %{_bindir}/repodiffer
%attr(755,root,root) %{_bindir}/repomapper
%attr(755,root,root) %{_bindir}/reposurgeon
%attr(755,root,root) %{_bindir}/repotool
%{_mandir}/man1/repocutter.1*
%{_mandir}/man1/repodiffer.1*
%{_mandir}/man1/repomapper.1*
%{_mandir}/man1/reposurgeon.1*
%{_mandir}/man1/repotool.1*
