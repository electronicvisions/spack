# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyCocotbTest(PythonPackage):
    """Unit testing for cocotb"""

    homepage = "https://github.com/themperek/cocotb-test"
    pypi = "cocotb-test/cocotb-test-0.2.4.tar.gz"

    version('0.2.4', sha256='e32de80fa680390e595b7b0e279e12ee861f2493e26c9bd467fd37a6462c4006')


    depends_on('python@3.7:')
    depends_on('py-cocotb@1.5:')
    depends_on('py-pytest')
    depends_on('py-find-libpython')
