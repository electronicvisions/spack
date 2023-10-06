# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyTreeMath(PythonPackage):
    """
    tree-math makes it easy to implement numerical algorithms that work on
    JAX pytrees, such as iterative methods for optimization and equation
    solving. It does so by providing a wrapper class tree_math.Vector that
    defines array operations such as infix arithmetic and dot-products on
    pytrees as if they were vectors.
    """

    homepage = "https://github.com/google/tree-math"
    pypi = "tree-math/tree-math-0.1.0.tar.gz"
    git = "https://github.com/google/tree-math.git"

    version('0.1.0.post', commit='0af9679125c13cc38dab5159bc8413ed79465344')
    version('0.1.0', sha256='77eb8d6ba4d6cfdd2d986a6bc3fc2d1b16212f0172863a3ca509720babf75929')

    depends_on('py-setuptools', type='build')
    depends_on('py-jax', type=('build', 'run'))
