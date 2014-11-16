%define		ocaml_ver	1:3.10.0
Summary:	OCaml library managing dates and times
Summary(pl.UTF-8):	Biblioteka OCamla do obsługi daty i czasu
Name:		ocaml-calendar
Version:	2.04
Release:	1
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	http://forge.ocamlcore.org/frs/download.php/1481/calendar-%{version}.tar.gz
# Source0-md5:	625b4f32c9ff447501868fa1c44f4f4f
URL:		https://forge.ocamlcore.org/projects/calendar/
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Calendar library is an OCaml library providing a set of operations
over dates and times.

%description -l pl.UTF-8
Calendar to biblioteka OCamla udostępniająca operacje na datach i
czasie.

%package devel
Summary:	OCaml library managing dates and times
Summary(pl.UTF-8):	Biblioteka OCamla do obsługi daty i czasu
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
The Calendar library is an OCaml library providing a set of operations
over dates and times.

%description devel -l pl.UTF-8
Calendar to biblioteka OCamla udostępniająca operacje na datach i
czasie.

%prep
%setup -q -n calendar-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{calendar,stublibs}

%{__make} \
	 install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# META for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/calendar
echo 'directory = "+calendar"' >> META
install META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/calendar
%{__sed} -i -e 's/calendarLib.cm[ox] //' $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/calendar/META

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc README src/*.mli
%dir %{_libdir}/ocaml/calendar
%{_libdir}/ocaml/calendar/*.cm[ixa]*
%{_libdir}/ocaml/calendar/*.cmo
%{_libdir}/ocaml/calendar/*.mli
%{_libdir}/ocaml/calendar/*.[ao]
%{_libdir}/ocaml/site-lib/calendar
%{_examplesdir}/%{name}-%{version}
