# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import re


# VISIONS: based on ebrains/a26393e12b6cf8949fb5cdb8e4e8690cdd58c001
class Nest(CMakePackage):
    """NEST is a simulator for spiking neural network models

    It focuses on the dynamics, size and structure of neural systems rather
    than on the exact morphology of individual neurons."""

    homepage = "http://www.nest-simulator.org"
    urls     = [
        #
        # note: for early nest releases the refs/tags/xxx.tar.gz is different
        # from download/v2.x.y/...tar.gz! The download one already had the
        # `make dist` boot-strapping done.
        #
        #'https://github.com/nest/nest-simulator/releases/download/v2.12.0/nest-2.12.0.tar.gz',
        'https://github.com/nest/nest-simulator/archive/refs/tags/v2.12.0.tar.gz',
        'https://github.com/nest/nest-simulator/archive/refs/tags/v3.0.tar.gz'
    ]
    git      = "https://github.com/nest/nest-simulator.git"

    maintainers = ['terhorst']

    version('master', branch='master')
    version('3.8',    sha256='eb255f8828be001abea0cddad2f14d78b70857fc82bece724551f27c698318c8')
    version('3.7',    sha256='b313e03aa05a0d8053b895a1d14ea42e75805393c6daa0cbc62f9398d0dacd8b')
    version('3.6',    sha256='68d6b11791e1284dc94fef35d84c08dd7a11322c0f1e1fc9b39c5e6882284922')
    patch('nest-simulator-3.6-p1-CxxRealPath.patch', when='@3.2:')
    version('3.5',    sha256='3cdf5720854a4d8a7d359f9de9d2fb3619a0be2e36932028d6940360741547bd')
    version('3.4',    sha256='c56699111f899045ba48e55e87d14eca8763b48ebbb3648beee701a36aa3af20')
    version('3.3',    sha256='179462b966cc61f5785d2fee770bc36f86745598ace9cd97dd620622b62043ed')
    version('3.2',    sha256='583d5725882ad5e8fd4fc7ffab425da97cbbb91fadbc327e940c184e8892b958')
    patch('nest-simulator-3.2-p1-VersionNumber.patch', when='@3.2')
    version('3.1',    sha256='5c11dd6b451c4c6bf93037bf29d5231c6c75a0e1a8863344f6fb9bb225f279ca')
    version('3.0',    sha256='d481ea67f3251fe3aadf5252ab0a999172f0cd5536c5985366d271d772e686e6')
    patch('2021-07-17_fix-pyexecdir.patch', when='@3.0')
    version('2.20.2', sha256='7c36daf673b379b8ef82d2293a4cdf2f4dbb5d25bf570cf52f41f6293c89a28d')
    version('2.20.1', sha256='df3d32b5899d5d444f708037b290f889ac6ff8eae6b7be9e9faee2c0d660d8e5')
    version('2.20.0', sha256='40e33187c22d6e843d80095b221fa7fd5ebe4dbc0116765a91fc5c425dd0eca4', deprecated=True)
    version('2.18.0', sha256='7295c936fbdd5486395b06f54f0d4d35d9a1b6ee50b7b844186ec2c92de641d1', deprecated=True)
    version('2.16.0', sha256='abfeb61719dec54da9477be035bef1d9d764f4e7663f63f6a6d9211f967e0490', deprecated=True)
    version('2.14.2', sha256='c80050ea94751a7f63bb255bdc518e03a033c4352903d2e06456157314cd42c3')
    version('2.14.1', sha256='23aeadd0b8eda83a31797751f96855b0208979d70472e0f6752a7ce7ea80ad7a')
    version('2.14.0', sha256='d6316d6c9153100a3220488abfa738958c4b65bf2622bd15540e4aa81e79f17f')
    version('2.12.0', sha256='bac578f38bb0621618ee9d5f2f1febfee60cddc000ff32e51a5f5470bb3df40d')
    version('2.10.0', sha256='2b6fc562cd6362e812d94bb742562a5a685fb1c7e08403765dbe123d59b0996c')
    version('2.8.0',  sha256='d47325b27a5599b6ea58a3c4ef06656e7c5a4941c4e94dec6a5c2fa956209915')
    version('2.6.0',  sha256='5fe4924bc57d0c7dd820aa371de935eedf7e813832c0eee2c976b33c9a8db4cf')
    version('2.4.2',  sha256='8f86e58c1a12b733ffabd8b0400326e5a3494a458149ea8ebe9f19674d05b91b')

    variant('python', default=True,
            description='Build the PyNEST interface')
    variant('mpi', default=True,
            description='Build with MPI bindings')
    variant('openmp', default=True,
            description='"Enable OpenMP support"')
    variant('optimize', default=True,
            description='Build with MPI bindings')
    variant('modules', default=False,
            description='Enables external module support')
    variant('gsl',     default=True,
            description="Enable GNU Scientific Library")
    variant('shared',   default=True,
            description="Build shared libraries")
    variant('testsuite', default=False,
            description="Run extended testsuite with full number of unit- and integration tests")
    variant('sonata',    default=False,
            description="Enable direct reading of connectivity from SONATA files")
    variant('boost',    default=True,
            description="Enable optimizations provided via Boost library algorithms and containers")
    # TODO add variants for neurosim and music when these are in spack

    conflicts('~gsl', when='@:2.10.99',
              msg='Option only introduced for non-ancient versions.')
    conflicts('~shared', when='@:2.10.99',
              msg='Option only introduced for non-ancient versions.')
    conflicts('~openmp', when='@:2.10.99',
              msg='Option only introduced for non-ancient versions.')

    depends_on('python@2.6:2.99',   when='@:2.15.99+python', type=('build', 'run'))
    depends_on('python@2.6:',       when='@2.16:+python', type=('build', 'run'))
    depends_on('python@3.8:',       when='@3:', type=('build', 'run'))
    depends_on('py-numpy@:1.16.99', when='@:2.14.99+python', type=('build', 'run'))
    depends_on('py-numpy@:1.23.99', when='@:3.3', type=('build', 'run', 'test'))
    depends_on('py-numpy',          when='+python', type=('build', 'run', 'test'))
    depends_on('py-pandas',         when='@3:', type=('test'))
    depends_on('py-cython@0.19.2:', when='+python', type='build')
    depends_on('py-setuptools',     when='+python', type='build')
    depends_on('boost',             when="@2.16:+boost", type='build')
    depends_on('py-setuptools@:44.99.99',     when='@:2.15.99+python', type='build')
    depends_on('py-h5py',           when='@3.4.99:+sonata', type=('test', 'build', 'run'))
    depends_on('hdf5+cxx+mpi',      when='@3.4.99:+sonata+mpi', type=('build', 'run'))
    depends_on('hdf5+cxx~mpi',      when='@3.4.99:+sonata~mpi', type=('build', 'run'))
    depends_on('py-pandas',         when='@3.4.99:+sonata', type=('build', 'run'))

    depends_on('py-nose',           when='@:2.99.99+python+testsuite', type='test')
    depends_on('py-pytest',         when='@3.0:+testsuite', type='test')
    depends_on('py-pytest-xdist',   when='@3.0:+testsuite', type='test')
    depends_on('py-pytest-timeout', when='@3.0:+testsuite', type='test')
    depends_on('py-junitparser@2:', when='+testsuite', type='test')
    depends_on('py-terminaltables', when='@3:+testsuite', type='test')
    depends_on('py-pycodestyle',    when='@3:+testsuite', type='test')
    depends_on('cppcheck',          when='+testsuite', type='test')

    # for `clang-format`
    depends_on('py-clang-format@3.6',  when='@:3.1.99+testsuite', type='test')
    depends_on('py-clang-format@9',    when='@3.2:3.3.99+testsuite', type='test')
    depends_on('py-clang-format@13',   when='@3.4:+testsuite', type='test')

    depends_on('mpi',               when='+mpi')
    depends_on('py-mpi4py',         when='+python+mpi', type=('run', 'test'))
    # depends_on('doxygen',           type='build')
    depends_on('gsl',               when='+gsl')
    depends_on('readline',          type=('build', 'run', 'test'))
    depends_on('ncurses',          type=('build', 'run', 'test'))
    depends_on('libtool',          type=('build', 'run', 'test'))
    depends_on('pkgconfig',         type='build')

    extends('python', when='+python')

    # Before 2.12.0 it was an autotools package
    @when('@:2.10.99')
    def cmake(self, spec, prefix):
        pass

    @when('@:2.10.99')
    def build(self, spec, prefix):
        pass

    @when('@:2.10.99')
    def install(self, spec, prefix):
        # calculate the "./configure" flags (not cmake!)
        configure_args = ["CXXFLAGS=-std=c++03",
                          "--prefix=" + prefix,
                          "--with-openmp"]
        if '+python' in spec:
            configure_args.append("--with-python")
        else:
            configure_args.append("--without-python")
        if '+mpi' in spec:
            configure_args.append("--with-mpi")
        else:
            configure_args.append("--without-mpi")
        if '+optimize' in spec:
            configure_args.append("--with-optimize")
        else:
            configure_args.append("--without-optimize")

        if '+mpi' in spec:
            env['CC'] = spec['mpi'].mpicc
            env['CXX'] = spec['mpi'].mpicxx
            env['F77'] = spec['mpi'].mpif77
            env['FC'] = spec['mpi'].mpifc

        configure(*configure_args)
        make()
        make("install")

    def cmake_args(self):
        args = [
            "-DCMAKE_INSTALL_LIBDIR=lib",
            "-DSPACK_CXX_COMPILER=" + self.compiler.cxx
            ]

        for flag in "boost mpi openmp optimize".split():
            if '+' + flag in self.spec:
                args.append('-Dwith-'+flag+'=ON')
            else:
                args.append('-Dwith-'+flag+'=OFF')

        if '+gsl' in self.spec:
            args.append('-Dwith-gsl=' + self.spec['gsl'].prefix)
        else:
            args.append('-Dwith-gsl=OFF')

        if self.spec.satisfies('@:2.999'):
            if '+python':
                version = self.spec['python'].version[0]
                args.append('-Dwith-python={0}'.format(version))
                args.append('-Dcythonize-pynest=' + self.spec['py-cython'].prefix)
            else:
                args.append('-Dwith-python=OFF')
                args.append('-Dcythonize-pynest=OFF')

        if '+sonata' in self.spec:
            args.append('-Dwith-hdf5=ON')
        else:
            args.append('-Dwith-hdf5=OFF')

        if '+shared' in self.spec:
            args.append('-Dstatic-libraries=OFF')
        else:
            args.append('-Dstatic-libraries=ON')

        return args

    @when('@:2.14.0+modules')
    @run_after('install')
    def install_headers(self):
        # copy source files to installation folder for older versions
        # (these are needed for modules to build against)
        # see https://github.com/nest/nest-simulator/pull/844
        path_headers = join_path(prefix, "include", "nest")

        mkdirp(path_headers)

        for suffix in ["h", "hpp"]:
            for f in find_headers('*.{0}'.format(suffix),
                                  self.stage.source_path, recursive=True):
                install(f, path_headers)

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def installcheck(self):
        if self.spec.variants['testsuite'].value:
            print('''
            ##########################################
            ###
            ### RUNNING MAKE INSTALLCHECK
            ###
            ##########################################
    ''')
            with working_dir(self.build_directory):
                make("installcheck")

    def setup_run_environment(self, env):
        pass

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def install_test(self):
        # test inspired by py-numpy spack package
        with working_dir('spack-test', create=True):
            python('-c', 'from pprint import pprint; import nest; pprint(nest.get())')
        # test to check the output of "nest-config --compiler"
        nest_config = Executable(self.prefix.bin + '/nest-config')
        out = nest_config('--compiler', output=str.split, error=str.split)
        check_outputs(re.escape(self.compiler.cxx), out)

    @when('@2.11.0:')
    @run_after('build')
    @on_package_attributes(run_tests=True)
    def check(self):
        # 'make test' currently does not run any useful tests, as the focus is on 'make installcheck'.
        # So we override this to no-op and use a post-install method instead (see above).
        pass
