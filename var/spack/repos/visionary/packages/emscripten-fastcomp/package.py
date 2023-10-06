##############################################################################
# Copyright (c) 2017, Los Alamos National Security, LLC
# Produced at the Los Alamos National Laboratory.
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


class EmscriptenFastcomp(CMakePackage):
    """Fastcomp is the default compiler core for Emscripten. It is a new LLVM
    backend that converts the LLVM Intermediate Representation (IR) created by
    Clang (from C/C++) into JavaScript."""

    homepage = "https://kripken.github.io/emscripten-site"
    url      = "https://github.com/kripken/emscripten-fastcomp"

    url_clang = "https://github.com/kripken/emscripten-fastcomp-clang"

    # every version has a corresponding clang version
    versions = [
            "1.38.25",
            "1.38.8",
            "1.38.7",
            "1.38.6",
            "1.38.5",
            "1.38.4",
            "1.38.3",
            "1.38.2",
            "1.38.1",
            "1.38.0",
            "1.37.40",
        ]
    for v in versions:
        version(v, git=url, tag=v)
        resource(name='emscripten-fastcomp-clang', git=url_clang, tag=v,
                 placement="tools/clang")

    depends_on("cmake", type='build')

    def cmake_args(self):
        options = [
            '-DLLVM_TARGETS_TO_BUILD=X86;JSBackend',
            '-DLLVM_INCLUDE_EXAMPLES=OFF',
            '-DLLVM_INCLUDE_TESTS=OFF',
            '-DCLANG_INCLUDE_TESTS=OFF',
        ]
        return options

