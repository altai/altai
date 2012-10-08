%define project_baseurl 'http://osc-build.vm.griddynamics.net/altai'
%define project_devurl None


Name:           altai-release
Version:        1.0.1
Release:        v1.0.1%{?dist}
Summary:        Altai packages for Enterprise Linux repository configuration

Group:          System Environment/Base
License:        LGPL

URL:            http://yum.griddynamics.net/yum/essex/
Source0:        http://yum.griddynamics.net/yum/essex/OpenStack-GD-RPM-GPG.key
Source1:        lgpl-2.1.txt
Source2:        altai.repo
Source3:        http://download.fedora.redhat.com/pub/epel/RPM-GPG-KEY-EPEL-6

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
This package contains the Altai packages for Enterprise Linux repository
GPG key as well as configuration for yum and up2date.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} LGPL

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-altai
install -Dpm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# vars
yum_vars_dir=$RPM_BUILD_ROOT/etc/yum/vars/
mkdir -p "$yum_vars_dir"
echo %{project_baseurl} > "$yum_vars_dir/altai_baseurl"
%if "%{project_devurl}" != None
echo %{project_devurl} > "$yum_vars_dir/altai_devurl"
%endif
chmod 644 "$yum_vars_dir"/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LGPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*
/etc/yum/vars/*


%changelog
