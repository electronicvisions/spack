# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyJupyterClient(PythonPackage):
    """Jupyter protocol client APIs"""

    homepage = "https://github.com/jupyter/jupyter_client"
    pypi = "jupyter-client/jupyter_client-6.1.7.tar.gz"

    version('7.1.2', sha256='4ea61033726c8e579edb55626d8ee2e6bf0a83158ddf3751b8dd46b2c5cd1e96')
    version('7.0.6', sha256='8b6e06000eb9399775e0a55c52df6c1be4766666209c22f90c2691ded0e338dc')
    version('6.1.12', sha256='c4bca1d0846186ca8be97f4d2fa6d2bae889cce4892a167ffa1ba6bd1f73e782')
    version('6.1.7', sha256='49e390b36fe4b4226724704ea28d9fb903f1a3601b6882ce3105221cd09377a1')
    version('5.3.4', sha256='2af6f0e0e4d88009b11103490bea0bfb405c1c470e226c2b7b17c10e5dda9734')
    version('5.3.3', sha256='9d76231da1b4969afc762896fa79f0135f9f650cab2c1fc6526941d20d9aa8c9')
    version('5.3.2', sha256='2ff67cf04f58a3aeefa9ea201f36feb5f5b46efb0641b472f86d28021c2bf223')
    version('5.3.1', sha256='aced0743cbb0c1449be7ef94bba89dc9661e050008cf15f906ae802c9c262cf8')
    version('5.3.0', sha256='004c83e7ad96d8fab1260cbdfcf0ccbcd9cd34b6769f5a6fb2134464fba409c6')
    version('5.2.4', sha256='61ee1e02fd78b025f9720963e1fe96d8d29f44bc250ca7e7a46bc35a174eb7d6')
    version('5.2.3', sha256='40d4dd389f34748a5fe8814240afdb24fe5672d54a794285a24288a8cfef4a10')
    version('5.2.2', sha256='030a65d9e781313ee0e5244543a336bbfd50a6ba1f773924d9946a2918406388')
    version('5.2.1', sha256='0af80c616a7e4d508c28ed0358d9e55b6eb731ee6e0afceced9978aebb546dc7')
    version('5.2.0', sha256='0e3c619f41dceab81cdfe1e67abc2440b0bc54cac1d4e437cbdd0fe42f801cfa')
    version('4.4.0', sha256='2fda7fe1af35f0b4a77c4a2fd4ee38ac3666ed7f4d92a5b6ff8aaf764c38e199')
    version('4.3.0', sha256='90b6ea3ced910ed94c5d558373490a81b33c672d877c1ffdc76b281e3216f1f6')
    version('4.2.2', sha256='bf3e8ea4c44f07dbe2991e41031f6dab242734be424f4d40b72cc58a12c7d2ca')
    version('4.2.1', sha256='547d443fb38ea667b468a6625ac374d476f8ac90fe17c3e35d75cab3cb8d40ba')
    version('4.2.0', sha256='00eab54615fb10f1e508d8e7a952fbeeb2a82cd67b17582bd61be51a08a61d89')
    version('4.1.1', sha256='ca6f3f66d5dc1e9bca81696ae607a93d652210c3ee9385a7c31c067d5ba88e6e')
    version('4.1.0', sha256='ecf76a159381ec9880fd2c31388c6983b1d855f92f0292cf0667a90dd63f51c0')
    version('4.0.0', sha256='33b15abb1307d8d3716b0d3b5d07aa22fdfbbf65a9f1aedf478a274a6adc11c0')

    depends_on('python@2.7:2.8,3.3:', type=('build', 'run'))
    depends_on('python@2.7:2.8,3.5:', type=('build', 'run'), when='@5:')
    depends_on('python@3.5:', type=('build', 'run'), when='@6:')
    depends_on('python@3.6.1:', type=('build', 'run'), when='@6.2:')
    depends_on('py-setuptools', type=('build', 'run'), when='@5:')

    depends_on('py-entrypoints', type=('build', 'run'), when='@7:')
    depends_on('py-jupyter-core', type=('build', 'run'))
    depends_on('py-jupyter-core@4.6.0:', type=('build', 'run'), when='@6:')
    depends_on('py-nest-asyncio@1.5:', type=('build', 'run'), when='@6.1.13:')
    depends_on('py-python-dateutil@2.1:', type=('build', 'run'), when='@5:')
    depends_on('py-pyzmq@13:', type=('build', 'run'))
    depends_on('py-tornado@4.1:', type=('build', 'run'), when='@5:')
    depends_on('py-traitlets', type=('build', 'run'))
