# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNflows(PythonPackage):
    """
    nflows is a comprehensive collection of normalizing flows using PyTorch.
    """

    homepage = "https://github.com/bayesiains/nflows"
    pypi = "nflows/nflows-0.14.tar.gz"

    version("0.14", sha256="6299844a62f9999fcdf2d95cb2d01c091a50136bd17826e303aba646b2d11b55")

    depends_on("py-setuptools", type=("build", "run"))

    # no versions for dependencies defined in requirements.txt
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tensorboard", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-umnn", type=("build", "run"))
