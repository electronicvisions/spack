# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gecode(AutotoolsPackage):
    """Generic constraint development environment."""

    homepage = "https://www.gecode.org"
    url      = "https://github.com/Gecode/gecode/archive/release-6.2.0.tar.gz"

    version('6.2.0', sha256='27d91721a690db1e96fa9bb97cec0d73a937e9dc8062c3327f8a4ccb08e951fd')

    depends_on('m4',       type='build')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
