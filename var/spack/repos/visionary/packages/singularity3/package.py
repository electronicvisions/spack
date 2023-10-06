##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import os
import shutil


class Singularity3(Package):
    """Singularity is a container platform focused on supporting 'Mobility of
       Compute'"""

    homepage = "https://www.sylabs.io/singularity/"
    url      = "https://github.com/sylabs/singularity/archive/v3.0.2.tar.gz"

    version('3.0.3',     '1dadc7a45d79c3503aab3a40bf9e9548')
    version('3.0.3-rc1', 'cc66e761b5344efbeb48e1123245d930')

    # experimental features
    version('trustedContainers-v2', git='https://github.com/obreitwi/singularity.git',
            tag='feature/trustedContainers-v2')

    variant('global_config', default=False,
            description="If enabled, the config folder will be installed to "
                        "/etc/singularity (needs sufficient permissions).")

    extends('go', deptypes='build')

    depends_on('openssl')
    depends_on('util-linux')
    # TODO: seccomp missing

    def install(self, spec, prefix):
        env = os.environ
        env['GOPATH'] = self.stage.path + ':' + env['GOPATH']

        with working_dir(os.path.join(self.stage.path, 'src/github.com/sylabs'), create=True):
            ln = which('ln')
            ln('-s', self.stage.source_path, 'singularity')

        with working_dir(self.stage.source_path):
            mconfig = Executable('./mconfig')
            mconfig_args = [
                    '-V', str(self.version),
                    '--prefix={0}'.format(prefix),
                    '--localstatedir=/var/lib']
            if spec.satisfies("+global_config"):
                mconfig_args.append('--sysconfdir=/etc/singularity')
            mconfig(*mconfig_args,
                    env=env)
            with working_dir('builddir'):
                make(env=env)
                make('install', '-j', '1', env=env)
