# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyWfdbPython(PythonPackage):
    """
    The native Python waveform-database (WFDB) package. A library of tools for
    reading, writing, and processing WFDB signals and annotations."""

    homepage = "https://github.com/MIT-LCP/wfdb-python"
    url      = "https://github.com/MIT-LCP/wfdb-python/archive/2.2.0.tar.gz"

    version('2.2.0', sha256='d93fdad3950edfb6edd3724c5e5019ca351f81fa599f98f54a43051f41888cc8')

    depends_on('py-setuptools',        type='build')
    depends_on('py-numpy@1.11.0:',     type=('build', 'run'))
    depends_on('py-matplotlib@1.5.1:', type=('build', 'run'))
    depends_on('py-requests@2.10.0:',   type=('build', 'run'))
    depends_on('py-pandas@0.19.1:',    type=('build', 'run'))
    depends_on('py-scipy@0.19.0:',     type=('build', 'run'))
    depends_on('py-scikit-learn',      type=('build', 'run'))
