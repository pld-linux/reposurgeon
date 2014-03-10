Summary:	VCS repository manipulation tool
Name:		reposurgeon
Version:	3.6
Release:	1
License:	BSD
Group:		Development/Tools
URL:		http://www.catb.org/~esr/reposurgeon/
Source0:	http://www.catb.org/~esr/reposurgeon/%{name}-%{version}.tar.gz
# Source0-md5:	a582cdf942d756deb7b78b7676797640
BuildRequires:	asciidoc
BuildRequires:	docbook-dtd412-xml
BuildRequires:	xmlto
Requires:	python >= 2.7.2
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
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README TODO features.html repodiffer.html repopuller.html reposurgeon.html
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/repopuller
%attr(755,root,root) %{_bindir}/repodiffer
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/repodiffer.1*
%{_mandir}/man1/repopuller.1*
