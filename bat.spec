%global __cargo_skip_build 0

%global crate bat

Name:           bat
Version:        0.25.0
Release:        1
Summary:        cat(1) clone with wings

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/bat
Source0:         https://github.com/sharkdp/bat/archive/v%{version}/bat-%{version}.tar.gz
Source1:        vendor.tar.xz
#Source2:        cargo_config

BuildRequires:  rust-packaging
# Renamed 2025/02/13 before 6.0
%rename rust-bat

%global _description %{expand:
Cat(1) clone with wings.}

%description %{_description}

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch
# Renamed 2025/02/13 before 6.0
%rename rust-bat-bash-completion

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Recommends:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch
# Renamed 2025/02/13 before 6.0
%rename rust-bat-fish-completion

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch
# Renamed 2025/02/13 before 6.0
%rename rust-bat-zsh-completion

%description zsh-completion
Zsh command line completion support for %{name}.


%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/bat
%{_mandir}/man1/bat.1*

%files bash-completion
%{_datadir}/bash-completion/completions/bat

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/bat.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_bat

%prep
%autosetup -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build

%install
#cargo_install
install -D -m 0755 target/release/bat %{buildroot}%{_bindir}/bat
install -D -m 0644 $(find target/release/build -name "bat.1") "%{buildroot}/%{_mandir}/man1/bat.1"

install -D -m 0644 $(find target/release/build -name "bat.bash") "%{buildroot}/%{_datadir}/bash-completion/completions/bat"
install -D -m 0644 $(find target/release/build -name "bat.fish") "%{buildroot}/%{_datadir}/fish/vendor_completions.d/bat.fish"
install -D -m 0644 $(find target/release/build -name "bat.zsh")  "%{buildroot}/%{_datadir}/zsh/site-functions/_bat"

#install -Dpm0644 -t %{buildroot}%{_mandir}/man1 \
#  doc/bat.1
