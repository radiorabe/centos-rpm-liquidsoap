# CentOS 7 RPM Specfile for liquidsoap

This repository contains the specfile for liquidsoap which is part of the [RaBe liquidsoap distribution](https://build.opensuse.org/project/show/home:radiorabe:liquidsoap).

It depends on `libmad` and `lame` from the [nux dextop repo](http://li.nux.ro/repos.html).

## Usage

```bash
yum -y install epel-release && rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
curl -o /etc/yum.repos.d/liquidsoap.repo http://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/CentOS_7/home:radiorabe:liquidsoap.repo
yum install liquidsoap
```
