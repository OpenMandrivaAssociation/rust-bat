# Generated by rust2rpm 13
# * assert_cmd is not packaged
%bcond_with check
%global __cargo_skip_build 0

%global crate bat

Name:           rust-%{crate}
Version:        0.12.1
Release:        3%{?dist}
Summary:        cat(1) clone with wings

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/bat
Source:         %{crates_source}
# Initial patched metadata
# * Bump console to 0.9, https://github.com/sharkdp/bat/pull/657
# * Bump git2 to 0.11, https://github.com/sharkdp/bat/commit/826624c9fa3af2b9aacd2bbdaa03304b9376b832
Patch0:         bat-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Cat(1) clone with wings.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/bat
%{_mandir}/man1/bat.1*

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
  doc/bat.1

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 09:50:18 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.1-2
- Bump git2 to 0.11

* Tue Dec 10 2019 Josh Stone <jistone@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 18:28:38 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-3
- Update dirs to 2.0

* Fri Jun 07 2019 Josh Stone <jistone@redhat.com> - 0.11.0-2
- Bump git2 to 0.9

* Sat Jun 01 2019 Josh Stone <jistone@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Sun Nov 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Thu Sep 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Mon Sep 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-1
- Initial package
