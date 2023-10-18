# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHbpNeuromorphicPlatform(PythonPackage):
    """Python client for the Human Brain Project Neuromorphic Computing Platform.
    """
    homepage = "https://electronicvisions.github.io/hbp-sp9-guidebook/"
    git      = "https://github.com/HumanBrainProject/hbp-neuromorphic-client.git"

    version('0.11.1', tag='0.11.1')

    # dependencies based on ebrains/ebrains-23-09
    depends_on('python@3.7:')
    depends_on('py-setuptools',       type=('build'))
    depends_on('py-requests@2.20.0:', type=('build', 'run'))
    depends_on('py-click@8.0.3:',     type=('build', 'run'))
    depends_on('py-pyyaml@6.0:',      type=('build', 'run'))

    variant("provider", default=True,
            description="Include dependencies which are needed as a platform provider.")
    with when("+provider"):
        depends_on('py-sh', type=('build', 'run'))
        depends_on('py-radical-saga', type=('build', 'run'))
