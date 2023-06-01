# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyScapy(PythonPackage):
    """Scapy: interactive packet manipulation tool"""

    homepage = "https://scapy.net/"
    pypi = "scapy/scapy-2.5.0.tar.gz"

    version('2.5.0', sha256='5b260c2b754fd8d409ba83ee7aee294ecdbb2c235f9f78fe90bc11cb6e5debc2')

    depends_on('python@2.7:2,3.4:3')
    depends_on('py-setuptools', type='build')
