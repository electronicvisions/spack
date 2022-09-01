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

class VisionaryNest(CMakePackage):
    """This repository contains many NEST models developed within the
    Electronic Vision(s) group, compiled into a single nest module."""

    # url = "https://brainscales-r.kip.uni-heidelberg.de/projects/model-visionary-nest"
    homepage = "https://brainscales-r.kip.uni-heidelberg.de/projects/model-visionary-nest"

    version('1.2',
            git="gerrit.bioai.eu:model-visionary-nest.git",
            commit="693455678a0ed645c8f1c006200a1f16a2a3de9c", preferred=True)
    version('1.0',
            git="gerrit.bioai.eu:model-visionary-nest.git",
            commit="1e4c5a4611875a97379b49a08b8769d3e2b76108", preferred=True)
    version('master',
            git="gerrit.bioai.eu:model-visionary-nest.git",
            branch="master")

    depends_on('nest@2.14.0:+modules')

    def cmake_args(self):
        # TODO: should be specified by nest-package
        # TODO: turn this package into extension of nest
        args = ["-DCMAKE_CXX_FLAGS=-I{0}".format(
                join_path(self.spec["nest"].prefix, "include", "nest"))]
        return args

    def setup_environment(self, spack_env, run_env):
        run_env.append_path("NEST_MODULES", "visionarymodule")

    @property
    def root_cmakelists_dir(self):
        return "nest-module"
