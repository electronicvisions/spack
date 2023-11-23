# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


# VISIONS: based on spack/0.21.0
class PyMlDtypes(PythonPackage):
    """A stand-alone implementation of several NumPy dtype extensions
    used in machine learning libraries."""

    homepage = "https://github.com/jax-ml/ml_dtypes"
    pypi = "ml_dtypes/ml_dtypes-0.3.1.tar.gz"
    git = "https://github.com/jax-ml/ml_dtypes.git"
    submodules = True

    version("0.3.1", tag="v0.3.1", commit="bbeedd470ecac727c42e97648c0f27bfc312af30")
    version("0.2.0", tag="v0.2.0", commit="5b9fc9ad978757654843f4a8d899715dbea30e88")

    # begin VISIONS (modified): bring upstream
    depends_on("python@3.7:")
    depends_on("python@3.9:", when="@0.3:", type=("build", "link", "run"))
    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-numpy@1.21.2:", when="^python@3.10:", type=("build", "run"))
    depends_on("py-numpy@1.23.3:", when="^python@3.11:", type=("build", "run"))
    depends_on("py-numpy@1.26.0:", when="^python@3.13:", type=("build", "run"))
    # end VISIONS
    # Build dependencies are overconstrained, older versions work just fine
    depends_on("py-pybind11", type=("build", "link"))
    depends_on("py-setuptools", type="build")

    # begin VISIONS (added): bring upstream
    patch('setup_py.patch')

    def install(self, spec, prefix):
    # Note: pip install doesn't install the python sources, probably a setuptool version issue
        python('setup.py', 'install', '--prefix=' + prefix,
               *self.install_options(spec, prefix))
    # end VISIONS
