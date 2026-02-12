# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCocotb(PythonPackage):
    """cocotb is a coroutine based cosimulation library for writing VHDL and Verilog testbenches in Python."""

    homepage = "https://www.cocotb.org"
    pypi = "cocotb/cocotb-2.0.1.tar.gz"

    version('2.0.1', sha256='69887748412ff43e98f8579ad6c0da1f6ff19a94d0c3b4d6da472d8e86784e82')


    depends_on('python@3.6.2:')
    depends_on('py-setuptools', type='build')
    depends_on('py-find-libpython')
