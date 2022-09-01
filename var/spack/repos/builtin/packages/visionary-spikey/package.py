# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.builtin.boost import Boost


class VisionarySpikey(Package):
    """Visionary Meta Package for the spikey platform."""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    variant('dev', default=True)

    depends_on('visionary-dev-tools', when='+dev')

    # build dependencies for the Spikey software stack
    # taken from: https://electronicvisions.github.io/hbp-sp9-guidebook/pm/spikey/appendix.html#setup-software;
    depends_on(Boost.with_default_variants)
    depends_on('boost+python cxxstd=17')
#    depends_on('libusb')  # needs to be an external requirement
    depends_on('llvm+clang')  # for clang-format
    depends_on('log4cxx')
    depends_on('qt@:4.8.999')
    depends_on('googletest')
    depends_on('gsl')
    depends_on('pkg-config')
    depends_on('py-lxml') # collab tests
    depends_on('py-nose')
    # runtime dependencies of experiments
    depends_on('python@:2.8')
    depends_on('py-numpy')
    depends_on('py-scipy')
    depends_on('py-matplotlib')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-spikey.py'))

        # we could create some filesystem view here?
