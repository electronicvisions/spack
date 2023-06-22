# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyLibpsf(PythonPackage):
    """An easy-to-use Python package for reading Cadence PSF data."""

    # Do not use pypi since no source is supplied there
    homepage = "https://gitlab.com/libpsf/libpsf-python"
    git      = "https://gitlab.com/libpsf/libpsf-python"

    build_directory = 'libpsf'

    version('0.1.4', commit='2af796caffe4b6f60cc42d24307a5207387f87c3')

    depends_on('libpsf')
    depends_on('boost+python')  # not sure if needed
    depends_on('py-numpy@1.10:')
