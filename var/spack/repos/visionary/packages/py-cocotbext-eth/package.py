# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCocotbextEth(PythonPackage):
    """Ethernet interface modules for cocotb"""

    homepage = "https://github.com/alexforencich/cocotbext-eth"
    pypi = "cocotbext-eth/cocotbext_eth-0.1.26.tar.gz"

    version('0.1.26', sha256='f6e17d7b4c5b5160d8c49eecf5505b01761dbd8f6b3f66ff68b76ff7fdb17dee')


    depends_on('python@3.6:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cocotb@1.6.0:')
    depends_on('py-cocotbext-axi@0.1.16:')
