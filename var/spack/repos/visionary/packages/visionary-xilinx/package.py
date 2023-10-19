# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VisionaryXilinx(BundlePackage):
    """Visionary Meta Package tracking runtime dependencies of xilinx module"""

    version('1.0')

    depends_on('fontconfig', type='run')
    depends_on('glib', type='run')
    depends_on('libice', type='run')
    depends_on('libsm', type='run')
    depends_on('libxi', type='run')
    depends_on('libxrandr', type='run')
    depends_on('libxrender', type='run')
    depends_on('libxtst', type='run')
    depends_on('libxcursor', type='run')
    depends_on('libxft', type='run')
