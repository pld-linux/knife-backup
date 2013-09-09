%define	pkgname	knife-backup
Summary:	Chef knife plugins to help backup and restore chef servers
Name:		ruby-%{pkgname}
Version:	0.0.8
Release:	0.2
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	29a04f47776955a15bb260e1e9c0c8fe
URL:		https://github.com/mdxp/knife-backup
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	chef >= 0.10.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chef knife plugins to help backup and restore chef servers

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_vendorlibdir}/chef/knife/backup_export.rb
%{ruby_vendorlibdir}/chef/knife/backup_restore.rb