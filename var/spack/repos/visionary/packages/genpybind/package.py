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


class Genpybind(WafPackage):
    """Autogeneration of Python bindings from manually annotated C++ headers"""

    homepage = "https://github.com/kljohann/genpybind"
    url      = "https://github.com/kljohann/genpybind/archive/v0.1.0.tar.gz"
    git      = "https://github.com/kljohann/genpybind.git"

    version('0.2.1', sha256='e4d993f0c65cb5cf635cec7df899cbd91af1f0bd8a3626f33e9e0925f5383384')
    version('0.2.0', sha256='9d1e9d026a9e355e282aca549a2af108bedcc5bc59ba0b76a6072f88e4c0be4c')
    version('0.1.1-pre', commit="9d06a3ad4b6b917c8fcc07261a97b13a3079bcba")
    version('0.1.0', sha256='f25cb2b3180103cb96c42fb8d37be8b1f06b7721f6aa08841d5ae16361896407')
    version('master', branch='master')
    version('develop', branch='develop')

    version('ebrains', tag='ebrains_release-1-rc1', git='https://github.com/electronicvisions/genpybind')
    version('visions', branch='master', git='https://github.com/electronicvisions/genpybind')

    depends_on(
        'llvm+clang+python+visionary@5.0.0:5.999.999,7.0.0:7.999.999,9.0.0:',
        type=('build', 'link', 'run'))
    depends_on('binutils', type='build')
    depends_on('python@2.7:', type=('build', 'run'))

    extends('python')

    def configure_args(self):
        args = super(Genpybind, self).configure_args()

        if self.spec.satisfies("@visions") or self.spec.satisfies("@ebrains"):
            # currently only our HEAD supports the rename
            # TODO: adapt once the change is upstream
            args.append("--genpybind-disable-tests")
        else:
            args.append("--disable-tests")
        return args
