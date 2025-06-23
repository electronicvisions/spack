# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNir(PythonPackage):
    """Neuromorphic Intermediate Representation"""

    homepage = "https://neuroir.org/docs/index.html"
    pypi = "nir/nir-1.0.5.tar.gz"

    version('1.0.5', sha256='dd90022cfd60443cdcd848852190f5425776db113708b3ecdf621d3da8d4bf33')

    depends_on('python@3.9:', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-setuptools@61:', type='build')
    depends_on('py-h5py', type=('build', 'run'))
