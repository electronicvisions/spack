# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyknos(PythonPackage):
    """
    Python package for conditional density estimation. It either wraps or implements diverse conditional density estimators.
    """

    homepage = "https://github.com/mackelab/pyknos"
    pypi = "pyknos/pyknos-0.15.1.tar.gz"

    version("0.15.1", sha256="d1cdd1ee14d913a5a6a656378908256e0df7273cc8be2316e1c46db042ed4751")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))

    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-nflows@0.14", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tensorboard", type=("build", "run"))
    depends_on("py-torch@1.5.1:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
