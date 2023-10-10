# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cusparselt(Package):
    """cuSPARSELt: A High-Performance CUDA Library for Sparse Matrix-Matrix
    Multiplication"""

    homepage = "https://docs.nvidia.com/cuda/cusparselt/index.html"

    version("0.5.0.1", sha256="4502db0cabec972b298f74c0e31630f602c80be89e59a413464f3daae94dfff4",
            url="https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-x86_64/libcusparse_lt-linux-x86_64-0.5.0.1-archive.tar.xz")
    version("0.4.0.7", sha256="15fc65cddcc76dceec41985a0737bc055c3944eadd02589ec8883f1196911f78",
            url="https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-x86_64/libcusparse_lt-linux-x86_64-0.4.0.7-archive.tar.xz")
    # does not work
    #url="https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse-lt/linux-x86_64/libcusparse_lt-linux-x86_64-0.3.0.3-archive.tar.xz")
    version("0.2.0", sha256="a2d724d44fc20ebd1ee481aee444cef0a803338c69208f7c70e2556920705541",
            url="https://developer.download.nvidia.com/compute/libcusparse-lt/0.2.0/local_installers/libcusparse_lt-linux-x86_64-0.2.0.1.tar.gz")

    depends_on("cuda@11:12", when="@0.5.0.1:", type=("build", "link", "run"))

    def install(self, spec, prefix):
        install_tree('.', prefix)

    @property
    def libs(self):
        return find_libraries( 'libcusparseLt*', root=self.prefix.lib, shared=True)
