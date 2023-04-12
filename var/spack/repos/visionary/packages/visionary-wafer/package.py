# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.boost import Boost


class VisionaryWafer(BundlePackage):
    """Visionary Meta Package"""

    version('1.0')

    variant('dev', default=True)

    depends_on('visionary-dev-tools', when='+dev')

    # conflicts('python@3:')
    # depends_on('python@:2.7.99')
    depends_on('python@3:')

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
    depends_on(Boost.with_default_variants)
    depends_on('boost@1.69.0: +graph+icu+mpi+python+numpy cxxstd=17')
    depends_on('log4cxx')
    depends_on('googletest@1.11.0:+gmock')
    depends_on('py-slurm-pipeline')
    depends_on('nest@2.20.1+python')
    #depends_on('py-brian')
    #depends_on('py-brian2')
    depends_on('py-bokeh')
    depends_on('py-elephant')
    depends_on('py-notebook')
    depends_on('py-numba')
    depends_on('py-pynn @0.9.6')
    depends_on('py-matplotlib@3:')
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
    depends_on('tcl-osys@1.1.1-post1')
    # annotations for the concretiser, otherwise it is unable to detect the tk
    # restrictions correctly -> should be removable in the future
    depends_on('tk@8.5.19')
    depends_on('tcl@8.5.19')

    # lib-rcf depends on libuuid which is part of this
    depends_on('util-linux')

    ##################
    # Current fixups #
    ##################
    # Our GPUs support
    #   - cuda arch 6.1 (NVIDIA Geforce 1080)
    #   - cuda arch 8.0 (NVIDIA A100)
    #   - cuda arch 8.6 (NVIDIA GeForce RTX 3080)
    # We want to set defaults in packages.yaml, but it's ignored?
    depends_on('py-torch@1.11.0 ~caffe2 ~xnnpack ~mkldnn ~cudnn ~magma ~qnnpack ~test +cuda cuda_arch=61,80,86')
    depends_on('py-torchvision')
