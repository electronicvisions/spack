# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on EBRAINS/25-02
class PyIpycanvas(PythonPackage):
    """Interactive Canvas in Jupyter."""

    # begin VISIONS (modified)
    homepage = "https://github.com/jupyter-widgets-contrib/ipycanvas"
    # end VISIONS
    pypi = "ipycanvas/ipycanvas-0.9.0.tar.gz"

    license("BSD-3-Clause")

    # begin VISIONS (added)
    version("0.13.3", sha256="4e867c509b01f5c4cfc009f7d921e32e5a12a029ac856e78c04ff15b65692c4a")
    # end VISIONS
    # begin EBRAINS (added): add version
    version("0.12.0", sha256="3984339cef0c15674e347dd65ffb0cd1edc62e37869cbb5efea46f3259e976f3")
    # end EBRAINS
    version("0.10.2", sha256="a02c494834cb3c60509801172e7429beae837b3cb6c61d3becf8b586c5a66004")
    version("0.9.0", sha256="f29e56b93fe765ceace0676c3e75d44e02a3ff6c806f3b7e5b869279f470cc43")

    depends_on("python@3.5:", type=("build", "run"))
    # begin EBRAINS (added)
    depends_on("python@3.6:", when="@0.10:", type=("build", "run"))
    depends_on("python@3.7:", when="@0.11:", type=("build", "run"))
    depends_on('py-jupyter-core', type=("build", "run"))
    # end EBRAINS
    # begin VISIONS (modified)
    depends_on("py-ipywidgets@7.6:9", type=("build", "run"))
    depends_on("pil@6:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    with default_args(type="build", when="@0.13.2:"):
        depends_on("py-hatchling")
        depends_on("py-hatch-jupyter-builder@0.8.1:")
        depends_on("py-jupyterlab@3.0:4")
        depends_on("yarn")  # see pyproject.toml: ipycanvas uses yarn instead of npm

    with default_args(type="build", when="@:0.13.1"):
        depends_on("py-setuptools@40.8:")
        depends_on("py-jupyter-packaging@0.7")
        depends_on("py-jupyterlab@3.0:3")
    # end VISIONS
