# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based on spack/0.21.2
class Log4cxx(CMakePackage):
    """A C++ port of Log4j"""

    homepage = "https://logging.apache.org/log4cxx/latest_stable/"
    url = "https://dlcdn.apache.org/logging/log4cxx/0.12.0/apache-log4cxx-0.12.0.tar.gz"

    maintainers("nicmcd")

    # begin VISIONS (added): bring upstream (ref. spack@0.21.2)
    version("1.2.0",  sha256="09f4748aa5675ef5c0770bedbf5e00488668933c5a935a43ac5b85be2436c48a")
    version("1.1.0",  sha256="1fc7d82697534184bc0f757348d969d24852b948f63d6b17283fd1ee29c2c28a")
    # end VISIONS
    version("0.12.1", sha256="7bea5cb477f0e31c838f0e1f4f498cc3b30c2eae74703ddda923e7e8c2268d22")
    version("0.12.0", sha256="bd5b5009ca914c8fa7944b92ea6b4ca6fb7d146f65d526f21bf8b3c6a0520e44")

    variant("cxxstd", default="17", description="C++ standard", values=("11", "17"), multi=False)
    # begin VISIONS (added): bring upstream (ref. spack@0.21.2)
    variant("events_at_exit",
            default=False,
            description="Enable to use logging during the application termination",
            when="@1.2.0:",
            )
    # end VISIONS

    depends_on("cmake@3.13:", type="build")

    depends_on("apr-util")
    depends_on("apr")
    depends_on("boost+thread+system", when="cxxstd=11")
    depends_on("zlib")
    depends_on("zip")

    def cmake_args(self):
        # begin VISIONS (modified): bring upstream (ref. spack@0.21.2)
        spec = self.spec

        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("BUILD_TESTING", "off"),
        ]

        if spec.satisfies("@1.2.0:"):
            args.append(self.define_from_variant("LOG4CXX_EVENTS_AT_EXIT", "events_at_exit"))

        return args
        # end VISIONS
