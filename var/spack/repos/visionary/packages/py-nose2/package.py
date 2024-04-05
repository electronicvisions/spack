# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on spack/0.20.0
class PyNose2(PythonPackage):
    """unittest2 with plugins, the succesor to nose"""

    homepage = "https://github.com/nose-devs/nose2"
    pypi = "nose2/nose2-0.9.1.tar.gz"

    # begin VISIONS (added): bring upstream
    version("0.14.1", sha256="7f8f03a21c9de2c33015933afcef72bf8e4a2d5dfec3b40092287de6e41b093a")
    version("0.12.0", sha256="956e79b9bd558ee08b6200c05ad2c76465b7e3860c0c0537686089285c320113")
    # end VISIONS
    version("0.9.1", sha256="0ede156fd7974fa40893edeca0b709f402c0ccacd7b81b22e76f73c116d1b999")
    version("0.6.0", sha256="daa633e92a52e0db60ade7e105a2ba5cad7ac819f3608740dcfc6140b9fd0a94")

    # begin VISIONS (modified): bring upstream
    depends_on("python@3.6:", type="build", when="@0.13:")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@61:", type="build", when="@0.13:")  # pyproject.toml support

    depends_on("py-six@1.7:", type=("build", "run"), when="@:0.11")
    depends_on("py-cov-core@1.12:", type=("build", "run"), when="@0.6.0:0.6.5")
    depends_on("py-coverage@4.4.1:", type=("build", "run"), when="@0.7.0:0.11")
    # end VISIONS
