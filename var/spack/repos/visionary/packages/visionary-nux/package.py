# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VisionaryNux(BundlePackage):
    """Visionary Meta Package"""
    version('1.0')

    variant('dev', default=True)

    depends_on('visionary-dev-tools', when='+dev')

    depends_on('gettext')
    depends_on('zlib')

    # was bison 3.0.4 in the past
    depends_on('bison')
    depends_on('flex')
    depends_on('m4')
    depends_on('texinfo')
    depends_on('wget')

    conflicts('flex', when='@2.6.3', msg='Binutils 2.25 for Nux doesn\'t build with flex 2.6.3.')
