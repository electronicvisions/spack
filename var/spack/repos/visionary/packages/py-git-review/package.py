# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


# VISIONS: based-on spack/0.20.0
class PyGitReview(PythonPackage):
    """git-review is a tool that helps submitting git branches to gerrit"""

    homepage = "https://docs.openstack.org/infra/git-review"
    pypi = "git-review/git-review-1.25.0.tar.gz"

    # begin VISIONS: bring upstream
    version("2.3.1", sha256="24e938136eecb6e6cbb38b5e2b034a286b70b5bb8b5a2853585c9ed23636014f")
    version("2.3.0", sha256="c602d80d268ac9c0b425b11e2296f0f5ee1e248c9ddd2bced6562c855616a96f")
    version("2.2.0", sha256="fd97a00e5c15173eb097cef8e8b7915df96d878ad11eb62cb44983642b8f3a63")
    # end VISIONS
    version("2.1.0", sha256="3a6c775645b1fa8c40c49fbfce6f8d7e225a1e797a0aa92912607b1d97e61ed6")
    version("2.0.0", sha256="6e6c86b61334526c5c0f200fdf61957310b0c32208339a38c890db7fe0de5452")
    version("1.28.0", sha256="8e3aabb7b9484063e49c2504d137609401e32ad5128ff2a5cf43e98d5d3dc15a")
    version("1.27.0", sha256="7a30afdd3c62e1ef69ebda3f22c17efccd1a0a89c761b9b0d301108a11a37476")
    version("1.26.0", sha256="487c3c1d7cc81d02b303a1245e432579f683695c827ad454685b3953f70f0b94")
    version("1.25.0", sha256="087e0a7dc2415796a9f21c484a6f652c5410e6ba4562c36291c5399f9395a11d")

    depends_on("python@3.5:", type=("build", "run"), when="@2:")
    depends_on("py-setuptools", type=("build"))
    depends_on("py-pbr", type=("build"))
    depends_on("py-pbr@4.1.0:", type=("build"), when="@2:")
    depends_on("py-six", type=("build", "run"), when="@1.28.0")
    depends_on("py-requests@1.1:", type=("build", "run"))
    depends_on("git", type=("run"))

    # begin VISIONS: bring upstream
    conflicts("openssh@9:", when="@:2.2", msg="Openssh changed scp default protocol to unsupported sftp")
    # end VISIONS

    def setup_run_environment(self, env):
        env.set("PBR_VERSION", str(self.spec.version))
