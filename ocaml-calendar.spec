%define		ocaml_ver	1:3.10.0
Summary:	OCaml library managing dates and times
Summary(pl.UTF-8):	Biblioteka OCamla do obsługi daty i czasu
Name:		ocaml-calendar
Version:	2.01.1
Release:	1
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	http://forge.ocamlcore.org/frs/download.php/173/calendar-%{name}.tar.gz
# Source0-md5:	a30974a97f718688198c5a5dc6235cff
URL:		http://www.lri.fr/~signoles/prog.en.html
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
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{calendar,stublibs}

install src/*.cm[ixa]* target/*.a $RPM_BUILD_ROOT%{_libdir}/ocaml/calendar

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
