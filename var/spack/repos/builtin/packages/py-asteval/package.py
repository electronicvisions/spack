# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyAsteval(PythonPackage):
    """Safe, minimalistic evaluator of python expression using ast module"""

    homepage = "http://github.com/newville/asteval"
    pypi = "asteval/asteval-0.9.18.tar.gz"

    version('0.9.18', sha256='5d64e18b8a72c2c7ae8f9b70d1f80b68bbcaa98c1c0d7047c35489d03209bc86')
    version('0.9.16', sha256='bc71bb4f9ad3ef8ccdc3b9a711e094fb00d768172cb7ff9a15773673aac9e0cc')

    depends_on('python@3.5:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
