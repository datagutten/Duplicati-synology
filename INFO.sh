#!/bin/bash
# Copyright (c) 2000-2020 Synology Inc. All rights reserved.

source /pkgscripts/include/pkg_util.sh

package="Duplicati"
support_url="https://www.duplicati.com/"
displayname="Duplicati"
maintainer="The Duplicati Team"
maintainer_url="http://github.com/duplicati/duplicati"
distributor="The Duplicati Team"
distributor_url="https://www.duplicati.com/"
arch="noarch"
dsmappname="SYNO.BACKUP.DUPLICATI"
support_center="no"
install_dep_services="mono"
start_dep_services="mono"
description="Use Duplicati to backup your data to cloud services"
adminport="8200"

# version="1.0.0-0001"
os_min_ver="7.0-40000"
dsmuidir="webroot"

[ "$(caller)" != "0 NULL" ] && return 0
pkg_dump_info
