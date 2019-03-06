##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
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

class PyAbslPy(PythonPackage):
    """
    This repository is a collection of Python library code for building Python applications. 
    The code is collected from Google's own Python code base, and has been extensively tested and used in production.
    """

    homepage = "https://pypi.org/project/absl-py/"
    url      = "https://cosmo-pypi.phys.ethz.ch/simple/absl-py/0.1.6/absl-py-0.1.6.tar.gz"

    version('0.1.6', 'b76269cbf04502b7d12efabcfa51a299')

    depends_on('py-six@1.10.0:', type='build')
    depends_on('py-enum34', type='build')
