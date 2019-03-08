# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob


class Gccxml(CMakePackage):
    """gccxml dumps an XML description of C++ source code using an extension of
    the GCC C++ compiler."""

    homepage = "http://gccxml.github.io"
    git      = "https://github.com/gccxml/gccxml.git"

    version('develop', branch='master')
    version('latest', commit='3afa8ba5be6866e603dcabe80aff79856b558e24',
            preferred=True)

    patch('darwin-gcc.patch', when='%gcc platform=darwin')
    # taken from https://github.com/gccxml/gccxml/issues/11#issuecomment-140334118
    patch('gcc-5.patch', when='%gcc@5:')

    # last supported version seems to be 4.9.3
    depends_on('gcc@:4.9.3', type='run')

    @run_after('install')
    def fix_path_to_gcc(self):
        path_to_config = glob.glob(join_path(self.prefix.share,
                                             'gccxml-*/gccxml_config'))
        if len(path_to_config) != 1:
            raise InstallError('multiple gccxml_config files found!')
        path_to_config = path_to_config[0]

        # fix path to 'runtime' g++ in gccxml's config
        filter_file('^GCCXML_COMPILER=.*', 'GCCXML_COMPILER="%s"' % join_path(
            self.spec['gcc'].prefix.bin, 'g++'), path_to_config)
