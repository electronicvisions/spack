# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCocotbBus(PythonPackage):
    """Pre-packaged testbenching tools and reusable bus interfaces for cocotb"""

    homepage = "https://www.cocotb.org"
    pypi = "cocotb-bus/cocotb-bus-0.2.1.tar.gz"

    version('0.2.1', sha256='a197aa4b0e0ad28469c8877b41b3fb2ec0206da9f491b9276d1578ce6dd8aa8d')
    patch('case.patch', sha256='16e11f5a9b45733163da253b89dfaec22c6440f281c147a6e39ac597ba99b3e5')
    patch('integer.patch', sha256='72151f003decff73bee02dd9928863b63dca556ebe4ee4a66bcf912efa48a353')

    depends_on('python@3.5:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cocotb@1.5.0.dev:1')
