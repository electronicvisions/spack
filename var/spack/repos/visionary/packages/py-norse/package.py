# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNorse(PythonPackage):
    """A deep learning library for spiking neural networks."""

    homepage = "https://norse.github.io/norse/"
    pypi = "norse/norse-0.0.7.post1.tar.gz"

    version('1.1.0', sha256='3f70b8579251316761f7a950680136029fcd9d92bbcc53531366d088a8aaf0c8')
    version('0.0.7.post1', sha256='aeea3bd08f47fcfe3b301f1190928dec482938956a1ab8ba568851deed94bda5')

    depends_on('python@3.8.0:', when='@1.1.0', type=('build', 'run'))
    depends_on('python@3.7.0:', when='@0.0.7.post1', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-torch@2.0.0:', when='@1.1.0', type=('build', 'run'))
    depends_on('py-torch@1.9.0:', when='@0.0.7.post1', type=('build', 'run'))
    depends_on('py-torchvision@0.15.0:', when='@1.1.0', type=('build', 'run'))
    depends_on('py-torchvision@0.10.0:', when='@0.0.7.post1', type=('build', 'run'))
    depends_on('py-setuptools@64:', when='@1.1.0', type=('build'))
    depends_on('py-setuptools', when='@0.0.7.post1', type=('build', 'run'))
    depends_on('py-setuptools-scm@8:', when='@1.1.0', type=('build'))
    depends_on('py-pybind11', type=('build', 'link', 'run'))
    depends_on('py-nir', when='@1.1.0', type=('build', 'run'))
    depends_on('py-nirtorch', when='@1.1.0', type=('build', 'run'))

    def setup_build_environment(self, env):
        include = []
        library = []
        for dep in self.spec.dependencies(deptype='link'):
            query = self.spec[dep.name]
            include.extend(query.headers.directories)
            if 'py-pybind11' in dep:
                # py-pybind11 does not provide any libraries for spack to
                # find, this raises an error -> fix on py-pybind11 side
                # at some point in the future
                continue
            library.extend(query.libs.directories)
