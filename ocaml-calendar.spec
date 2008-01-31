%define		ocaml_ver	1:3.10.0
Summary:	A library managing dates and times
Summary(pl.UTF-8):	Biblioteka do obsługi daty i czasu
Name:		ocaml-calendar
Version:	1.10
Release:	3
License:	LGPL + OCaml linking exception
Group:		Libraries
URL:		http://www.lri.fr/~signoles/prog.en.html
Source0:	http://www.lri.fr/~signoles/prog/calendar/calendar-%{version}.tar.gz
# Source0-md5:	ab36c83c354644695cbf81165dc3757d
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Calendar library is a library providing a set of operations
over dates and times.

%package devel
Summary:	A library managing dates and times
Summary(pl.UTF-8):	Biblioteka do obsługi daty i czasu
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
The Calendar library is a library providing a set of operations
over dates and times.

%prep
%setup -q -n calendar-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{calendar,stublibs}

install src/*.cm[ixa]* src/*.a $RPM_BUILD_ROOT%{_libdir}/ocaml/calendar

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# META for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/calendar
echo 'directory = "+calendar"' >> META
install META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/calendar

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc README src/*.mli
%dir %{_libdir}/ocaml/calendar
%{_libdir}/ocaml/calendar/*.cm[ixa]*
%{_libdir}/ocaml/calendar/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/calendar
