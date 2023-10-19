# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VisionaryClusterservices(BundlePackage):
    """
    Visionary Meta Package to make sure the dependecies for all visionary cluster services
    are built.
    """

    version('1.0')

    depends_on('visionary-slurmviz')
    depends_on('visionary-unicore')
