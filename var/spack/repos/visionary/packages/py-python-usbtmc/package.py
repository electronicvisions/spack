# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPythonUsbtmc(PythonPackage):
    """ Python USBTMC driver for controlling instruments over USB."""

    homepage = "https://github.com/python-ivi/python-usbtmc"
    url      = "https://pypi.io/packages/source/p/python-usbtmc/python-usbtmc-0.8.tar.gz"

    version('0.8', sha256='510658781dd94a38d86c6f742a338a5a737af76c71ed15718088cbee9aeb0ba7')

    depends_on('py-pyusb', type=('build', 'run'))
