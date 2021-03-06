# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyBleach(PythonPackage):
    """An easy whitelist-based HTML-sanitizing tool."""

    homepage = "http://github.com/mozilla/bleach"
    pypi = "bleach/bleach-3.1.0.tar.gz"

    version('3.1.0', sha256='3fdf7f77adcf649c9911387df51254b813185e32b2c6619f690b593a617e19fa')
    version('1.5.0', sha256='978e758599b54cd3caa2e160d74102879b230ea8dc93871d0783721eef58bc65')

    depends_on('python@2.6:2.8,3.2:3.5', type=('build', 'run'), when='@:3.0.999')
    depends_on('python@2.6:2.8,3.4:', type=('build', 'run'), when='@3.1.0:')
    depends_on('py-setuptools', type='build')
    depends_on('py-six@1.9.0:', type=('build', 'run'))
    depends_on('py-webencodings', type=('build', 'run'))
    depends_on('py-html5lib@0.999,0.999999:0.9999999', type=('build', 'run'), when='@:2.999.999')
