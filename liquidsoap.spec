Name:     liquidsoap 
Version:  1.3.0
Release:  1
Summary:  Liquidsoap by Savonet
License:  GPLv2
URL:      http://savonet.sourceforge.net/
Source0:  https://github.com/savonet/liquidsoap/releases/download/%{version}/liquidsoap-%{version}.tar.bz2
Source1:  liquidsoap@.service

BuildRequires: libstdc++-static
BuildRequires: ocaml
BuildRequires: ocaml-findlib
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
BuildRequires: ocaml-alsa-devel
BuildRequires: ocaml-vorbis
BuildRequires: libvorbis-devel
BuildRequires: ocaml-opus
BuildRequires: opus-devel
BuildRequires: ocaml-flac
BuildRequires: flac-devel
BuildRequires: ocaml-speex
BuildRequires: speex-devel
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
BuildRequires: ocaml-biniou-devel
BuildRequires: ocaml-biniou
BuildRequires: ocaml-easy-format-devel
BuildRequires: ocaml-easy-format
BuildRequires: ocaml-fdkaac-devel
BuildRequires: ocaml-faad-devel
BuildRequires: ocaml-theora-devel

Requires(pre): shadow-utils

Requires: lame
Requires: libmad

%description
Liquidsoap is a powerful and flexible language for describing your streams. It offers a rich collection of
operators that you can combine at will, giving you more power than you need for creating or transforming
streams. But liquidsoap is still very light and easy to use, in the Unix tradition of simple strong
components working together.

%prep
%setup -q 
./configure --disable-camomile --prefix=%{_exec_prefix} --sysconfdir=/etc --mandir=/usr/share/man --localstatedir=/var --disable-ldconf

%build
make

%install
make install DESTDIR=%{buildroot}%{_exec_prefix} OCAMLFIND_DESTDIR=%{buildroot}%{_exec_prefix} prefix=%{buildroot}%{_exec_prefix} sysconfdir=%{buildroot}/etc mandir=%{buildroot}%{_exec_prefix}/share/man localstatedir=%{buildroot}/var
/bin/install -d %{buildroot}%{_exec_prefix}/lib/systemd/system/
/bin/install -c %{SOURCE1} -m 644 %{buildroot}%{_exec_prefix}/lib/systemd/system/

%pre
getent group liquidsoap >/dev/null || groupadd -r liquidsoap
getent passwd liquidsoap >/dev/null || \
    useradd -r -g liquidsoap -d /var/lib/liquidsoap -m \
    -c "Liquidsoap system user account" liquidsoap
exit 0

%files
%{_exec_prefix}/bin/liquidsoap
%{_exec_prefix}/lib/systemd/system/liquidsoap@.service
%config/etc/liquidsoap/radio.liq.example
%config/etc/logrotate.d/liquidsoap
%{_exec_prefix}/lib/liquidsoap/%{version}/
%doc README
%doc
%{_exec_prefix}/share/doc/liquidsoap-%{version}/examples/*.liq
%{_exec_prefix}/share/man/man1/liquidsoap.1.gz
