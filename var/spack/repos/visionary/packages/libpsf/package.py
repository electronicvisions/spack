# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.builtin.boost import Boost


class Libpsf(AutotoolsPackage):
    """PSF simulation data c++ library."""

    homepage = "https://gitlab.com/libpsf/libpsf-core"
    git      = "https://gitlab.com/libpsf/libpsf-core"

    version('0.2', commit='001dc734e01725e739847c8cde6480a0cf35a082')

    # option suggested by build instructions in repo
    autoreconf_extra_args = ["-Im4"]
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on(Boost.with_default_variants)
