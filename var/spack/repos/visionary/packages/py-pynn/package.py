# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on ebrains/a26393e1
class PyPynn(PythonPackage):
    """A Python package for simulator-independent specification of neuronal
        network models
    """

    homepage = "http://neuralensemble.org/PyNN/"
    pypi = "PyNN/PyNN-0.10.0.tar.gz"
    git = "https://github.com/NeuralEnsemble/PyNN.git"

    maintainers = ["apdavison"]

    version('0.12.3', sha256='e196f9055c46fe5c0e23f491815d16dca8db9be599a226ee11fa67605cab153d')
    version('0.12.2', sha256='8039b68e3e5f98b537038c249dc42c027bd63f9ecc015c82f1f88bd30dfa28a9')
    version('0.12.1', sha256='fef49cc601032565341f02c5c982cb805bc0cc16de75166acb1b7f8c179adfda')
    version('0.11.0', sha256='eab6ef281e0a00180c8b31ffb65984f54216c68464db363a5c09832fec91f952')
    version('0.10.1', sha256='03fbafeddd64ae7163e2b557b2760380b6eceb52469f1b3f4cc203bbb80f0cde')
    version('0.10.0', sha256='04120fe0e03260d664b337e0ac29d985c3fb3684ef35b1add93a66739891c98f')
    version('0.9.6', sha256='d85226800e30bc1692d3f84485c3fa20b921c2ab55f1201d0a3bf23432e16cd2')
    version('0.9.5', sha256='91af2126b639a6a795bfc2709ac49423278c4794b6d0da143908b9afcb415f80')

    variant('mpi', default=False, description='Enable MPI support')
    depends_on('python@2.7:2.8,3.3:', when="@0.9.5")
    depends_on('python@2.7:2.8,3.6:', when="@0.9.6")
    depends_on('python@3.7:',         when="@0.10.0:0.10.1")
    depends_on('python@3.8:',         when="@0.11.0:")

    depends_on('py-setuptools',         type=('build'))
    depends_on('py-setuptools@61:',     type=('build'), when="@0.11:")

    depends_on('py-jinja2@2.7:',        type=('run', 'test'))
    depends_on('py-docutils@0.10:',     type=('run', 'test'))

    depends_on('py-numpy@1.8.2:',       type=('run', 'test'), when="@0.9.5")
    depends_on('py-numpy@1.13.0:',      type=('run', 'test'), when="@0.9.6")
    depends_on('py-numpy@1.16.1:',      type=('run', 'test'), when="@0.10.0")
    depends_on('py-numpy@1.18.5:',      type=('run', 'test'), when="@0.10.1:")
    depends_on('py-numpy@:1.23',        type=('run', 'test'), when="@:0.10")  # removal of numpy.int/float/...

    depends_on('py-mpi4py',             type=('run', 'test'), when='+mpi')
    depends_on('py-quantities@0.12.1:', type=('run', 'test'), when="@0.9.5:")

    depends_on('py-lazyarray@0.3.2:',   type=('run', 'test'), when="@0.9.5")
    depends_on('py-lazyarray@0.3.4:',   type=('run', 'test'), when="@0.9.6")
    depends_on('py-lazyarray@0.5.0:',   type=('run', 'test'), when="@0.10.0")
    depends_on('py-lazyarray@0.5.2:',   type=('run', 'test'), when="@0.10.1:")

    depends_on('py-neo@0.5.2:',         type=('run', 'test'), when="@0.9.5")
    depends_on('py-neo@0.8.0',          type=('run', 'test'), when="@0.9.6")
    depends_on('py-neo@0.10.0:',        type=('run', 'test'), when="@0.10.0")
    depends_on('py-neo@0.11.0:',        type=('run', 'test'), when="@0.10.1:")

    depends_on('py-libneuroml@0.4.1:',  type=('run', 'test'), when="@0.12.1:")
    depends_on('py-morphio',            type=('run', 'test'), when="@0.12:")

    depends_on('neuron@8.1:+python',    type=('run', 'test'), when="@0.10.1:")
    depends_on('nest@3.3:3.4+python',   type=('run', 'test'), when="@0.10.1:0.11.0")
    depends_on('nest@3.4:+python',      type=('run', 'test'), when="@0.12.1:")
    depends_on('py-brian2',             type=('run', 'test'))
    depends_on('arbor@0.8.1:+python',   type=('run', 'test'), when="@0.12.1:0.12.2")
    depends_on('arbor@0.9.0:+python',   type=('run', 'test'), when="@0.12.3:")


    depends_on('py-mock@1.0:',          type='test')
    depends_on('py-matplotlib',         type='test')
    depends_on("py-pytest",             type='test', when="@0.11.0:")

    patch('pynn-0.9.6-python3.patch', when='@0.9.6 ^python@3:')
    patch('pynn-0.12.2-arbor-0.9.0.patch', when='@0.12.1:0.12.2')

    # neuroml and nineml are optional dependencies. Leave out of import_modules to avoid errors in tests
    skip_modules = ['pyNN.neuroml', 'pyNN.nineml', 'pyNN.hardware']

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def install_test(self):
        # run tests here:
        pytest = which('pytest')
        pytest()
