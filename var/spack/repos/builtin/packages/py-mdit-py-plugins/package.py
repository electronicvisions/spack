# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMditPyPlugins(PythonPackage):
    """Collection of core plugins for markdown-it-py."""

    homepage = "https://mdit-py-plugins.readthedocs.io"
    pypi = "mdit-py-plugins/mdit-py-plugins-0.2.8.tar.gz"

    version('0.2.8', sha256='5991cef645502e80a5388ec4fc20885d2313d4871e8b8e320ca2de14ac0c015f')

    depends_on('python@3.6.0:', type=('build', 'run'))
    depends_on('py-markdown-it-py@1.0:', type=('build', 'run'))
