# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class F27Niklas(BundlePackage):
    """Software environment definition for niklas@F27"""

    version('1.0')  # Dummy

    depends_on('blas')
    depends_on('boost')
    depends_on('cmake')
    depends_on('cuda@11')
