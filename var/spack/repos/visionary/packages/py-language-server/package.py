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


class PyLanguageServer(PythonPackage):
    """An implementation of the Language Server Protocol for Python"""

    homepage = "https://github.com/palantir/python-language-server"
    url      = "https://pypi.io/packages/source/p/python-language-server/python-language-server-0.22.0.tar.gz"

    version('0.22.0', 'a45f2ea5538dc7e9743f7f319f98bb71')

    depends_on('py-setuptools', type='build')
    depends_on('py-configparser', type=('build', 'run'), when='^python@:2.999.999')
    depends_on('py-future@0.14.0:', type=('build', 'run'))
    depends_on('py-futures', type=('build', 'run'), when='^python@:2.999.999')
    depends_on('py-jedi@0.12:', type=('build', 'run'))
    depends_on('py-jsonrpc-server@0.1.0:', type=('build', 'run'))
    depends_on('py-pluggy', type=('build', 'run'))

    depends_on('py-autopep8', type=('build', 'run'))
    depends_on('py-mccabe', type=('build', 'run'))
    depends_on('py-pycodestyle', type=('build', 'run'))
    depends_on('py-pydocstyle@2.0.0:', type=('build', 'run'))
    depends_on('py-pyflakes@1.6.0:', type=('build', 'run'))
    depends_on('py-rope@0.10.5:', type=('build', 'run'))
    depends_on('py-yapf', type=('build', 'run'))
