%define		svnrev	43
%define		rel		1
Summary:	C++ lint your files
Name:		cpplint
Version:	0.1
Release:	0.1
License:	Artistic License/GPL
Group:		Development/Tools
# svn co http://google-styleguide.googlecode.com/svn/trunk/cpplint
# tar -cjf cpplint-$(svnversion cpplint).tar.bz2 --exclude=.svn --remove-files cpplint
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	b34ddbdddab368aa071731cee3470fc2
URL:		http://google-styleguide.googlecode.com/svn/trunk/cpplint/
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is automated checker to make sure a C++ file follows Google's C++
style guide
<http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml>.

As it heavily relies on regular expressions, cpplint.py won't catch
all violations of the style guide and will very occasionally report a
false positive. There is a list of things we currently don't handle
very well at the top of cpplint.py, and we welcome patches to improve
it.

%prep
%setup -q -n %{name}
%{__sed} -i -e '1s,#!.*python\(2\..\)\?,#!%{__python},' *.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/cpplint
