Summary:	Chef knife plugins to help backup and restore chef servers
Name:		knife-backup
Version:	0.0.10
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	bf69bba9c8caa111b675390e5cfabcf2
URL:		https://github.com/mdxp/knife-backup
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	knife >= 0.10.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chef knife plugins to help backup and restore chef servers

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}
%{ruby_vendorlibdir}/chef/knife/backup_export.rb
%{ruby_vendorlibdir}/chef/knife/backup_restore.rb
