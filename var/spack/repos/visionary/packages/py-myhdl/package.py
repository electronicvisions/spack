# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


# VISIONS: based on spack/0.20.0
class PyMyhdl(PythonPackage):
    """Python as a Hardware Description Language"""

    homepage = "http://www.myhdl.org"
    pypi = "myhdl/myhdl-0.11.tar.gz"

    # begin VISIONS (added): bring upstream
    version('0.11', sha256='d30f997866cbaa2e98aa4e0609bf640ecfe5c979b29da84064ba15eb592ad111')
    # end VISIONS
    version("0.9.0", sha256="52d12a5fe2cda22558806272af3c2b519b6f7095292b8e6c8ad255fb604507a5")

    depends_on("python@2.6:2.8,3.4:")
    depends_on("py-setuptools", type="build")

    # begin VISIONS (added): bring upstream
    variant('cosim-icarus', default=False, description='Build icarus cosim support module')
    depends_on('icarus', when='+cosim-icarus')

    @run_after("install")
    def build_icarus_cosim_model(self):
        if "+cosim-icarus" in self.spec:
            make("-C", "cosimulation/icarus")
            mkdirp(join_path(self.prefix.lib, "myhdl", "share"))
            install("cosimulation/icarus/myhdl.vpi", join_path(self.prefix.lib, "myhdl", "share"))

    def setup_run_environment(self, env):
        spec = self.spec
        if "+cosim-icarus" in spec:
            env.prepend_path("IVERILOG_VPI_MODULE_PATH", join_path(self.prefix.lib, "myhdl", "share"))
    # end VISIONS
