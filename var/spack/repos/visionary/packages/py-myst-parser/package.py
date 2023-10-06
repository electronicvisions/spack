# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMystParser(PythonPackage):
    """An extended CommonMark-compliant parser, with bridges to Docutils and
    Sphinx."""

    homepage = "https://myst-parser.readthedocs.io"
    pypi = "myst-parser/myst-parser-0.14.tar.gz"

    version('0.14.0', sha256='fc262959a74cdc799d7fa9b30c320c17187485b9a1e8c39e988fc12f3adff63c')

    depends_on('python@3.6.0:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')

    depends_on('py-sphinx@2.1:3.999.999', type=('build', 'run'))
    depends_on('py-docutils@0.15:,0.17.999', type=('build', 'run'))
    # py-jinja2 is mentioned in package's dependencies but comes via py-sphinx
    depends_on('py-markdown-it-py@1.0.0:1.999.999', type=('build', 'run'))
    depends_on('py-mdit-py-plugins@0.2.8:', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
