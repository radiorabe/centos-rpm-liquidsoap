# CentOS 7 RPM Specfile for liquidsoap

This repository contains the specfile for liquidsoap which is part of the [RaBe liquidsoap distribution](https://build.opensuse.org/project/show/home:radiorabe:liquidsoap).

It depends on `libmad` and `lame` from the [nux dextop repo](http://li.nux.ro/repos.html).

## Install

```bash
yum -y install epel-release && rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
curl -o /etc/yum.repos.d/liquidsoap.repo http://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/CentOS_7/home:radiorabe:liquidsoap.repo
yum install liquidsoap
```

You might have to install some dependencies explicitly to get all the parts you need to work. This is due to the fact that liquidsoap does some runtime detection
and to allow for unbloated installs where advanced features are not needed.

## Usage

You can run `liquidsoap` directly on the command line to verify it is working but will want to run scripts automatically as user `liquidsoap` at some stage.

The RaBe liquidsoap distribution comes bundles with an instantiatable systemd service file that takes over the job of upstreams upstart config. While this
does not automatically loop over `/etc/liquidsoap` and start all the contained scripts, configuring it is rather easy.

```bash
# enable and start the bundled example script
cp /etc/liquidsoap/radio.liq.example /etc/liquidsoap/radio.liq
systemctl enable liquidsoap@radio
systemctl start liquidsoap@radio

# add an addtional script and start it
echo "out(sine())" > /etc/liquidsoap/sine-example.liq
systemctl enable liquidsoap@sine-example
systemctl start liquidsoap@sine-example
```
