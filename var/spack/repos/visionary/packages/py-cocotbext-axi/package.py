# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCocotbextAxi(PythonPackage):
    """AXI, AXI lite, and AXI stream modules for cocotb"""

    homepage = "https://github.com/alexforencich/cocotbext-axi"
    pypi = "cocotbext-axi/cocotbext_axi-0.1.28.tar.gz"

    version('0.1.28', sha256='5d062185b9bb5476839a1d816821c4533b245f56f7b171b3f39130e26891ae37')
    patch('0001-axi-ID-signal-is-optional.patch', sha256='81f29fceb97a888c08d1e7008479159bac6077a0dbb38ba7f44a5e8035c7e0f5')


    depends_on('python@3.6:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cocotb@1.6.0:')
    depends_on('py-cocotb-bus')
