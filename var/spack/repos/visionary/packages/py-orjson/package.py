# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from glob import glob


class PyOrjson(Package):
    """Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy"""

    # This Py* package is a bit special, which makes it different from other Python
    # packages:
    # * orjson has to be built with rust + maturin. Maturin supports building of wheels
    #   and sdists (but sdist build of orjson is somehow broken, didn't investigate
    #   further). The standard way seems to be to build a wheel and subsequently install
    #   it with pip, which is done here.
    # * TODO: orjson depends on rust nightly at the moment
    #   (cf. https://github.com/ijl/orjson/issues/108), we should update if this gets
    #   fixed and remove pinned nightly rust, too.

    homepage = "https://github.com/ijl/orjson"
    url      = "https://pypi.io/packages/source/o/orjson/orjson-3.5.3.tar.gz"

    version('3.5.3', sha256='8818f651ef7ed55f7c0ee34fa51f3de0988dd35386e8cefd0c2e1f32ff9f1966')

    extends('python')
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-pip', type='build')
    depends_on('rust@nightly.2021-05-25', type='build')
    depends_on('maturin@0.10.6:0.10.999', type='build')

    phases = ['build', 'install']

    def build(self, spec, prefix):
        maturin = which('maturin')
        python = which('python')
        maturin(
            'build',
            '--no-sdist',
            '--release',
            '--strip',
            '--manylinux', 'off',
            '--interpreter', python.path,
        )

    def install(self, spec, prefix):
        pip = which('pip')
        pip('install', glob('./target/wheels/*.whl')[0], '--prefix={0}'.format(prefix))
