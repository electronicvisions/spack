# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyIpycanvas(PythonPackage):
    """Interactive widgets library exposing the browser's Canvas API"""

    homepage = "https://github.com/martinRenou/ipycanvas"
    pypi     = "ipycanvas/ipycanvas-0.8.2.tar.gz"

    version('0.8.2', sha256='45ca524d90d158a5e884e146a10885f853d5a352e547e7b1eb5329230c9eff02')

    depends_on('python@3.5:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-jupyter-packaging', type='build')
    depends_on('py-ipywidgets@7.6.0:', type=('build', 'run'))
    depends_on('py-pillow@6.0:', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-orjson', type=('build', 'run'))
