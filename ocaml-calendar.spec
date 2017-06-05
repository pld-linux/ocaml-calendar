#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		ocaml_ver	1:3.10.0
Summary:	OCaml library managing dates and times
Summary(pl.UTF-8):	Biblioteka OCamla do obsługi daty i czasu
Name:		ocaml-calendar
Version:	2.04
Release:	4
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	http://forge.ocamlcore.org/frs/download.php/1481/calendar-%{version}.tar.gz
# Source0-md5:	625b4f32c9ff447501868fa1c44f4f4f
URL:		https://forge.ocamlcore.org/projects/calendar/
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
BuildRequires:	sed >= 4.0
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
Requires:	%{name} = %{version}-%{release}

%description devel
The Calendar library is an OCaml library providing a set of operations
over dates and times.

This package contains files needed to develop OCaml programs using
calendar library.

%description devel -l pl.UTF-8
Calendar to biblioteka OCamla udostępniająca operacje na datach i
czasie.

Ten pakiet zawiera pliki niezbędne do tworzenia programów używających
biblioteki calendar.

%prep
%setup -q -n calendar-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{calendar,stublibs}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# move META for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/calendar
%{__mv} $RPM_BUILD_ROOT%{_libdir}/ocaml/calendar/META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/calendar
echo 'directory = "+calendar"' >> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/calendar/META

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/ocaml/calendar
%{_libdir}/ocaml/calendar/calendarLib.cma
%{_libdir}/ocaml/calendar/calendarLib.cmo
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/calendar/calendarLib.cmxs
%endif
%{_libdir}/ocaml/site-lib/calendar

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/calendar/calendarLib.cmi
# doc?
%{_libdir}/ocaml/calendar/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/calendar/calendarLib.cmx
%{_libdir}/ocaml/calendar/calendarLib.cmxa
%{_libdir}/ocaml/calendar/calendarLib.a
%{_libdir}/ocaml/calendar/calendarLib.o
%endif
%{_examplesdir}/%{name}-%{version}
