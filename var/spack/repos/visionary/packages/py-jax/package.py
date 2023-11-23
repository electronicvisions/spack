# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


# VISIONS: based on spack/0.20.0
class PyJax(PythonPackage):
    """JAX is Autograd and XLA, brought together for high-performance
    machine learning research. With its updated version of Autograd,
    JAX can automatically differentiate native Python and NumPy
    functions. It can differentiate through loops, branches,
    recursion, and closures, and it can take derivatives of
    derivatives of derivatives. It supports reverse-mode
    differentiation (a.k.a. backpropagation) via grad as well as
    forward-mode differentiation, and the two can be composed
    arbitrarily to any order."""

    homepage = "https://github.com/google/jax"
    pypi = "jax/jax-0.2.25.tar.gz"

    # begin VISIONS (modified): bring upstream
    version("0.4.13", sha256="03bfe6749dfe647f16f15f6616638adae6c4a7ca7167c75c21961ecfd3a3baaa")
    version("0.4.9", sha256="1ed135cd08f48e4baf10f6eafdb4a4cdae781f9052b5838c09c91a9f4fa75f09")
    version("0.4.3", sha256="d43f08f940aa30eb339965cfb3d6bee2296537b0dc2f0c65ccae3009279529ae")
    version("0.3.25", sha256="18bea69321cb95ea5ea913adfe5e2c1d453cade9d4cfd0dc814ecba9fc0cb6e3")
    # end VISIONS
    version("0.3.23", sha256="bff436e15552a82c0ebdef32737043b799e1e10124423c57a6ae6118c3a7b6cd")
    version("0.2.25", sha256="822e8d1e06257eaa0fdc4c0a0686c4556e9f33647fa2a766755f984786ae7446")

    # begin VISIONS (modified): bring upstream
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("python@3.8:", when="@0.4:", type=("build", "run"))
    depends_on("python@3.9:", when="@0.4.14:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.22:", when="@0.4.14:", type=("build", "run"))
    depends_on("py-numpy@1.21:", when="@0.4.9:", type=("build", "run"))
    depends_on("py-numpy@1.20:", when="@0.3:", type=("build", "run"))
    depends_on("py-numpy@1.18:", type=("build", "run"))
    depends_on("py-opt-einsum", type=("build", "run"))
    depends_on("py-scipy@1.2.1:", type=("build", "run"))
    depends_on("py-scipy@1.5:", when="@0.3:", type=("build", "run"))
    depends_on("py-scipy@1.7:", when="@0.4.7:", type=("build", "run"))
    depends_on("py-ml-dtypes@0.2.0:", when="@0.4.14:", type=("build", "run"))
    depends_on("py-ml-dtypes@0.1.0:", when="@0.4.9:", type=("build", "run"))
    depends_on("py-ml-dtypes@0.0.3:", when="@0.4.7:", type=("build", "run"))
    depends_on("py-importlib-metadata@4.6:", when="@0.4.11: ^python@:3.9", type="run")
    # end VISIONS

    # See _minimum_jaxlib_version in jax/version.py
    # begin VISIONS (modified): bring upstream
    jax_to_jaxlib = {
        "0.4.14": "0.4.14",
        "0.4.13": "0.4.13",
        "0.4.9": "0.4.7",
        "0.4.3": "0.4.2",
        "0.3.25": "0.3.22",
        "0.3.23": "0.3.15",
        "0.2.25": "0.1.69",
    }
    # end VISIONS

    for jax, jaxlib in jax_to_jaxlib.items():
        # begin VISIONS (modified): bring upstream
        depends_on(f"py-jaxlib@{jaxlib}", when=f"@{jax}", type=("build", "run"))
        # end VISIONS

    # Historical dependencies
    depends_on("py-absl-py", when="@:0.3", type=("build", "run"))
    depends_on("py-typing-extensions", when="@:0.3", type=("build", "run"))
    # begin VISIONS (deleted):
    # depends_on("py-etils+epath", when="@0.3", type=("build", "run"))
    # end VISIONS
