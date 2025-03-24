# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on ebrains/a26393e1
class PyLibneuroml(PythonPackage):
    """A SciUnit library for data-driven validation testing of models of hippocampus
    """

    homepage = "https://github.com/NeuralEnsemble/libNeuroML"
    pypi     = "libNeuroML/libNeuroML-0.4.1.tar.gz"
    git      = "https://github.com/NeuralEnsemble/libNeuroML.git"

    version('0.5.5', sha256='b05830bb451ba797d941efee174724be9075d8d2e7d66f8379b2f2513c90d588')
    version('0.4.1', sha256='d1b81dbcf794097904438f04f201cb2cffed7c38117c19f65c595d63fcb8c8b3')

    depends_on('python@3.7:')
    depends_on('py-setuptools',    type=('build'))
    depends_on('py-lxml',          type=('run', 'test'))
    depends_on('py-six',           type=('run', 'test'))
    depends_on('py-networkx',      type=('run', 'test'))
    depends_on('py-numpy',         type=('run', 'test'))
    depends_on('py-tables@3.3.0:', type=('run', 'test'))
    depends_on('py-natsort',       type=('run', 'test'))
