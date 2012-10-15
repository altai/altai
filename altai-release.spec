Name:           altai-release
Version:        1.0.1
Release:        v1.0.1%{?dist}
Summary:        Altai packages for Enterprise Linux repository configuration

Group:          System Environment/Base
License:        LGPL

URL:            http://www.griddynamics.com/solutions/altai-private-cloud-for-developers/
Source0:        %{name}-%{version}.tar.gz
Source1:        baseurl

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
This package contains the Altai packages for Enterprise Linux repository
GPG key as well as configuration for yum and up2date.

%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
for key in RPM-GPG-KEY-altai RPM-GPG-KEY-EPEL-6-altai; do
    install -Dpm 644 project-release/$key $RPM_BUILD_ROOT/etc/pki/rpm-gpg/$key
done

# yum
install -Dpm 644 project-release/altai.repo $RPM_BUILD_ROOT/etc/yum.repos.d/altai.repo

# vars
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/yum/vars/altai_baseurl


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*
/etc/yum/vars/*


%changelog
