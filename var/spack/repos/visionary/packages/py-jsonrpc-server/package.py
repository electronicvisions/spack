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


class PyJsonrpcServer(PythonPackage):
    """A Python 3 asynchronous JSON RPC server"""

    homepage = "https://github.com/palantir/python-jsonrpc-server"
    url      = "https://pypi.io/packages/source/p/python-jsonrpc-server/python-jsonrpc-server-0.1.2.tar.gz"

    version('0.1.2', 'b1bc6c2854764f874040a0dd921f6f35')

    depends_on('py-setuptools', type='build')
    depends_on('py-future@0.14.0:', type=('build', 'run'))
