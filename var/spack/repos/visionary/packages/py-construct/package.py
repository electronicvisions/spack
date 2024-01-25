# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyConstruct(PythonPackage):
    """Construct is a powerful declarative and symmetrical parser and builder for binary data."""

    homepage = "https://construct.readthedocs.org/"
    pypi = "construct/construct-2.10.70.tar.gz"

    version('2.10.70', sha256='2e3a01162d1c653d7bc6cd5a15f55420b3384388')


    depends_on('python@3.6:')
    depends_on('py-setuptools', type='build')
