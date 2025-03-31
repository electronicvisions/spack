# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on EBRAINS/25-02
class Genpybind(WafPackage):
    """Autogeneration of Python bindings from manually annotated C++ headers"""

    homepage = "https://github.com/kljohann/genpybind"
    url      = "https://github.com/kljohann/genpybind/archive/v0.1.0.tar.gz"
    git      = "https://github.com/kljohann/genpybind.git"

    version('0.2.1', sha256='e4d993f0c65cb5cf635cec7df899cbd91af1f0bd8a3626f33e9e0925f5383384')
    version('0.2.0', sha256='9d1e9d026a9e355e282aca549a2af108bedcc5bc59ba0b76a6072f88e4c0be4c')
    version('0.1.1-pre', commit="9d06a3ad4b6b917c8fcc07261a97b13a3079bcba")
    version('0.1.0', sha256='f25cb2b3180103cb96c42fb8d37be8b1f06b7721f6aa08841d5ae16361896407')
    version('master', branch='master')
    version('develop', branch='develop')

    version('visions', branch='master', git='https://github.com/electronicvisions/genpybind')
    # good for ebrains-10.0 too…
    version('ebrains-llvm15', tag='ebrains-9.0-a9', git='https://github.com/electronicvisions/genpybind')
    version('ebrains', tag='ebrains_release-1-rc1', git='https://github.com/electronicvisions/genpybind')

    # begin VISIONS (added)
    conflicts("llvm@:14", when="@ebrains-llvm15")
    conflicts("llvm@16:", when="@ebrains-llvm15")
    # end VISIONS

    depends_on(
            'llvm+clang+python+visionary@5.0.0:',
        type=('build', 'link'))
    depends_on('binutils', type='build')
    depends_on('python@2.7:', type=('build', 'run'))

    extends('python')

    patch('v0.2.1-python3.10.patch', when='@:0.2.1 ^python@3.10:')

    # llvm-config needs to be found at build time of packages using genpybind
    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path("PATH", self.spec["llvm"].prefix.bin)

    def configure_args(self):
        args = super(Genpybind, self).configure_args()

        if self.spec.satisfies("@visions") or self.spec.satisfies("@ebrains"):
            # currently only our HEAD supports the rename
            # TODO: adapt once the change is upstream
            args.append("--genpybind-disable-tests")
        else:
            args.append("--disable-tests")
        return args
