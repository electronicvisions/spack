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


class VisionaryDefaultsSpikey(Package):
    """Visionary Meta Package for the spikey platform."""


    homepage = ''
    # some random tarball, to make `spack fetch --dependencies visionary-defaults` work
    url = 'https://github.com/electronicvisions/spack-visions/archive/master.tar.gz'
    version('1.0', git='https://github.com/electronicvisions/spack-visions.git')

    # build dependencies for the Spikey software stack
    # taken from: https://electronicvisions.github.io/hbp-sp9-guidebook/pm/spikey/appendix.html#setup-software;
    depends_on('boost +clanglibcpp +graph +icu +mpi +python')
#    depends_on('libusb')  # needs to be an external requirement
    depends_on('log4cxx')
    depends_on('qt@4.8.6')
    depends_on('googletest')
    depends_on('gsl')
    depends_on('py-nose')
    # runtime dependencies of experiments
    depends_on('python@:2.8')
    depends_on('py-numpy')
    depends_on('py-scipy')
    depends_on('py-matplotlib')

    def install(self, spec, prefix):
        mkdirp(prefix.etc)
        # store a copy of this package.
        install(__file__, join_path(prefix.etc, 'visionary-defaults-spikey.py'))

        # we could create some filesystem view here?
