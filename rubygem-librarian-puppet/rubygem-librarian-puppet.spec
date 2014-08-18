%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name librarian-puppet

Summary: Bundler for your Puppet modules
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.9
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/rodjek/librarian-puppet
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: git
Requires: %{?scl_prefix}puppet
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi)
Requires: %{?scl_prefix}rubygem(json)
Requires: %{?scl_prefix}rubygem(librarian) >= 0.1.2
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Simplify deployment of your Puppet infrastructure by automatically pulling in
modules from the forge and git repositories with a single command.

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

mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gem_dir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gem_dir}/bin
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%{_bindir}/librarian-puppet
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/LICENSE
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Wed Aug 06 2014 Dominic Cleal <dcleal@redhat.com> 1.0.8-1
- Update to 1.0.8 (dcleal@redhat.com)

* Mon Aug 04 2014 Dominic Cleal <dcleal@redhat.com> 1.0.7-1
- Update to 1.0.7 (dcleal@redhat.com)

* Fri Aug 01 2014 Dominic Cleal <dcleal@redhat.com> 1.0.6-1
- Update to 1.0.6 (dcleal@redhat.com)

* Tue Jul 22 2014 Dominic Cleal <dcleal@redhat.com> 1.0.5-1
- Update to 1.0.5 (dcleal@redhat.com)

* Mon Jun 09 2014 Dominic Cleal <dcleal@redhat.com> 1.0.3-1
- Update to 1.0.3 (dcleal@redhat.com)

* Mon May 12 2014 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- Update to 1.0.2 (dcleal@redhat.com)

* Mon Apr 14 2014 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Update to 1.0.1 (dcleal@redhat.com)

* Fri Apr 04 2014 Dominic Cleal <dcleal@redhat.com> 0.9.17-1
- Update to 0.9.17

* Fri Jan 17 2014 Dominic Cleal <dcleal@redhat.com> 0.9.10-3
- Correct rubygem-thor dependency (dcleal@redhat.com)

* Fri Jan 17 2014 Dominic Cleal <dcleal@redhat.com> 0.9.10-2
- Add git dependency (dcleal@redhat.com)

* Fri Jan 17 2014 Dominic Cleal <dcleal@redhat.com> 0.9.10-1
- new package built with tito

