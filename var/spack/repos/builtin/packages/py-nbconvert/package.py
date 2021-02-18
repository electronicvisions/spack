# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack import *


class PyNbconvert(PythonPackage):
    """Jupyter Notebook Conversion"""

    homepage = "https://github.com/jupyter/nbconvert"
    url      = "https://github.com/jupyter/nbconvert/archive/4.2.0.tar.gz"

    version('5.5.0', sha256='93721d772361d1cd59502dacfb76c4122359b1c321cea1882451532a2db02d59')
    version('5.4.1', sha256='9a187e1b9269c248b5debc5bd89cfb0d3bfac2a1d0f17df8e94a5ae8d2d92353')
    version('4.2.0', sha256='32394be5a20f39f99fabfb9b2f2625df17f1c2a6699182ca41598e98e7cc9610')
    version('4.1.0', sha256='459f23381411fd1ff9ec5ed71fcd56b8c080d97b3a1e47dae1c5c391f9a47266')
    version('4.0.0', sha256='00e25eeca90523ba6b774b289073631ef5ac65bb2de9774e9b7f29604516265c')

    depends_on('py-pycurl', type='build')
    depends_on('python@2.7:2.8,3.3:')
    depends_on('py-mistune@0.8.1:', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'), when='@:5.4.999')
    depends_on('py-jinja2@2.4:', type=('build', 'run'), when='@5.5.0:')
    depends_on('py-pygments', type=('build', 'run'))
    depends_on('py-traitlets@4.2:', type=('build', 'run'))
    depends_on('py-jupyter-core', type=('build', 'run'))
    depends_on('py-nbformat@4.4:', type=('build', 'run'))
    depends_on('py-entrypoints@0.2.2:', type=('build', 'run'))
    depends_on('py-tornado', type=('build', 'run'))
    depends_on('py-jupyter-client', type=('build', 'run'))

    depends_on('py-setuptools', type='build', when='@5:')
    depends_on('py-bleach', type=('build', 'run'), when='@5:')
    depends_on('py-pandocfilters', type=('build', 'run'), when='@5.0.0:5.4.999')
    depends_on('py-pandocfilters@1.4.1:', type=('build', 'run'), when='@5.5.0:')
    depends_on('py-defusedxml', type=('build', 'run'), when='@5:')
    depends_on('py-testpath', type=('build', 'run'), when='@5:')

    def patch(self):
        # We bundle this with the spack package so that the installer
        # doesn't try to download it.
        install(os.path.join(self.package_dir, 'style.min.css'),
                os.path.join('nbconvert', 'resources', 'style.min.css'))
