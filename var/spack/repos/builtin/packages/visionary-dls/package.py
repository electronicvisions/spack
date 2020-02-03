# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class VisionaryDls(Package):
    """Visionary Meta Package - software needed for various experiments running
    on DLS (be it spiking or hagen mode)
    """
    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    variant("dev", default=True, description="With visionary-dev-tools")

    depends_on("visionary-dls-core")

    depends_on("visionary-dev-tools", when="+dev")

    depends_on('py-flask')
    depends_on('py-h5py')
    depends_on('py-lxml')  # collab tests
    depends_on('py-notebook')
    depends_on('py-pandas')
    depends_on('py-python-socketio')
    depends_on('py-scikit-learn')
    depends_on('py-seaborn')
    depends_on('py-sqlalchemy')
    depends_on('py-torchvision')
    depends_on('py-yccp@1.0.0:')
    depends_on('xerces-c')


    ##################
    # Current fixups #
    ##################
    # intel-mkldnn depends on intel-mkl which also provides blas ->
    # concretization error -> reinvestigate when needed
    depends_on('py-torch ~mkldnn')

    # TODO Re-enable once https://github.com/spack/spack/pull/13112 is merged
    #  depends_on('tensorflow')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, spec.name + '.py'))

        # we could create some filesystem view here?
