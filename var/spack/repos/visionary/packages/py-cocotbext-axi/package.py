# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCocotbextAxi(PythonPackage):
    """AXI, AXI lite, and AXI stream modules for cocotb"""

    homepage = "https://github.com/alexforencich/cocotbext-axi"
    pypi = "cocotbext-axi/cocotbext-axi-0.1.24.tar.gz"

    version('0.1.24', sha256='3ed62dcaf9448833176826507c5bc5c346431c4846a731e409d87c862d960593')
    patch('0001-axi-ID-signal-is-optional.patch', sha256='81f29fceb97a888c08d1e7008479159bac6077a0dbb38ba7f44a5e8035c7e0f5')


    depends_on('python@3.6:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cocotb@1.6.0:')
    depends_on('py-cocotb-bus')
