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


class PyMmdnn(PythonPackage):
    """MMdnn is a set of tools to help users inter-operate among different deep
    learning frameworks"""

    homepage = "https://github.com/Microsoft/MMdnn"
    url      = "https://github.com/Microsoft/MMdnn/archive/0.2.1.tar.gz"

    version('master', git='https://github.com/Microsoft/MMdnn', branch='master')
    version('0.2.1', '9f5c45289369f6c16555bb0067b60e02')

    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-numpy@1.15.0:', type=('build', 'run'))
    depends_on('py-pillow@3.1.0:', type=('build', 'run'))
    depends_on('py-protobuf@3.6.0:', type='build')
    depends_on('py-six@1.10.0:', type=('build', 'run'))
    depends_on('py-uuid@1.30:', type=('build', 'run'))
