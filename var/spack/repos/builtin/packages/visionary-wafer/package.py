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


class VisionaryWafer(Package):
    """Visionary Meta Package"""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    variant('dev', default=True)

    depends_on('visionary-dev-tools', when='+dev')

    conflicts('python@3:')

    variant('tensorflow', default=False)

    # to provide non-gccxml spack views we manually add the gccxml w/o dependencies later :)
    variant('gccxml', default=False)

    depends_on('catch2')
    depends_on('clara')
    depends_on('gccxml', when='+gccxml')
    depends_on('gsl')
    depends_on('intel-tbb')
    depends_on('liblockfile')
    # depends_on('npm')         FIXME: might be able to use the npm from node-js
    depends_on('node-js')     # FIXME: see above
    depends_on('pkg-config')
    depends_on('py-lxml') # collab tests
    depends_on('xerces-c')
    depends_on('boost@1.69.0: +graph+icu+mpi+python+numpy cxxstd=17')
    # we didn't introduce cuda support at all, upstream defaults to it
    # if we want cuda we need to decide on the cuda_arch, cf. py-torch
    # depends_on('py-tensorflow~cuda~tensorrt~nccl', when='+tensorflow')
    depends_on('log4cxx')
    depends_on('googletest@1.11.0:+gmock')
    depends_on('py-slurm-pipeline')
    depends_on('nest@2.20.1+python')
    #depends_on('py-brian')
    #depends_on('py-brian2')
    depends_on('py-bokeh')
    #depends_on('py-elephant')
    depends_on('py-notebook')
    depends_on('py-numba')
    depends_on('py-pynn @0.9.6')
    depends_on('py-matplotlib')
    depends_on('py-numpy')
    depends_on('py-pandas @0.19.0:')
    depends_on('py-tables @3.3.0:')
    depends_on('py-scipy')
    depends_on('py-scikit-image')
    depends_on('py-lmfit')
    depends_on('py-tabulate')
    depends_on('py-pybind11')
    depends_on('py-mock')
    depends_on('cereal')
    depends_on('py-yccp@:0.5.0', when="^python@:2.999.999")  #TODO remove constraints once concretizer fixed
    depends_on('py-yccp@1.0.0:', when="^python@3:")          #TODO remove constraints once concretizer fixed

    # hmf-fpga register file requires:
    depends_on('tcl-osys@890eafffbda95b58a472a2005c3cb9e90fd22ff6')
    # annotations for the concretiser, otherwise it is unable to detect the tk
    # restrictions correctly -> should be removable in the future
    depends_on('tk@8.5.19')
    depends_on('tcl@8.5.19')

    # lib-rcf depends on libuuid which is part of this
    depends_on('util-linux')

    ##################
    # Current fixups #
    ##################
    # intel-mkldnn depends on intel-mkl which also provides blas ->
    # concretization error -> reinvestigate when needed
    # Our GPUs support
    #   - cuda arch 6.1 (Geforce 1080)
    #   - cuda arch 8.6 (GeForce RTX 3080)
    # fix it up if you use other cards.
    depends_on('py-torch ~mkldnn +fbgemm +distributed +mpi +tensorpipe +nccl +gloo +cuda cuda_arch=61,86')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-wafer.py'))

        # we could create some filesystem view here?
