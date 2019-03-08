# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPythonEngineio(PythonPackage):
    """Engine.IO is the implementation of transport-based
    cross-browser/cross-device bi-directional communication
    layer for Socket.IO."""

    homepage = "http://python-engineio.readthedocs.io/en/latest/"
    url      = "https://github.com/miguelgrinberg/python-engineio/archive/v2.0.2.tar.gz"

    version('3.3.0',
            sha256='e4ac17c04c32ccca67287dfdbbe4ee1e9eec3a0a1a9a6070f3ab784db08407dd',
            url='https://files.pythonhosted.org/packages/2f/09/83d627ad3dadd064bfb875c7767e93f3568354fe82cebe298b4e07f79238/python-engineio-3.3.0.tar.gz')
    version('2.0.2', 'b91c6fa900905f9a96b86c3e141e2754')

    depends_on('py-setuptools', type='build')
    depends_on('py-six@1.9.0:', type=('build', 'run'))
