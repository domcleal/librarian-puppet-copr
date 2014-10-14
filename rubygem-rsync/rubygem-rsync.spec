%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name rsync

Summary: Ruby library to synchronize files between remote hosts via rsync
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.9
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/jbussdieker/ruby-rsync
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
%if 0%{?fedora} > 18 || 0%{?rhel} >= 7
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi)
%endif
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ruby/Rsync is a Ruby library that can synchronize files between remote hosts
by wrapping a call to the rsync binary.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}

%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}
%{?scl:"}

%files
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/rsync.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Oct 14 2014 Dominic Cleal <dcleal@redhat.com> 1.0.9-1
- new package built with tito

