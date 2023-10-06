##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *



class VisionarySimulation(Package):
    """Visionary Meta Package"""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    variant('dev', default=True)

    depends_on('visionary-dev-tools', when='+dev')

    depends_on('llvm+clang')  # for clang-format
    depends_on('nest+backports')
    depends_on('py-cython')  # add runtime dependency so cython is available in visionary-simulation app (needed for sbs)
    #depends_on('py-elephant')
    depends_on('py-h5py')
    depends_on('py-ipython')
    depends_on('py-pandas')
    depends_on('py-pyyaml')
    depends_on('py-sbs')
    depends_on('py-scikit-learn')
    # depends_on('visionary-nest')
    depends_on('py-yccp@:0.5.0', when="^python@:2.999.999")  #TODO remove constraints once concretizer fixed
    depends_on('py-yccp@1.0.0:', when="^python@3:")          #TODO remove constraints once concretizer fixed
    # TODO Re-enable once https://github.com/spack/spack/pull/13112 is merged
    #  depends_on('tensorflow')
    #  depends_on('tensorflow-estimator', when='^tensorflow@1.13:')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-simulation.py'))

        # we could create some filesystem view here?
