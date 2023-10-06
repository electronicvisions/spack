# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyOptax(PythonPackage):
    """Optax is a gradient processing and optimization library for JAX."""

    homepage = "https://github.com/deepmind/optax"
    pypi = "optax/optax-0.1.4.tar.gz"

    version("0.1.4", sha256="fb7a0550d57a6636164a3de25986a8a19be8ff6431fcdf1225b4e05175810f22")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-absl-py@0.7.1:", type=("build", "run"))
    depends_on("py-chex@0.1.5:", type=("build", "run"))
    depends_on("py-jax@0.1.55:", type=("build", "run"))
    depends_on("py-jaxlib@0.1.37:", type=("build", "run"))
    depends_on("py-numpy@1.18:", type=("build", "run"))
