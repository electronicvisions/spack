# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyJupyterPackaging(PythonPackage):
    """Jupyter Packaging Utilities."""

    homepage = "https://github.com/jupyter/jupyter-packaging"
    pypi     = "jupyter_packaging/jupyter_packaging-0.9.1.tar.gz"

    version('0.9.1', sha256='6f819759804536f9e563cc8a76a9d8588bb90cd735deaa550a6d8453012b0164')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools@49.4:', type=('build', 'run'))
    depends_on('py-packaging', type=('build', 'run'))
    depends_on('py-wheel', type=('build', 'run'))
    depends_on('py-deprecation', type=('build', 'run'))
    depends_on('py-tomlkit', type=('build', 'run'))
