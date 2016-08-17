Name:     liquidsoap 
Version:  1.2.1
Release:  3
Summary:  Liquidsoap by Savonet
License:  GPLv2
URL:      http://savonet.sourceforge.net/
Source0:  https://github.com/savonet/liquidsoap/releases/download/1.2.1/liquidsoap-1.2.1.tar.bz2
Source1:  liquidsoap@.service

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
BuildRequires: libsamplerate-devel
BuildRequires: ocaml-lame
BuildRequires: lame-devel
BuildRequires: ocaml-alsa
BuildRequires: alsa-lib-devel
BuildRequires: ocaml-vorbis
BuildRequires: libvorbis-devel
BuildRequires: ocaml-opus
BuildRequires: opus-devel
BuildRequires: ocaml-flac
BuildRequires: flac-devel
BuildRequires: ocaml-speex
BuildRequires: speex-devel
BuildRequires: ocaml-schroedinger
BuildRequires: schroedinger-devel
BuildRequires: ocaml-xmlm-devel
BuildRequires: ocaml-xmlm
BuildRequires: ocaml-xmlplaylist
BuildRequires: ocaml-ladspa
BuildRequires: ladspa-devel
BuildRequires: ocaml-soundtouch
BuildRequires: soundtouch-devel
BuildRequires: ocaml-magic
BuildRequires: file-devel
BuildRequires: ocaml-ssl-devel
BuildRequires: ocaml-yojson-devel
BuildRequires: ocaml-inotify
BuildRequires: inotify-tools-devel
BuildRequires: ocaml-biniou

Requires(pre): shadow-utils

Requires: lame
Requires: libmad

%prep
%setup -q 
./configure --disable-camomile --prefix=/usr --sysconfdir=/etc --mandir=/usr/share/man --localstatedir=/var
make

%install
make install DESTDIR=%{buildroot}/usr/ OCAMLFIND_DESTDIR=%{buildroot}/usr/ prefix=%{buildroot}/usr sysconfdir=%{buildroot}/etc mandir=%{buildroot}/usr/share/man localstatedir=%{buildroot}/var
/bin/install -c scripts/liquidtts %{buildroot}/usr/lib/%{name}/%{version}
/bin/install -d %{buildroot}/usr/lib/systemd/system/
/bin/install -c %{SOURCE1} -m 644 %{buildroot}/usr/lib/systemd/system/

%pre
getent group liquidsoap >/dev/null || groupadd -r liquidsoap
getent passwd liquidsoap >/dev/null || \
    useradd -r -g liquidsoap -d /var/lib/liquidsoap -m \
    -c "Liquidsoap system user account"i liquidsoap
exit 0

%files
/usr/bin/liquidsoap
/usr/lib/systemd/system/liquidsoap@.service
%config/etc/liquidsoap/radio.liq.example
%config/etc/logrotate.d/liquidsoap
/usr/lib/liquidsoap/1.2.1/externals.liq
/usr/lib/liquidsoap/1.2.1/extract-replaygain
/usr/lib/liquidsoap/1.2.1/flows.liq
/usr/lib/liquidsoap/1.2.1/gstreamer.liq
/usr/lib/liquidsoap/1.2.1/http.liq
/usr/lib/liquidsoap/1.2.1/http_codes.liq
/usr/lib/liquidsoap/1.2.1/lastfm.liq
/usr/lib/liquidsoap/1.2.1/pervasives.liq
/usr/lib/liquidsoap/1.2.1/shoutcast.liq
/usr/lib/liquidsoap/1.2.1/utils.liq
/usr/lib/liquidsoap/1.2.1/video.liq
/usr/lib/liquidsoap/1.2.1/liquidtts
%doc
/usr/share/doc/liquidsoap-1.2.1/examples/README
/usr/share/doc/liquidsoap-1.2.1/examples/fallible.liq
/usr/share/doc/liquidsoap-1.2.1/examples/geek.liq
/usr/share/doc/liquidsoap-1.2.1/examples/radio.liq
/usr/share/doc/liquidsoap-1.2.1/examples/transitions.liq
/usr/share/man/man1/liquidsoap.1.gz

%description
Liquidsoap is a powerful and flexible language for describing your streams. It offers a rich collection of operators that you can combine at will, giving you more power than you need for creating or transforming streams. But liquidsoap is still very light and easy to use, in the Unix tradition of simple strong components working together.

%changelog
* Sat Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- updated to liquidsoap 1.2.1
- changed source location to github
- dont copy PACKAGES.minimal file
* Sat Oct 21 2012 Martin Konecny <martin dot konecny at gmail.com> - 1.0-2
- initial version 
