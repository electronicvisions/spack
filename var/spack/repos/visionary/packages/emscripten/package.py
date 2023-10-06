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
import os

all_build_types = ('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel')

class Emscripten(Package):
    """Emscripten is a toolchain for compiling to asm.js and WebAssembly, built
    using LLVM, that lets you run C and C++ on the web at near-native speed
    without plugins."""

    homepage = "https://kripken.github.io/emscripten-site"
    url      = "https://github.com/kripken/emscripten"

    # same as built_type in cmake packages
    variant('build_type', default='Release',
            description='CMake build type',
            values=all_build_types)

    # keep in sync with emscripten-fastcomp
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
    for bt in all_build_types:
        for v in versions:
            version(v, git=url, tag=v)
            depends_on("emscripten-fastcomp@{0} build_type={1}".format(v, bt),
                       when="@{0} build_type={1}".format(v, bt))

    depends_on("cmake", type='build')
    depends_on("node-js", type='run')

    # TODO add dependency on default-jre! --obreitwi, 08-05-18 22:19:42

    path_relative_em_config = "emscripten.cfg"

    def install(self, spec, prefix):
        # emscripten does not provide a bin folder with all executables, so we
        # have to install the repo somewhere and link ourselves
        install_path = join_path(prefix, "share", "emscripten")
        install_tree(os.getcwd(), install_path)

        executables = [
            "em-config",
            "em++",
            "emar",
            "emcc",
            "emcmake",
            "emconfigure",
            "emmake",
            "emranlib",
            "emrun",
            "emscons",
            "embuilder.py",
            "emlink.py"
            ]
        mkdirp(prefix.bin)
        for exe in executables:
            os.symlink(join_path(install_path, exe),
                       join_path(prefix.bin, exe))

        # taken from https://kripken.github.io/emscripten-site/docs/tools_reference/emsdk.html#compiler-configuration-file
        em_config_lines = [
            "# .emscripten file from Linux SDK",
            "",
            "import os",
            "SPIDERMONKEY_ENGINE = ''",
            "NODE_JS = '{0}'".format(
                join_path(spec["node-js"].prefix.bin, "node")),
            "LLVM_ROOT='{0}'".format(
                spec["emscripten-fastcomp"].prefix.bin),
            "EMSCRIPTEN_ROOT='{}'".format(install_path),
            "V8_ENGINE = ''",
            "TEMP_DIR = '{0}'".format(os.environ.get("TMPDIR", "/tmp")), #TODO is there a spack /tmp setting?
            "COMPILER_ENGINE = NODE_JS",
            "JS_ENGINES = [NODE_JS]",
        ]
        with open(self.path_em_config(), "w") as f:
            f.writelines(map(lambda l: "{0}\n".format(l), em_config_lines))

    def setup_run_environment(self, run_env):
        run_env.set("EM_CONFIG", self.path_em_config())

    def path_em_config(self):
        return join_path(self.prefix, self.path_relative_em_config)
