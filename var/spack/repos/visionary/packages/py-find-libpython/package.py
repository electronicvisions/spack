# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyFindLibpython(PythonPackage):
    """Finds the libpython associated with your environment, wherever it may be hiding"""

    homepage = "https://github.com/ktbarrett/find_libpython"
    pypi = "find-libpython/find_libpython-0.3.0.tar.gz"

    version('0.3.0', sha256='6e7fe5d9af7fad6dc066cb5515a0e9c90a71f1feb2bb2f8e4cdbb4f83276e9e5')

    depends_on('py-setuptools@42:', type='build')
    # taken from the development branch of spack
    depends_on("py-setuptools-scm+toml", when="@:0.3.0", type="build")
