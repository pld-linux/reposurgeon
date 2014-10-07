Summary:	VCS repository manipulation tool
Name:		reposurgeon
Version:	3.12
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	http://www.catb.org/~esr/reposurgeon/%{name}-%{version}.tar.gz
# Source0-md5:	4f6bbc17a733112baddaf224bb3d6b2c
URL:		http://www.catb.org/~esr/reposurgeon/
BuildRequires:	asciidoc
BuildRequires:	docbook-dtd412-xml
BuildRequires:	python-devel
BuildRequires:	xmlto
Requires:	python >= 1:2.7.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reposurgeon enables risky operations that version-control systems
don't want to let you do, such as (a) editing past comments and
metadata, (b) excising commits, (c) coalescing commits, and (d)
removing files and subtrees from repo history. The original motivation
for reposurgeon was to clean up artifacts created by repository
conversions.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README TODO features.html repodiffer.html repopuller.html reposurgeon.html
%attr(755,root,root) %{_bindir}/reposurgeon
%attr(755,root,root) %{_bindir}/repopuller
%attr(755,root,root) %{_bindir}/repodiffer
%{_mandir}/man1/reposurgeon.1*
%{_mandir}/man1/repodiffer.1*
%{_mandir}/man1/repopuller.1*
