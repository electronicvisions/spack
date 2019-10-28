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

    # prefetches PR #14 typedef alias support (and the llvm 9.x stuff)
    version('alias', git='https://github.com/electronicvisions/genpybind.git',
            commit="69ca6c09fbac46efc733ff2fd21bb13af9345140", preferred=True)
    version('0.1.1-pre', git='https://github.com/kljohann/genpybind.git',
            commit="9d06a3ad4b6b917c8fcc07261a97b13a3079bcba")
    version('0.1.0', '345ca9c6ca96f79c8a217e44a9c99fe6')
    version('develop', git='https://github.com/kljohann/genpybind.git')

    depends_on(
            'llvm+clang+python+visionary@5.0.0:5.999.999,7.0.0:7.999.999,9.0.0:9.999.999',
        type=('build', 'link', 'run'))
    depends_on('binutils', type='build')
    depends_on('python@2.7:', type=('build', 'run'))

    extends('python')

    def configure_args(self):
        args = super(Genpybind, self).configure_args()
        args.append("--disable-tests")
        return args
