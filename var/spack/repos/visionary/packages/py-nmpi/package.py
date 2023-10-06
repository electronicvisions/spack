##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyNmpi(PythonPackage):
    """Python client for the Human Brain Project Neuromorphic Computing Platform"""

    homepage = "https://github.com/HumanBrainProject/hbp-neuromorphic-client"
    url      = "https://github.com/HumanBrainProject/hbp-neuromorphic-client/archive/0.4.2.tar.gz"

    version('2017-01-18',
	    git='https://github.com/HumanBrainProject/hbp-neuromorphic-client.git',
	    commit='09ba7e4b6ddfd57d6ad3959cca69b824a63a0320')

    version('0.4.2', '189b4fbe017d6500f3480d0031745976')
    version('0.4.1', '08645ff62d050e99f9bb57bb7d6b9138')
    version('0.4.0', '595b40a8d7f2ec7b68e0198cf764ea72')
    version('0.3.0', '1a2dc04ea0e00f2b56a862720705dd6c')
    version('0.2.0', '6864997bb0fea58dc3a41a466b32aaf4')

    depends_on('py-requests@2.3.0:',         type=('build', 'run'))
    depends_on('py-saga-python@0.15:',       type=('build', 'run'))
    depends_on('py-sh@1.09:',                type=('build', 'run'))
