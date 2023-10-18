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


class TclOdfi(Package):
    """
    Some TCL libraries to help build great tools: Closures, file interaction,
    unit test design and more to be improved
    """

    homepage = "https://github.com/unihd-cag/odfi-dev-tcl"
    url      = "https://github.com/unihd-cag/odfi-dev-tcl"
    git      = "https://github.com/unihd-cag/odfi-dev-tcl.git"

    version('master', branch='master')
    version('legacy', commit='a5dd21226f71e8550632357d5fbaf6dfec188d6b')

    extends('tcl')
    depends_on('tcl@8.5.0:8.5.999')
    depends_on('tcl-tclxml', type=('build', 'run'))
    depends_on('tcl-itcl@3.4.3')
    depends_on('tcl-tcllib')

    def install(self, spec, prefix):
        install_tree('bin', spec.prefix.bin)
        install_tree('tcl', join_path(spec.prefix.lib, 'odfi'))
