# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCocotb(PythonPackage):
    """cocotb is a coroutine based cosimulation library for writing VHDL and Verilog testbenches in Python."""

    homepage = "https://www.cocotb.org"
    pypi = "cocotb/cocotb-1.7.2.tar.gz"

    version('1.7.2', sha256='959892eb94bd0b3ff40e0fca51d33a3936416deb853e2bac4f7f766b40002650')


    depends_on('python@3.6:')
    depends_on('py-setuptools', type='build')
    depends_on('py-find-libpython')
