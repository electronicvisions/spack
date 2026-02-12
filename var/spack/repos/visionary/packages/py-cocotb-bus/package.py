# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCocotbBus(PythonPackage):
    """Pre-packaged testbenching tools and reusable bus interfaces for cocotb"""

    homepage = "https://www.cocotb.org"
    pypi = "cocotb-bus/cocotb_bus-0.3.0.tar.gz"

    version('0.3.0', sha256='9762b29273ff062f52160e57274e3cb106d14e7e776515de1372c1d73546b005')

    depends_on('python@3.6.2:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cocotb@1.6.0:')
    depends_on('py-scapy')
