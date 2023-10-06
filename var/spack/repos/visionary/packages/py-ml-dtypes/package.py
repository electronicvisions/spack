# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMlDtypes(PythonPackage):
    """ml_dtypes is a stand-alone implementation of several NumPy dtype
    extensions used in machine learning libraries."""

    homepage = "https://github.com/jax-ml/ml_dtypes"
    pypi = "ml_dtypes/ml_dtypes-0.1.0.tar.gz"

    version("0.1.0", sha256="c1fc0afe63ce99069f9d7e0693a61cfd0aea90241fc3821af9953d0c11f4048a")

    patch('setup_py.patch')

    depends_on("python@3.7:")
    depends_on("py-setuptools", type="build") # ~=67.7.0
    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-numpy@1.21.2:", when="^python@3.9:", type=("build", "run"))
    depends_on("py-numpy@1.23.3:", when="^python@3.10:", type=("build", "run"))
    depends_on("py-pybind11@2.10.0:", type="build") # ~=2.10.0

    def install(self, spec, prefix):
    # Note: pip install doesn't install the python sources, probably a setuptool version issue
        python('setup.py', 'install', '--prefix=' + prefix,
               *self.install_options(spec, prefix))
