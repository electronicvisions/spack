# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack.package import *


# F27: based on spack/0.21.2
_versions = {
    # begin F27: added new version
    # cuTensor 1.7.0
    "1.7.0.1": {
        "Linux-x86_64": "dd3557891371a19e73e7c955efe5383b0bee954aba6a30e4892b0e7acb9deb26",
        "Linux-ppc64le": "af4ad5e29dcb636f1bf941ed1fd7fc8053eeec4813fbc0b41581e114438e84c8",
        "Linux-aarch64": "c31f8e4386539434a5d1643ebfed74572011783b4e21b62be52003e3a9de3720",
    },
    # end F27
    # cuTensor 1.5.0
    "1.5.0.3": {
        "Linux-x86_64": "4fdebe94f0ba3933a422cff3dd05a0ef7a18552ca274dd12564056993f55471d",
        "Linux-ppc64le": "ad736acc94e88673b04a3156d7d3a408937cac32d083acdfbd8435582cbe15db",
        "Linux-aarch64": "5b9ac479b1dadaf40464ff3076e45f2ec92581c07df1258a155b5bcd142f6090",
    }
}


class Cutensor(Package):
    """NVIDIA cuTENSOR Library is a GPU-accelerated tensor linear algebra
    library providing tensor contraction, reduction and elementwise
    operations."""

    homepage = "https://developer.nvidia.com/cutensor"

    maintainers("bvanessen")
    url = "cutensor"

    for ver, packages in _versions.items():
        key = "{0}-{1}".format(platform.system(), platform.machine())
        pkg = packages.get(key)
        cutensor_ver = ver

        cuda_ver = "10.0"
        if platform.machine() == "aarch64":
            cuda_ver = "11.0"

        if pkg:
            version(cutensor_ver, sha256=pkg)
            # Add constraints matching CUDA version to cuTensor version
            cuda_req = "cuda@{0}:".format(cuda_ver)
            cutensor_ver_req = "@{0}".format(cutensor_ver)
            depends_on(cuda_req, when=cutensor_ver_req)

    def url_for_version(self, version):
        # Get the system and machine arch for building the file path
        sys = "{0}-{1}".format(platform.system(), platform.machine())
        # Munge it to match Nvidia's naming scheme
        sys_key = sys.lower()
        sys_key = sys_key.replace("aarch64", "sbsa")

        url = "https://developer.download.nvidia.com/compute/cutensor/redist/libcutensor/{0}/libcutensor-{0}-{1}-archive.tar.xz"
        return url.format(sys_key, version)

    def install(self, spec, prefix):
        install_tree(".", prefix)

    # begin F27: modified
    @property
    def libs(self):
        cuda_ver = self.spec["cuda"].version.up_to(1)
        return find_libraries('{0}/libcutensor*'.format(cuda_ver), root=self.prefix.lib, shared=True)
    # end F27
