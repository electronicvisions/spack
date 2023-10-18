# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VisionaryNmpi(BundlePackage):
    """
    Visionary Meta Package which bundels packages needed to provide the nmpi jobrunner.
    """

    version('1.0')

    depends_on('py-hbp-neuromorphic-platform')
    depends_on('py-pandas')
    depends_on('py-psutil')
