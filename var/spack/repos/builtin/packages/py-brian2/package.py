# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyBrian2(PythonPackage):
    """A clock-driven simulator for spiking neural networks"""

    homepage = "http://www.briansimulator.org"
    pypi = "Brian2/Brian2-2.2.2.1.tar.gz"

    version('2.3',     sha256='7c725209e0e907876e420477b5c8fef31326820f3e38a46a54dff55d669478b7')
    version('2.2.2.1', sha256='02075f66d42fd243fc5e28e1add8862709ae9fdabaffb69858e6d7f684a91525')
    version('2.1.3.1', sha256='6d8e8a7abdcef6366880a43240ab15daaa1ebfda0c14f84e99d74dba49ec1fc8')
    version('2.0.1',   sha256='195d8ced0d20e9069917776948f92aa70b7457bbc6b5222b8199654402ee1153')
    version('2.0rc3',  sha256='05f347f5fa6b25d1ce5ec152a2407bbce033599eb6664f32f5331946eb3c7d66')

    variant('docs', default=False, description='Build the documentation')

    depends_on('python@2.7:', type=('build', 'run'))
    depends_on('py-numpy@1.10:', type=('build', 'run'))
    depends_on('py-cython@0.29:', type=('build', 'run'))
    depends_on('py-sympy@0.7.6:1.0,1.1.1:', type=('build', 'run'))
    depends_on('py-pyparsing', type=('build', 'run'))
    depends_on('py-jinja2@2.7:', type=('build', 'run'))
    depends_on('py-setuptools@21:', type=('build', 'run'))
    depends_on('py-sphinx@1.5:', type=('build', 'run'), when='+docs')
    depends_on('py-nose@1.0:', type='test')
    # FIXME: Extra depends_on from EV
    depends_on('py-py-cpuinfo@0.1.6:', type=('build', 'run'))

    def build_args(self, spec, prefix):
        return ['--with-cython']
