# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMarkdownItPy(PythonPackage):
    """Python port of markdown-it. Markdown parsing, done right!"""

    homepage = "https://markdown-it-py.readthedocs.io/en/latest/"
    pypi = "markdown-it-py/markdown-it-py-1.1.0.tar.gz"

    version('1.1.0', sha256='36be6bb3ad987bfdb839f5ba78ddf094552ca38ccbd784ae4f74a4e1419fc6e3')

    depends_on('python@3.6.0:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-attrs@19.0.0:21.999.999', type=('build', 'run'))
    depends_on('py-typing-extensions@3.7.4:', type=('build', 'run'), when='^python@:3.7.999')
