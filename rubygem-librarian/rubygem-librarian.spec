%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%define gem_name librarian

Summary: A Framework for Bundlers
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/applicationsonline/librarian
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: git
Requires: %{?scl_prefix}rubygems
%if 0%{?fedora} > 18 || 0%{?rhel} >= 7
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi)
%endif
Requires: %{?scl_prefix}rubygem(thor) >= 0.15
Requires: %{?scl_prefix}rubygem(thor) < 1
Requires: %{?scl_prefix}rubygem(highline)
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Librarian is a framework for writing bundlers, which are tools that resolve,
fetch, install, and isolate a project's dependencies, in Ruby.

A bundler written with Librarian will expect you to provide a specfile listing
your project's declared dependencies, including any version constraints and
including the upstream sources for finding them. Librarian can resolve the
spec, write a lockfile listing the full resolution, fetch the resolved
dependencies, install them, and isolate them in your project.

A bundler written with Librarian will be similar in kind to Bundler, the
bundler for Ruby gems that many modern Rails applications use.

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
%{gem_dir}/gems/%{gem_name}-%{version}/
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/LICENSE.txt
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/*.gemspec

%changelog
* Fri Apr 04 2014 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- new package built with tito
