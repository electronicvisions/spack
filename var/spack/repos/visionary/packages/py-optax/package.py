# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on spack@0.23.1
class PyOptax(PythonPackage):
    """A gradient processing and optimisation library in JAX."""

    homepage = "https://github.com/deepmind/optax"
    pypi = "optax/optax-0.1.7.tar.gz"

    license("Apache-2.0")

    version("0.2.1", sha256="fc9f430fa057377140d00aa50611dabbd7e8f4999e3c7543f641f9db6997cb1a")
    version("0.1.7", sha256="6a5a848bc5e55e619b187c749fdddc4a5443ea14be85cc769f995779865c110d")
    # begin VISIONS (added): bring upstream
    version("0.1.4", sha256="fb7a0550d57a6636164a3de25986a8a19be8ff6431fcdf1225b4e05175810f22")
    # end VISIONS

    depends_on("python@3.9:", when="@0.2.1:", type=("build", "run"))
    # begin VISIONS (modify): upper bound
    depends_on("python@3.8:", when="@:0.1.7", type=("build", "run"))
    # end VISIONS

    # begin VISIONS (added)
    depends_on("py-setuptools", when="@0.1.4", type="build")
    # end VISIONS

    depends_on("py-flit-core@3.2:3", type="build")
    depends_on("py-absl-py@0.7.1:", type=("build", "run"))
    depends_on("py-chex@0.1.7:", when="@0.2.1:", type=("build", "run"))
    # begin VISIONS (modify): lower bound
    depends_on("py-chex@0.1.5:", when="@0.1.4:", type=("build", "run"))
    # end VISIONS
    depends_on("py-jax@0.1.55:", type=("build", "run"))
    depends_on("py-jaxlib@0.1.37:", type=("build", "run"))
    depends_on("py-numpy@1.18.0:", type=("build", "run"))
