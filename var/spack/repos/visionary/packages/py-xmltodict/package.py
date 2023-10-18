# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on spack/0.20.0
class PyXmltodict(PythonPackage):
    """xmltodict is a Python module that makes working with XML feel like
    you are working with JSON."""

    homepage = "https://github.com/martinblech/xmltodict"
    pypi = "xmltodict/xmltodict-0.12.0.tar.gz"

    version("0.12.0", sha256="50d8c638ed7ecb88d90561beedbf720c9b4e851a9fa6c47ebd64e99d166d8a21")

    # begin VISIONS (added): bring upstream
    # taken from: https://github.com/martinblech/xmltodict/pull/216
    patch("fix_py3_unicodedecode_error.patch", when="@0.12.0 ^python@3.0.0:")

    depends_on("pkgconfig", type="build")
    # end VISIONS
    depends_on("py-setuptools", type="build")
    depends_on("python@2.7:2.8,3.4:", type=("build", "run"))
