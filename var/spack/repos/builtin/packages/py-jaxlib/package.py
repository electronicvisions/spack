# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import tempfile

import llnl.util.tty as tty

from spack.package import *


class PyJaxlib(PythonPackage, CudaPackage):
    """XLA library for Jax"""

    homepage = "https://github.com/google/jax"
    url = "https://github.com/google/jax/archive/refs/tags/jaxlib-v0.1.74.tar.gz"

    tmp_path = ""

    version("0.4.13", sha256="45766238b57b992851763c64bc943858aebafe4cad7b3df6cde844690bc34293")
    version("0.4.7", sha256="0578d5dd5035b5225cadb6a62ca5f93dd76b70292268502fc01a0fd9ca7001d0")
    version("0.4.3", sha256="2104735dc22be2b105e5517bd5bc6ae97f40e8e9e54928cac1585c6112a3d910")
    version("0.3.22", sha256="680a6f5265ba26d5515617a95ae47244005366f879a5c321782fde60f34e6d0d")
    version("0.1.74", sha256="bbc78c7a4927012dcb1b7cd135c7521f782d7dad516a2401b56d3190f81afe35")

    # jaxlib/setup.py
    depends_on("python@3.9:", when="@0.4.14:", type=("build", "run"))
    depends_on("python@3.8:", when="@0.4:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.22:", when="@0.4.14:", type=("build", "run"))
    depends_on("py-numpy@1.21:", when="@0.4.9:", type=("build", "run"))
    depends_on("py-numpy@1.20:", when="@0.3:", type=("build", "run"))
    depends_on("py-numpy@1.18:", type=("build", "run"))
    depends_on("py-scipy@1.5:", type=("build", "run"))
    depends_on("py-scipy@1.7:", when="@0.4.7:", type=("build", "run"))
    depends_on("py-ml-dtypes@0.2.0:", when="@0.4.14:", type=("build", "run"))
    depends_on("py-ml-dtypes@0.1.0:", when="@0.4.9:", type=("build", "run"))
    depends_on("py-ml-dtypes@0.0.3:", when="@0.4.7:", type=("build", "run"))

    # .bazelversion
    depends_on("bazel@5.1.1:5.9", when="@0.3:", type="build")
    # https://github.com/google/jax/issues/8440
    depends_on("bazel@4.1:4", when="@0.1", type="build")

    # README.md
    depends_on("cuda@11.8:", when="@0.4.8:+cuda")
    depends_on("cuda@11.4:", when="@0.4:+cuda")
    depends_on("cuda@11.1:", when="@0.3+cuda")
    # https://github.com/google/jax/issues/12614
    depends_on("cuda@11.1:11.7.0", when="@0.1+cuda")
    depends_on("cudnn@8.2:", when="@0.4:+cuda")
    depends_on("cudnn@8.0.5:", when="+cuda")

    # Historical dependencies
    depends_on("py-absl-py", when="@:0.3", type=("build", "run"))
    depends_on("py-flatbuffers@1.12:2", when="@0.1", type=("build", "run"))

    def install(self, spec, prefix):
        args = []
        args.append("build/build.py")
        if "+cuda" in spec:
            args.append("--enable_cuda")
            args.append("--cuda_path={0}".format(self.spec["cuda"].prefix))
            args.append("--cudnn_path={0}".format(self.spec["cudnn"].prefix))
            capabilities = ",".join(
                "{0:.1f}".format(float(i) / 10.0) for i in spec.variants["cuda_arch"].value
            )
            args.append("--cuda_compute_capabilities={0}".format(capabilities))
        args.append("--bazel_startup_options=" "--output_user_root={0}".format(self.buildtmp))
        python(*args)
        with working_dir(self.tmp_path):
            tty.warn("in dir " + self.tmp_path)
            args = std_pip_args + ["--prefix=" + self.prefix, "."]
            pip(*args)
        remove_linked_tree(self.tmp_path)
        remove_linked_tree(self.buildtmp)

    def patch(self):
        self.tmp_path = tempfile.mkdtemp(prefix="spack")
        self.buildtmp = tempfile.mkdtemp(prefix="spack")
        filter_file(
            """f"--output_path={output_path}",""",
            """f"--output_path={output_path}","""
            """f"--sources_path=%s","""
            """f"--nohome_rc'","""
            """f"--nosystem_rc'",""" % self.tmp_path,
            "build/build.py",
        )
        filter_file(
            "args = parser.parse_args()",
            "args,junk = parser.parse_known_args()",
            "build/build_wheel.py",
            string=True,
        )

