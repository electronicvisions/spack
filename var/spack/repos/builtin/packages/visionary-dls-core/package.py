# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.builtin.boost import Boost


class VisionaryDlsCore(Package):
    """Core package that contains dependencies of the core DLS software
    ONLY!"""

    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack/archive/v0.8.tar.gz'

    # This is only a dummy tarball (see difference between version numbers)
    # TODO: as soon as a MetaPackage-concept has been merged, please update this package
    version('1.0', '372ce038842f20bf0ae02de50c26e85d', url='https://github.com/electronicvisions/spack/archive/v0.8.tar.gz')

    # Depend on visionary-nux to enable joint developement of host and PPU code with one meta package
    depends_on('visionary-nux ~dev')

    # depends_on('libusb-1.0')  external dependency
    depends_on('bear')
    depends_on('bitsery')
    depends_on(Boost.with_default_variants)
    depends_on('boost@1.69.0: +graph+icu+mpi+python+numpy+coroutine+context+valgrind cxxstd=17')
    depends_on('cereal')
    depends_on('cppcheck')
    depends_on('doxygen+graphviz')
    depends_on('genpybind')
    depends_on('gflags')
    depends_on('googletest@1.11.0:+gmock')
    # depends_on('icarus')
    depends_on('inja')  # template engine for PPU source jit generation
    depends_on('intel-tbb')  # ppu gdbserver
    depends_on('libelf')
    depends_on('liblockfile')
    depends_on('llvm')
    depends_on('log4cxx')
    depends_on('munge')
    depends_on('pkg-config')
    depends_on('py-jax@0.3.25: +cuda cuda_arch=61,80,86')
    depends_on('py-matplotlib@3:')
    depends_on('py-networkx')
    depends_on('py-nose')
    depends_on('py-numpy')
    depends_on('py-pybind11')
    depends_on('py-pybind11-stubgen')
    depends_on('py-pycodestyle')
    depends_on('py-pyelftools')
    depends_on('py-pylint')
    depends_on('py-pynn')
    depends_on('py-python-usbtmc')
    depends_on('py-scipy')
    depends_on('py-sqlalchemy')
    depends_on('py-tree-math')
    depends_on('util-linux') # from lib-rcf
    depends_on('yaml-cpp+shared')

    ##################
    # Current fixups #
    ##################
    # Our GPUs support
    #   - cuda arch 6.1 (NVIDIA Geforce 1080)
    #   - cuda arch 8.0 (NVIDIA A100)
    #   - cuda arch 8.6 (NVIDIA GeForce RTX 3080)
    # We want to set defaults in packages.yaml, but it's ignored?
    depends_on('py-torch@1.11.0 ~caffe2 ~xnnpack ~mkldnn ~cudnn ~magma ~nnpack ~qnnpack ~test +cuda cuda_arch=61,80,86')

    # we only support Python 3.7+!
    depends_on('python@3.7.0:')

    # xilinx runtime dependencies
    depends_on('visionary-xilinx')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, spec.name + '.py'))

        # we could create some filesystem view here?
