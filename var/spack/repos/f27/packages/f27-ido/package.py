# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class F27Ido(BundlePackage):
    """Software environment definition for Ido@F27"""

    version('1.0')  # Dummy

    depends_on('cmake')
    depends_on('hdf5')
    depends_on('fftw@3.3.9:+openmp')
    depends_on('libconfig@1.7.2:')
    depends_on('tclap@1.2.2:')
    depends_on('eigen@:3.3') # 3.4 breaks things?
    depends_on('cuda@11')
    depends_on('gsl')
    depends_on('boost')

    depends_on('python@3:')
    depends_on('py-numpy')
    depends_on('py-scipy')
    depends_on('py-h5py')
    depends_on('py-matplotlib')
    depends_on('py-cupy+cuda')
