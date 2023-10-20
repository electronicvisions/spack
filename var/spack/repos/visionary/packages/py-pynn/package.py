# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on spack/0.20.0
class PyPynn(PythonPackage):
    """A Python package for simulator-independent specification of neuronal
    network models
    """

    homepage = "https://neuralensemble.org/PyNN/"
    pypi = "PyNN/PyNN-0.8.3.tar.gz"
    git = "https://github.com/NeuralEnsemble/PyNN.git"

    # begin VISIONS (modified): bring upstream
    version("0.10.1", sha256="03fbafeddd64ae7163e2b557b2760380b6eceb52469f1b3f4cc203bbb80f0cde")
    version("0.10.0", sha256="04120fe0e03260d664b337e0ac29d985c3fb3684ef35b1add93a66739891c98f")
    version("0.9.6", sha256="d85226800e30bc1692d3f84485c3fa20b921c2ab55f1201d0a3bf23432e16cd2")
    # end VISIONS
    version("0.9.1", sha256="bbc60fea3235427191feb2daa0e2fa07eb1c3946104c068ac8a2a0501263b0b1")
    version("0.8.3", sha256="9d59e6cffa4714f0c892ec6b32d1f5f8f75ba3a20d8635bac50c047aa6f2537e")
    version("0.8beta", commit="ffb0cb1661f2b0f2778db8f71865978fe7a7a6a4")
    version("0.8.1", sha256="ce94246284588414d1570c1d5d697805f781384e771816727c830b01ee30fe39")
    version("0.7.5", sha256="15f75f422f3b71c6129ecef23f29d8baeb3ed6502e7a321b8a2596c78ef7e03c")

    depends_on("python@2.6:2.8,3.3:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"), when="@0.10.0:")

    # begin VISIONS (modified): bring upstream
    # pip silently replaces distutils with setuptools
    depends_on("py-setuptools", type="build")
    depends_on("py-jinja2@2.7:", type=("build", "run"))
    depends_on("py-docutils@0.10:", type=("build", "run"))

    depends_on("py-numpy@1.5:", type=("build", "run"))
    depends_on("py-numpy@1.16.1:", type=("build", "run"), when="@0.10.0")
    depends_on("py-numpy@1.18.5:", type=("build", "run"), when="@0.10.1:")

    depends_on("py-quantities@0.10:", type=("build", "run"))
    depends_on("py-quantities@0.12.1:", type=("build", "run"), when="@0.10.0:")

    depends_on("py-lazyarray@0.2.9:", type=("build", "run"))
    depends_on("py-lazyarray@0.5.0:", type=("build", "run"), when="@0.10.0")
    depends_on("py-lazyarray@0.5.2:", type=("build", "run"), when="@0.10.1:")

    depends_on("py-neo@0.3:0.4.1", type=("build", "run"), when="@:0.8.3")
    depends_on("py-neo@0.5.0:0.8.0", type=("build", "run"), when="@0.9.0:0.9.6")
    depends_on("py-neo@0.10.0", type=("build", "run"), when="@0.10.0")
    depends_on("py-neo@0.11.0:", type=("build", "run"), when="@0.10.1:")
    # end VISIONS

    # begin VISIONS (added): bring upstream
    depends_on("py-mock@1.0:", type="test")

    patch("pynn-0.9.6-python3.patch", when="@0.9.6 ^python@3:")
    # end VISIONS
