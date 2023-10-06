# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySbi(PythonPackage):
    """
    sbi is a PyTorch package for simulation-based inference. Simulation-based inference is
    the process of finding parameters of a simulator from observations.

    sbi takes a Bayesian approach and returns a full posterior distribution over the parameters, conditional on the observations.
    This posterior can be amortized (i.e. useful for any observation) or focused (i.e. tailored to a particular observation),
    with different computational trade-offs.
    """

    pypi = "sbi/sbi-0.21.0.tar.gz"
    homepage = "https://github.com/mackelab/sbi"

    version("0.21.0", sha256="154f30bc15df437a657311c393d6227d146c57d9430691cc7bd6f480136efb2f")
    version("0.20.0", sha256="a962d3bc6d79a001903c7b12bda6fe2bba944e3b05888aa25fc87f7051f2db5f")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))

    depends_on("py-arviz", type=("build", "run"))
    depends_on("py-joblib@1.0.0:", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-pyknos@0.15.1:", type=("build", "run"))
    depends_on("py-pyro-ppl@1.3.1:", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tensorboard", type=("build", "run"))
    depends_on("py-torch@1.8.0:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
