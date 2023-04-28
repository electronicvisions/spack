# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VisionaryAsic(BundlePackage):
    """Visionary ASIC-specific environment. For now this serves as a minimum
    software environment for our ASIC-related CI jobs (e.g. building bitfiles)
    in the ASIC container. It is not to be used with the visionary software
    stack (for now)."""

    version('1.0')

    # verilog-ethernet test deps
    depends_on('py-cocotb')
    depends_on('py-cocotb-bus')
    depends_on('py-cocotb-test')
    depends_on('py-cocotbext-axi')
    depends_on('py-cocotbext-eth')
    depends_on('py-construct')
    depends_on('py-jinja2')
    depends_on('py-pytest')
    depends_on('py-pytest-xdist')
    depends_on('py-scapy')
    depends_on('py-myhdl+cosim-icarus')

    depends_on('tcl-osys@1.1.1-post1')
