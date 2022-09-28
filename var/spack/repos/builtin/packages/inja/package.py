# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Inja(CMakePackage):
    """Inja is a template engine for modern C++, loosely inspired by jinja for python.
    """

    homepage = "https://github.com/pantor/inja"
    url      = "https://github.com/pantor/inja/archive/refs/tags/v3.3.0.tar.gz"

    version('3.3.0', sha256='e628d994762dcdaa9a97f63a9b8b73d9af51af0ffa5acea6bdbba0aceaf8ee25')

    depends_on('nlohmann-json@3.8.0:')

    def cmake_args(self):
        args = [
            '-DINJA_USE_EMBEDDED_JSON:BOOL=OFF',
            '-DINJA_BUILD_TESTS:BOOL=OFF',
            '-DBUILD_BENCHMARK:BOOL=OFF',
            '-DCOVERALLS:BOOL=OFF',
        ]
        return args
