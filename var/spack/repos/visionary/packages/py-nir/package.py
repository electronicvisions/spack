# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNir(PythonPackage):
    """Neuromorphic Intermediate Representation"""

    homepage = "https://neuroir.org/docs/index.html"
    pypi = "nir/nir-1.0.6.tar.gz"

    version('1.0.6', sha256='ac81a0c3d56803f535f68863fc5ea3b5bbef58adab83291a4b9d30e8ac664f17')

    depends_on('python@3.9:', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-setuptools@61:', type='build')
    depends_on('py-h5py', type=('build', 'run'))
