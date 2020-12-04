#!/bin/bash
#
# RPM build wrapper for liquidsoap, runs inside the build container on travis-ci

set -xe

OBS_OS=`source /etc/os-release; echo $ID`

case $OBS_OS in
"centos")
    OBS_DIST="CentOS_8"
    curl -o /etc/yum.repos.d/ocaml.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap:/ocaml/${OBS_DIST}/home:radiorabe:liquidsoap:ocaml.repo"

    # somewhat adventurous install of deps since we have less control than in OBS
    dnf config-manager --set-disabled epel

    dnf install -y --enablerepo=epel \
      flac-libs \
      inotify-tools-devel \
      jack-audio-connection-kit-devel

    dnf install -y --enablerepo=PowerTools \
      file-devel \
      flac \
      flac-devel \
      ladspa-devel \
      lame-devel \
      libmad-devel \
      libsamplerate-devel \
      libstdc++-static \
      libtheora-devel \
      libvorbis-devel \
      opus-devel \
      pandoc \
      perl-XML-DOM \
      soundtouch-devel \
      speex-devel \
      taglib-devel

    # we install these explicitly until theier old versions get removed from OBS, on OBS they are deactivated for builds so this is not an issue
    dnf install -y --disablerepo=home_radiorabe_liquidsoap \
      ocaml-biniou-devel \
      ocaml-yojson-devel \
      ocaml-xmlm-devel
    ;;
"fedora")
    V=`source /etc/os-release; echo $VERSION_ID`
    OBS_DIST="Fedora_${V}"
    ;;
esac

curl -o /etc/yum.repos.d/liquidsoap.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/${OBS_DIST}/home:radiorabe:liquidsoap.repo"
echo 'exclude=ocaml-biniou* ocaml-yojson* ocaml-xmlm*' >> /etc/yum.repos.d/liquidsoap.repo

chown root:root liquidsoap.spec

rpmdev-setuptree

cp *.patch *.service /root/rpmbuild/SOURCES/

build-rpm-package.sh liquidsoap.spec
