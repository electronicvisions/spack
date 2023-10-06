# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPythonEngineio(PythonPackage):
    """Engine.IO is the implementation of transport-based
    cross-browser/cross-device bi-directional communication
    layer for Socket.IO."""

    homepage = "https://python-engineio.readthedocs.io/en/latest/"
    url      = "https://github.com/miguelgrinberg/python-engineio/archive/v2.0.2.tar.gz"

    version('3.3.0',
            sha256='e4ac17c04c32ccca67287dfdbbe4ee1e9eec3a0a1a9a6070f3ab784db08407dd',
            url='https://files.pythonhosted.org/packages/2f/09/83d627ad3dadd064bfb875c7767e93f3568354fe82cebe298b4e07f79238/python-engineio-3.3.0.tar.gz')
    version('2.0.2', sha256='9fbe531108a95bc61518b61c4718e2661fc81d32b54fd6af34799bf10a367a6b')

    depends_on('py-setuptools', type='build')
    depends_on('py-six@1.9.0:', type=('build', 'run'))
