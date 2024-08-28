# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on spack/0.20.0
class PyIpycanvas(PythonPackage):
    """Interactive Canvas in Jupyter."""

    homepage = "https://github.com/martinRenou/ipycanvas"
    pypi = "ipycanvas/ipycanvas-0.9.0.tar.gz"

    license("BSD-3-Clause")

    # begin VISIONS (added): bring upstream
    version("0.13.2", sha256="52387d9d87f65955f39552fb7927c445e5e5e4937d853814d910cbe8efa0fb79")
    # end VISIONS
    version("0.10.2", sha256="a02c494834cb3c60509801172e7429beae837b3cb6c61d3becf8b586c5a66004")
    version("0.9.0", sha256="f29e56b93fe765ceace0676c3e75d44e02a3ff6c806f3b7e5b869279f470cc43")

    depends_on("python@3.5:", type=("build", "run"))

    depends_on("py-hatchling", when="@0.13.2:", type="build")
    depends_on("py-hatch-jupyter-builder@0.8.1:", when="@0.13.2:", type="build")
    depends_on("yarn", when="@0.13.2:", type="build")
    depends_on("py-jupyterlab@3.0:5", when="@0.13.2:", type="build")
    depends_on("py-ipywidgets@7.6:8", when="@0.13.2:", type=("build", "run"))
    depends_on("pil@6:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    # Historical dependencies
    depends_on("py-setuptools@40.8:", type="build", when="@:0.13.1")
    depends_on("py-ipywidgets@7.6:", type=("build", "run"))
    depends_on("py-jupyter-packaging@0.7", type="build", when="@:0.13.1")
    depends_on("py-jupyterlab@3.0:3", type="build", when="@:0.13.1")
