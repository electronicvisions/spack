# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on EBRAINS/25.02
class PyHbpNeuromorphicPlatform(PythonPackage):
    """Python client for the Human Brain Project Neuromorphic Computing Platform.
    """

    homepage = "https://electronicvisions.github.io/hbp-sp9-guidebook/"
    pypi     = "hbp_neuromorphic_platform/hbp_neuromorphic_platform-0.10.1.tar.gz"
    git      = "https://github.com/HumanBrainProject/hbp-neuromorphic-client.git"

    maintainers = ['apdavison']

    version('0.11.2', sha256='ac74412dd838e977e204c1cb812ed3520d1db89e3b3758cc7eb630d72b593f22')
    # begin VISIONS (added version) in-repo version includes nmpi_saga.py (missing in pypi!)
    version('0.11.1', tag='0.11.1')
    # end VISIONS
    version('0.11.0', sha256='14295b3132c603f16b88af336372f36a9458d71918325b46178f2b7f2d752b9e')
    version('0.10.2', sha256='3e29175636385f2f561b8095e6225edc41be7f05c6a21232872ef662e6b7ce56')
    version('0.10.1', sha256='76b3acdbc63c901d158bad6d74e26f8a4ad7b10a261c1d51f1e9bf482766bae7')

    depends_on('python@3.7:')
    depends_on('py-setuptools',       type=('build'))
    depends_on('py-requests@2.20.0:', type=('run', 'test'))
    depends_on('py-click@8.0.3:',     type=('run', 'test'))
    depends_on('py-pyyaml@6.0:',      type=('run', 'test'))
    depends_on('py-ebrains-drive@0.5.1:', type=('run', 'test'))

    # begin VISIONS (added)
    # `when` enforce the repo version
    variant("provider", default=True, when="@0.11.1",
            description="Include dependencies which are needed as a platform provider.")
    with when("+provider"):
        depends_on('py-sh', type=('build', 'run'))
        depends_on('py-radical-saga', type=('build', 'run'))
    # end VISIONS
