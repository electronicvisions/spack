# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys


class PyElephant(PythonPackage):
    """Elephant is a package for analysis of electrophysiology data in Python
    """

    homepage = "https://neuralensemble.org/elephant"
    pypi = "elephant/elephant-0.3.0.tar.gz"

    version('0.5.0', sha256='eeedc58f49200b158a9be329015c8dd562450b3c2aa01fdcd92375aca80e461c')
    version('0.4.1', sha256='86b21a44cbacdc09a6ba6f51738dcd5b42ecd553d73acb29f71a0be7c82eac81')
    version('0.3.0', sha256='747251ccfb5820bdead6391411b5faf205b4ddf3ababaefe865f50b16540cfef')

    variant('doc', default=False, description='Build the documentation')
    variant('pandas', default=True, description='Build with pandas')
    variant('scikit', default=True, description='Build with scikit-learn')
    variant('spade', default=False, description='Build with prebuild spade')

    patch('deletefetches.patch')

    resource(name='fim364.so',
             url='http://www.borgelt.net/bin64/py3/fim.so',
             destination='.',
             placement='elephant/spade_src/fim364.so',
             sha256='4e4751f511d32c37f0feefec5ee3c566e8e31c3cc345e4add0d9fe3fd8747300',
             when='^python@3:',
             expand=False)

    resource(name='fim264.so',
             url='http://www.borgelt.net/bin64/py2/fim.so',
             placement='elephant/spade_src/fim264.so',
             destination='.',
             sha256='6d0ebafb55e5156e9cf087f77b88d36326917776e1fe53b478967ab353e3f91f',
             when='^python@:2.8',
             expand=False)

    resource(name='fim332.so',
             url='http://www.borgelt.net/bin32/py3/fim.so',
             placement='elephant/spade_src/fim332.so',
             destination='.',
             sha256='6d0ebafb55e5156e9cf087f77b88d36326917776e1fe53b478967ab353e3f91f',
             when='^python@3:',
             expand=False)

    resource(name='fim232.so',
             url='http://www.borgelt.net/bin32/py2/fim.so',
             placement='elephant/spade_src/fim232.so',
             destination='.',
             sha256='db2cd8470c92ea541fb9f107421c6b7b0a6ce9ceab5772e87e410e6ac6982dac',
             when='^python@:2.8',
             expand=False)

    depends_on('py-setuptools',         type='build')
    depends_on('py-neo@0.3.4:',         type=('build', 'run'))  # > 0.3.3 ?
    depends_on('py-numpy@1.8.2:',       type=('build', 'run'))
    depends_on('py-quantities@0.10.1:', type=('build', 'run'))
    depends_on('py-scipy@0.14.0:',      type=('build', 'run'))
    depends_on('py-six@1.10.0:',        type=('build', 'run'))
    depends_on('py-pandas@0.14.1:',     type=('build', 'run'), when='+pandas')
    depends_on('py-numpydoc@0.5:',      type=('build', 'run'), when='+doc')
    depends_on('py-sphinx@1.2.2:',      type=('build', 'run'), when='+doc')
