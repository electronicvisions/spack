# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNir(PythonPackage):
    """Neuromorphic Intermediate Representation"""

    homepage = "https://neuroir.org/docs/index.html"
    pypi = "nir/nir-1.0.4.tar.gz"

    version('1.0.1', sha256='82dc90d8ee05ff25d87337a32f308ee07d19d648ede4c4596995f148b72df622')

    depends_on('python@3:',type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-setuptools@61:', type=('build'))
    depends_on('py-h5py', type=('build', 'run'))
