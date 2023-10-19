# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VisionaryWaferVisu(BundlePackage):
    """Visionary Meta Package"""
    version('1.0')

    depends_on("emscripten")
    depends_on("py-numpy")
