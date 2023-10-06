# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os.path as osp

class VisionaryAsic(Package):
    """Visionary ASIC-specific environment. For now this serves as a minimum
    software environment for our ASIC-related CI jobs (e.g. building bitfiles)
    in the ASIC container. It is not to be used with the visionary software
    stack (for now)."""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    depends_on('tcl-osys@890eafffbda95b58a472a2005c3cb9e90fd22ff6')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        filename = osp.basename(osp.dirname(__file__)) # gives name of parent folder
        install(__file__, join_path(prefix.etc, filename + '.py'))

        # we could create some filesystem view here?
