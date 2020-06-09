# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyJupyterTelemetry(PythonPackage):
    """Configurable event-logging for Jupyter applications and extensions."""

    homepage = "https://jupyter-telemetry.readthedocs.io"
    url      = "https://files.pythonhosted.org/packages/source/j/jupyter_telemetry/jupyter_telemetry-0.1.0.tar.gz"

    version('0.1.0', sha256='445c613ae3df70d255fe3de202f936bba8b77b4055c43207edf22468ac875314')

    depends_on('python@3.5:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-traitlets', type=('build', 'run'))
    depends_on('py-jsonschema', type=('build', 'run'))
    depends_on('py-python-json-logger', type=('build', 'run'))
    depends_on('py-ruamel-yaml', type=('build', 'run'))
