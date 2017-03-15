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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install nix
#
# You can edit this file again by typing:
#
#     spack edit nix
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Nix(CMakePackage):
    """Neuroscience information exchange format."""

    homepage = "https://github.com/G-Node/nix"
    url      = "https://github.com/G-Node/nix/archive/1.3.2.tar.gz"

    version('2017-03-01', git="https://github.com/electronicvisions/nix",
            commit="2083023c868f6db65fabac825636a78495881a4a")
    version('2017-02-17', git="https://github.com/electronicvisions/nix",
            commit="f7b639bf2e3d2e3724eec8f1fce25a1a5c29db95")
    version('1.3.2', '1922d471fcef2975ca4a5072f6123ecc')

    depends_on('boost+mpi@1.55.0', type="build")
    depends_on('hdf5+mpi@1.8.18')
    depends_on('cppunit')
