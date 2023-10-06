# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class PySphinxcontribJupyter(PythonPackage):
    """A Sphinx Extension for Generating Jupyter Notebooks."""

    homepage = "https://sphinxcontrib-jupyter.readthedocs.io"
    url      = "https://github.com/QuantEcon/sphinxcontrib-jupyter/archive/v0.5.10.tar.gz"

    version('0.5.10', sha256='6eb4bc2b5c62a5dff6972e91c723c09fb84b82f44b68d32f471799722122aa89')

    depends_on('python@2.7:2.8,3.3:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-sphinx', type=('build', 'run'))
    depends_on('py-docutils', type=('build', 'run'))
    depends_on('py-nbformat', type=('build', 'run'))
    depends_on('py-sphinx', type=('build', 'run'))
    depends_on('py-dask', type=('build', 'run'))
    depends_on('py-distributed', type=('build', 'run'))
    depends_on('py-ipython', type=('build', 'run'))
    depends_on('py-nbconvert', type=('build', 'run'))
    depends_on('py-jupyter-client', type=('build', 'run'))

    # patch away dependency on pip
    patch('init_pip.patch', when='@0.4.0:')
    # support for solution images (see: https://github.com/QuantEcon/sphinxcontrib-jupyter/pull/337)
    patch('solution_images.patch', when='@0.5.10:')
