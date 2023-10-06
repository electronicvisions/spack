# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPytorchIgnite(PythonPackage):
    """
    A lightweight library to help with training neural networks in PyTorch.
    """

    homepage = "https://github.com/pytorch/ignite"
    url      = "https://pypi.io/packages/source/p/pytorch-ignite/pytorch-ignite-0.3.0.tar.gz"

    version('0.3.0', sha256='d39ec25cf592308d6c30bb10f1bc5038fc68ad20c8639750ac504d9e8b25074c')

    depends_on('python@3.5:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-torch',      type=('build', 'run'))
