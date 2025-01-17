# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNirtorch(PythonPackage):
    """PyTorch helper module to translate to and from NIR"""

    homepage = "https://neuroir.org/docs/index.html"
    pypi = "nirtorch/nirtorch-1.0.tar.gz"

    version('1.0', sha256='a0a7c485c0cb523a257a68b881c83d3710a471ad896188879a1bb722d47db2bf')

    depends_on('python@3:',type=('build', 'run'))
    depends_on('py-torch', type=('build', 'run'))
    depends_on('py-setuptools@61:', type=('build'))
    depends_on('py-nir', type=('build', 'run'))
