# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# F27: based on spack/0.21.2
class PyCupy(PythonPackage, CudaPackage):
    """CuPy is an open-source array library accelerated with
    NVIDIA CUDA. CuPy provides GPU accelerated computing with
    Python. CuPy uses CUDA-related libraries including cuBLAS,
    cuDNN, cuRand, cuSolver, cuSPARSE, cuFFT and NCCL to make
    full use of the GPU architecture."""

    homepage = "https://cupy.dev/"
    pypi = "cupy/cupy-8.0.0.tar.gz"

    # begin F27: added new version
    version("12.2.0", sha256="f95ffd0afeacb617b048fe028ede07b97dc9e95aca1610a022b1f3d20a9a027e")
	# end F27
    version("11.2.0", sha256="c33361f117a347a63f6996ea97446d17f1c038f1a1f533e502464235076923e2")
    version(
        "8.0.0",
        sha256="d1dcba5070dfa754445d010cdc952ff6b646d5f9bdcd7a63e8246e2472c3ddb8",
        deprecated=True
    )

    # begin F27: modified
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cython@0.29.22:2", type="build")
    depends_on("py-fastrlock@0.5:", when="@12:", type=("build", "run"))
    depends_on("py-fastrlock@0.3:", type=("build", "run"))
    depends_on("py-numpy@1.20:1.25", type=("build", "run"))
    depends_on("cuda", type=("build", "link", "run"))
    depends_on("nccl@2.8:", type=("build", "link"))
    depends_on("cudnn@8", type=("build", "link"))
    depends_on("cutensor@1.4:", when="@11:", type=("build", "link"))
    depends_on("cutensor@1.1:", type=("build", "link"))
    depends_on("cusparselt@0.2", when="@11:", type=("build", "link"))

    conflicts("~cuda")

    def setup_build_environment(self, env):
        env.set("CUPY_NUM_BUILD_JOBS", make_jobs)
        if not self.spec.satisfies("cuda_arch=none"):
            cuda_arch = self.spec.variants["cuda_arch"].value
            arch_str = ";".join("arch=compute_{0},code=sm_{0}".format(i) for i in cuda_arch)
            env.set("CUPY_NVCC_GENERATE_CODE", arch_str)
        include = []
        library = []
        for dep in self.spec.dependencies(deptype='link'):
            query = self.spec[dep.name]
            include.extend(query.headers.directories)
            library.extend(query.libs.directories)

        env.set('CUDA_PATH', self.spec['cuda'].prefix)
        env.set('CFLAGS', '-I' + ' -I'.join(include))
        env.set('LDFLAGS', '-L' + ' -L'.join(library))
    # end F27
