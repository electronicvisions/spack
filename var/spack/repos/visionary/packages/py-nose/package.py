# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on spack/0.20.0
class PyNose(PythonPackage):
    """nose extends the test loading and running features of unittest,
    making it easier to write, find and run tests."""

    pypi = "nose/nose-1.3.4.tar.gz"

    version("1.3.7", sha256="f1bffef9cbc82628f6e7d7b40d7e255aefaa1adb6a1b1d26c69a8b79e6208a98")
    version("1.3.6", sha256="f61e0909a743eed37b1207e38a8e7b4a2fe0a82185e36f2be252ef1b3f901758")
    version("1.3.4", sha256="76bc63a4e2d5e5a0df77ca7d18f0f56e2c46cfb62b71103ba92a92c79fab1e03")

    depends_on("py-setuptools@:57", type="build")

    # begin VISIONS (added): bring upstream
    # https://github.com/nose-devs/nose/pull/1090
    variant("xunit2", default=True, description="Some (in)sane people changed "
                                                "the a variable name, so nose "
                                                "needs a patch (PR 1090)")

    patch("1090.patch", when="+xunit2")
    # end VISIONS
