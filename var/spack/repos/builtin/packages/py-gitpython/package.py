# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class PyGitpython(PythonPackage):
    """
    GitPython is a python library used to interact with Git repositories.
    """

    homepage = "https://github.com/gitpython-developers/GitPython"
    url      = "https://pypi.io/packages/source/G/GitPython/GitPython-3.1.3.tar.gz"

    version('3.1.3', sha256='e107af4d873daed64648b4f4beb89f89f0cfbe3ef558fc7821ed2331c2f8da1a')

    depends_on('py-setuptools', type='build')
    depends_on('python@3.4:', type=('build', 'run'))
    depends_on('py-gitdb@4.0.1:4.999', type=('build', 'run'))
    # tests require additional dependencies
