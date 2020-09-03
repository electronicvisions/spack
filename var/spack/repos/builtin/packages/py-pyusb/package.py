# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyusb(PythonPackage):
    """Easy USB access from Python."""

    homepage = "https://github.com/pyusb/pyusb"
    url      = "https://pypi.io/packages/source/p/pyusb/pyusb-1.0.2.tar.gz"

    version('1.0.2', sha256='4e9b72cc4a4205ca64fbf1f3fff39a335512166c151ad103e55c8223ac147362')

    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('libusb', type=('build', 'run'))
