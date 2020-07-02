# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class PySacred(PythonPackage):
    """
    Sacred is a tool to configure, organize, log and reproduce computational
    experiments.
    """

    homepage = "https://github.com/IDSIA/sacred"
    url      = "https://pypi.io/packages/source/s/sacred/sacred-0.8.1.tar.gz"

    version('0.8.1', sha256='a822f8011ffff729f51858990b14c3bab47d291db7a37150085fbbb56602bb93')

    # relative paths of dependencies break the file observer
    patch('file_observer_normpath.patch')
    # multiprocessing sometimes break fd output capturing
    # cf. https://github.com/IDSIA/sacred/pull/740
    patch("fix-tee_740.patch", when="@0.8.0:")

    depends_on('py-setuptools', type='build')
    depends_on("python@3.5.0:", type=('build', 'run'))
    depends_on('py-docopt@0.3:0.999', type=('build', 'run'))
    depends_on('py-jsonpickle@1.2:1.999', type=('build', 'run'))
    depends_on('py-munch@2.0.2:2.999', type=('build', 'run'))
    depends_on('py-wrapt@1.0:1.999', type=('build', 'run'))
    depends_on('py-py-cpuinfo@4.0:', type=('build', 'run'))
    depends_on('py-colorama@0.4:', type=('build', 'run'))
    depends_on('py-packaging@18.0:', type=('build', 'run'))
    depends_on('py-gitpython', type=('build', 'run'))
