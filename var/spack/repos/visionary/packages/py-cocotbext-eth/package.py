# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCocotbextEth(PythonPackage):
    """Ethernet interface modules for cocotb"""

    homepage = "https://github.com/alexforencich/cocotbext-eth"
    pypi = "cocotbext-eth/cocotbext-eth-0.1.20.tar.gz"

    version('0.1.22', sha256='9cabbefd0003010692f0b5140b09d9f08f79c634')


    depends_on('python@3.6:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cocotb@1.6.0:')
    depends_on('py-cocotbext-axi@0.1.16:')
