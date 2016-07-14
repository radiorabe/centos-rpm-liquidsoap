Name:     liquidsoap 
Version:  1.2.1
Release:  3
Summary:  Liquidsoap by Savonet
License:  GPLv2
URL:      http://savonet.sourceforge.net/
Source0:  https://github.com/savonet/liquidsoap/releases/download/1.2.1/liquidsoap-1.2.1.tar.bz2

BuildRequires: ocaml
BuildRequires: pcre-ocaml
BuildRequires: ocaml-duppy
BuildRequires: ocaml-dtools
BuildRequires: ocaml-mm
BuildRequires: libmad-devel
BuildRequires: libX11-devel
BuildRequires: ocaml-taglib
BuildRequires: taglib-devel
BuildRequires: ocaml-cry
BuildRequires: ocaml-samplerate

%prep
%setup -q 
./configure --disable-camomile
make

%install
make install DESTDIR=%{buildroot} OCAMLFIND_DESTDIR=%{buildroot} prefix=%{buildroot}

%files
/bin/liquidsoap
%config/etc/liquidsoap/radio.liq.example
%config/etc/logrotate.d/liquidsoap
/lib/liquidsoap/1.2.1/externals.liq
/lib/liquidsoap/1.2.1/extract-replaygain
/lib/liquidsoap/1.2.1/flows.liq
/lib/liquidsoap/1.2.1/gstreamer.liq
/lib/liquidsoap/1.2.1/http.liq
/lib/liquidsoap/1.2.1/http_codes.liq
/lib/liquidsoap/1.2.1/lastfm.liq
/lib/liquidsoap/1.2.1/pervasives.liq
/lib/liquidsoap/1.2.1/shoutcast.liq
/lib/liquidsoap/1.2.1/utils.liq
/lib/liquidsoap/1.2.1/video.liq
%doc
/share/doc/liquidsoap-1.2.1/examples/README
/share/doc/liquidsoap-1.2.1/examples/fallible.liq
/share/doc/liquidsoap-1.2.1/examples/geek.liq
/share/doc/liquidsoap-1.2.1/examples/radio.liq
/share/doc/liquidsoap-1.2.1/examples/transitions.liq
/share/man/man1/liquidsoap.1

%description
Liquidsoap is a powerful and flexible language for describing your streams. It offers a rich collection of operators that you can combine at will, giving you more power than you need for creating or transforming streams. But liquidsoap is still very light and easy to use, in the Unix tradition of simple strong components working together.

%changelog
* Sat Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- updated to liquidsoap 1.2.1
- changed source location to github
- dont copy PACKAGES.minimal file
* Sat Oct 21 2012 Martin Konecny <martin dot konecny at gmail.com> - 1.0-2
- initial version 
