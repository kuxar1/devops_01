Name:       hello_world
Version:    1.0
Release:    1%{?dist}
Summary:    Hello World
License:    GPLv3+
BuildArch:  noarch

%description
Hello World!

%prep

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog