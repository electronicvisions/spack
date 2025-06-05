# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.boost import Boost


class VisionaryDlsCore(BundlePackage):
    """Core package that contains dependencies of the core DLS software
    ONLY!"""
    version('1.0')

    # Depend on visionary-nux to enable joint developement of host and PPU code with one meta package
    depends_on('visionary-nux ~dev')

    # depends_on('libusb-1.0')  external dependency
    depends_on('bear@3:')
    depends_on('bitsery')
    depends_on(Boost.with_default_variants)
    depends_on('boost@1.69.0: +graph+icu+mpi+python+numpy+coroutine+context+valgrind cxxstd=17')
    depends_on('cereal')
    depends_on('cppcheck')
    depends_on('doxygen+graphviz')
    depends_on('gecode')
    depends_on('genpybind')
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
    depends_on('py-jax@0.4.13') # later requires python@3.9; `^py-jaxlib +cuda cuda_arch=61,80,86` does not work for v0.21.0 -> specify in py-jax/package.py
    depends_on('py-junit-xml')  # needed for tests in libnux
    depends_on('py-matplotlib@3:')
    depends_on('py-networkx')
    depends_on('py-pytest')
    depends_on('py-nir')
    depends_on('py-numpy')
    depends_on('py-optax')
    depends_on('py-pybind11')
    depends_on('py-pycodestyle')
    depends_on('py-pylint')
    depends_on('py-pynn')
    depends_on('py-scipy')
    depends_on('py-tree-math')
    depends_on('python@3.10')
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
    depends_on('py-torch ~caffe2 ~xnnpack ~mkldnn ~cudnn ~magma ~qnnpack ~test ~gloo +cuda cuda_arch=61,80,86')

    # xilinx runtime dependencies
    depends_on('visionary-xilinx')

    # some versions of dependencies are broken
    conflicts("boost@1.86.0") # sha1 digest changed length, but boost::compute didn't adapt
    conflicts("py-pytest@8.2")
