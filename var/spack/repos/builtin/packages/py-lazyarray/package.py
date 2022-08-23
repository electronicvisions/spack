# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyLazyarray(PythonPackage):
    """a Python package that provides a lazily-evaluated numerical array class,
    larray, based on and compatible with NumPy arrays."""

    homepage = "http://bitbucket.org/apdavison/lazyarray/"
    pypi = "lazyarray/lazyarray-0.2.8.tar.gz"

    version("0.5.2", sha256="fe31804d82115ed7c382840a1708f498419ec1455cac084707ece9908310c7d1")
    version("0.5.0", sha256="4cc4b54940def52fd96818a1c10528c4b7ecca77aa617d9e4fecfb42b51e73cf")
    version('0.3.2',  sha256='be980534c5950a976709085570f69be9534bdf0f3e5c21a9113de3ee2052683e')
    version('0.2.10', sha256='7a53f81b5f3a098c04003d2ad179fc197451fd96bc921510f8534c6af8cc8e19')
    version('0.2.8',  sha256='aaee4e18117cc512de7a4e64522f37bc6f4bf125ecffdbdbf4e4e390fbdd9ba2')

    depends_on("python@3.4:3.9", type=("build", "run"), when="@0.5.0:")
    depends_on("python@3.4:3.10", type=("build", "run"), when="@0.5.2:")
    depends_on('py-numpy@1.3:', type=('build', 'run'))
    depends_on('py-numpy@1.5:', type=('build', 'run'), when='^python@3:')
    depends_on("py-numpy@1.12:", type=("build", "run"), when="@0.3:0.5.0^python@3:")
    depends_on('py-numpy@1.13:', type=('build', 'run'), when='@0.5.2:')
