# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyTypedAst(PythonPackage):
    """A fork of Python 2 and 3 ast modules with type comment support."""

    homepage = "https://github.com/python/typed_ast"
    pypi = "typed-ast/typed_ast-1.4.0.tar.gz"

    version('1.4.0', sha256='66480f95b8167c9c5c5c87f32cf437d585937970f3fc24386f313a4c97b44e34')
    version('1.3.5', sha256='5315f4509c1476718a4825f45a203b82d7fdf2a6f5f0c8f166435975b1c9f7d4',
            url="https://files.pythonhosted.org/packages/d3/b1/959c3ed4a9cc100feba7ad1a7d6336d8888937ee89f4a577f7698e09decd/typed-ast-1.3.5.tar.gz")
    version('1.2.0', sha256='b4726339a4c180a8b6ad9d8b50d2b6dc247e1b79b38fe2290549c98e82e4fd15',
            url="https://files.pythonhosted.org/packages/00/be/c3769a5d6a179c42eba04186dc7efeb165edf92f7b1582ccfe81cb17d7f9/typed-ast-1.2.0.tar.gz")
    version('1.1.2', sha256='4304399ff89452871348f6fb7a7112454cd508fbe3eb49b5ed711cce9b99fe9e',
            url="https://files.pythonhosted.org/packages/68/72/96ba023d854ce8b3bf11cf261e4b2774787768834c9e30b77a94d02c98ad/typed-ast-1.1.2.tar.gz")

    depends_on('python@3.3:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
