Summary:	XIRW - an infrared commands debugger
Summary(pl):	XIRW - debugger sygna³ów w podczerwieni
Name:		xirw
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.sourceforge.net/LIRC/%{name}-%{version}.tar.gz
URL:		http://www.lirc.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lirc-devel >= 0.6.0
BuildRequires:	qt-devel >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xirw is a Qt based application that shows you which commands are
received by LIRC.

%description -l pl
Xirw jest aplikacj± z interfejsem w Qt, która pokazuje jakie komendy
s± odbierane prze LIRC.

%prep
%setup -q

%build
aclocal
%{__automake}
%{__autoconf}
%configure \
    --with-qt-libraries=/usr/X11R6/lib \
    --with-qt-includes=/usr/X11R6/include/qt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/bin
install xirw $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog
%attr(755,root,root) %{_prefix}/X11R6/bin/xirw
