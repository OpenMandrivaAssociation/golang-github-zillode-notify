# https://github.com/Zillode/notify
%global goipath github.com/Zillode/notify
%global commit  a4d89c12bcfbda5640050eb549079dad19f7741c
%global date    20180313

%gometa

Name:           golang-github-zillode-notify
Version:        0
Release:        0.11%{?dist}
Summary:        File system event notification library on steroids
License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(golang.org/x/sys/unix)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
# ignore test results for now
%gochecks || :


%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS


%changelog
* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.11.20180313gita4d89c1
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20180313.gita4d89c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.9.20180313.gita4d89c1
- Bump to commit a4d89c1.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20180204.gita8abcfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.7.20180204.gita8abcfb
- Bump to commit a8abcfb.

* Tue Dec 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.20171210.git8fff849
- Bump to commit 8fff849.

* Fri Oct 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.git54e3093
- Bump to commit 54e3093.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitd1bed6c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitd1bed6c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.2.gitd1bed6c
- Bump to commit d1bed6c.

* Mon Mar 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.gitc2582a9
- First package for Fedora

