# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyJupyterhub(PythonPackage):
    """Multi-user server for Jupyter notebooks."""

    pypi = "jupyterhub/jupyterhub-1.0.0.tar.gz"

    version('1.3.0',    sha256='05ff701209c340c792cd103606c448c52ace772ece858380905ddd1a2136ee8e')
    version('1.1.0',    sha256='852a70225a03abd631b36a207f3ffdf69326a0db4cef539825fde39ec1b713d7')
    version('1.0.0',    sha256='33541a515a041b9a518ca057c1c4ab4215a7450fdddc206401713ee8137fa67f')
    version('0.9.4',    sha256='7848bbb299536641a59eb1977ec3c7c95d931bace4a2803d7e9b28b9256714da')

    depends_on('python@3.5:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-python-dateutil', type=('build', 'run'))
    depends_on('py-jinja2@2.11.0:', type=('build', 'run'), when='@1.3:')
    depends_on('py-jinja2', type=('build', 'run'), when='@:1.2.999')
    depends_on('py-sqlalchemy@1.1:', type=('build', 'run'))
    depends_on('py-tornado@5.1:', type=('build', 'run'), when='@1.3:')
    depends_on('py-tornado@5.0:', type=('build', 'run'), when='@:1.2.999')
    depends_on('py-traitlets@4.3.2:', type=('build', 'run'))
    depends_on('py-alembic', type=('build', 'run'))
    depends_on('py-mako', type=('build', 'run'))
    depends_on('py-async-generator@1.9:', type=('build', 'run'), when='@1.3:')
    depends_on('py-async-generator@1.8:', type=('build', 'run'), when='@:1.2.999')
    depends_on('py-requests', type=('build', 'run'))
    depends_on('py-certipy@0.1.2:', when='@1.0.0:',  type=('build', 'run'))
    depends_on('py-entrypoints', when='@1.0.0:',  type=('build', 'run'))
    depends_on('py-oauthlib@3.0:', when='@1.0.0:', type=('build', 'run'))
    depends_on('py-python-oauth2@1.0:', when='@:9.4', type=('build', 'run'))
    depends_on('py-pamela', type=('build', 'run'))
    depends_on('py-notebook', type=('build', 'run'))
    depends_on('py-prometheus-client@0.4.0:', type=('build', 'run'), when='@1.3:')
    depends_on('py-prometheus-client@0.0.21:', type=('build', 'run'), when='@:1.2.999')
    depends_on('py-jupyter-telemetry@0.1.0:', when='@1.1.0:', type=('build', 'run'))
    depends_on('py-psutil@5.6.5:', type=('build', 'run'))
    # npm needed at runtime for configurable-http-proxy
    #depends_on('npm', when='@1.1.0:', type=('build', 'run'))
    depends_on('node-js', when='@1.1.0:', type=('build', 'run'))

    @run_before('install')
    def install_npm_stuff(self):
        which('npm')('install', '-g', 'configurable-http-proxy')
