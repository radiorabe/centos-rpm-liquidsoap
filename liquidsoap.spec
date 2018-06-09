#
# spec file for package liquidsoap
#
# Copyright (c) 2018 Radio Bern RaBe
#                    http://www.rabe.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as 
# published  by the Free Software Foundation, version 3 of the 
# License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/centos-rpm-liquidsoap
#

Name:     liquidsoap 
Version:  1.3.3
Release:  1%{?dist}
Summary:  Liquidsoap by Savonet
License:  GPLv2
URL:      http://liquidsoap.info/
Source0:  https://github.com/savonet/liquidsoap/releases/download/%{version}/liquidsoap-%{version}.tar.bz2
Source1:  liquidsoap@.service

BuildRequires: file-devel
BuildRequires: flac-devel
BuildRequires: inotify-tools-devel
BuildRequires: ladspa-devel
BuildRequires: lame-devel
BuildRequires: libX11-devel
BuildRequires: libmad-devel
BuildRequires: libsamplerate-devel
BuildRequires: libstdc++-static
BuildRequires: libvorbis-devel
BuildRequires: ocaml
BuildRequires: ocaml-alsa-devel
BuildRequires: ocaml-biniou
BuildRequires: ocaml-biniou-devel
BuildRequires: ocaml-cry
BuildRequires: ocaml-dtools
BuildRequires: ocaml-duppy
BuildRequires: ocaml-easy-format
BuildRequires: ocaml-easy-format-devel
BuildRequires: ocaml-faad-devel
BuildRequires: ocaml-fdkaac-devel
BuildRequires: ocaml-findlib
BuildRequires: ocaml-flac
BuildRequires: ocaml-inotify
BuildRequires: ocaml-ladspa
BuildRequires: ocaml-lame
BuildRequires: ocaml-magic
BuildRequires: ocaml-mm
BuildRequires: ocaml-opus
BuildRequires: ocaml-samplerate
BuildRequires: ocaml-soundtouch
BuildRequires: ocaml-speex
BuildRequires: ocaml-ssl-devel
BuildRequires: ocaml-taglib
BuildRequires: ocaml-theora-devel
BuildRequires: ocaml-vorbis >= 0.7.0
BuildRequires: ocaml-xmlm
BuildRequires: ocaml-xmlm-devel
BuildRequires: ocaml-xmlplaylist
BuildRequires: ocaml-yojson-devel
BuildRequires: opus-devel
BuildRequires: pcre-ocaml
BuildRequires: soundtouch-devel
BuildRequires: speex-devel
BuildRequires: systemd
BuildRequires: taglib-devel

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
./configure --with-internal-glib --disable-camomile --prefix=%{_exec_prefix} --sysconfdir=/etc --mandir=/usr/share/man --localstatedir=/var --disable-ldconf

%build
make

%install
%make_install%{_exec_prefix} OCAMLFIND_DESTDIR=%{buildroot}%{_exec_prefix} prefix=%{buildroot}%{_exec_prefix} sysconfdir=%{buildroot}/etc mandir=%{buildroot}%{_exec_prefix}/share/man localstatedir=%{buildroot}/var
/bin/install -d %{buildroot}%{_unitdir}
/bin/install -c %{SOURCE1} -m 644 %{buildroot}%{_unitdir}

%pre
getent group liquidsoap >/dev/null || groupadd -r liquidsoap
getent passwd liquidsoap >/dev/null || \
    useradd -r -g liquidsoap -d /var/lib/liquidsoap -m \
    -c "Liquidsoap system user account" liquidsoap
exit 0

%post
%systemd_post liquidsoap@.service

%preun
%systemd_preun liquidsoap@.service

%postun
%systemd_postun_with_restart liquidsoap@.service

%files
%{_exec_prefix}/bin/liquidsoap
%{_unitdir}/liquidsoap@.service
%config/etc/liquidsoap/radio.liq.example
%config/etc/logrotate.d/liquidsoap
%{_exec_prefix}/lib/liquidsoap/%{version}/
%doc README
%doc
%{_exec_prefix}/share/doc/liquidsoap-%{version}/examples/*.liq
%{_mandir}/man1/liquidsoap.1.*
