# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Maturin(Package):
    """Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages"""

    homepage = "https://github.com/PyO3/maturin"
    url      = "https://pypi.io/packages/source/m/maturin/maturin-0.10.6.tar.gz"

    version('0.10.6', sha256='bd39f7e08eb9908d4fe1cd9b3c953fad5b1fb4fec9c82d14c2973a65751e1899')

    depends_on('rust', type='build')
    depends_on('python', type='run')

    def install(self, spec, prefix):
        cargo = which('cargo')
        cargo('install', '--root', prefix, '--path', '.')
