# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyUmnn(PythonPackage):
    """Implementation of Unconstrained Monotonic Neural Networks (UMNN)

    Provides the implementation of Unconstrained Monotonic Neural Networks
    (UMNN) and implements experiments descriped in [1].

    [1] Antoine Wehenkel and Gilles Louppe.
        "Unconstrained Monotonic Neural Networks." (2019) [arXiv]

    """

    homepage = "https://github.com/awehenkel/umnn"
    pypi = "UMNN/UMNN-1.68.tar.gz"

    version("1.68", sha256="1e79aea82a0fcb54cec61afcc672d437df1adef0f04f7f1491d499ecd9c3afb8")

    # no requirements.txt present. Extracted dependencies from README and
    # source code
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-torch@1.1:", type=("build", "run"))
