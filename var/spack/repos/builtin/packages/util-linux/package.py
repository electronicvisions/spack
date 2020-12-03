# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class UtilLinux(AutotoolsPackage):
    """Util-linux is a suite of essential utilities for any Linux system."""

    homepage = "http://freecode.com/projects/util-linux"
    url      = "https://www.kernel.org/pub/linux/utils/util-linux/v2.29/util-linux-2.29.2.tar.gz"
    list_url = "https://www.kernel.org/pub/linux/utils/util-linux"
    list_depth = 1

    version('2.36.1', sha256='37de03dbb98cdeffdf9e754122b0aca2a9bbdc19769f6570dfcb6f123643bf53')
    version('2.35.2', sha256='7c7e1e6cd000c2d70523fc2852a7712befcd896138e69db93e35d29861ea936d')
    version('2.29.2', sha256='29ccdf91d2c3245dc705f0ad3bf729ac41d8adcdbeff914e797c552ecb04a4c7')
    version('2.29.1', sha256='a6a7adba65a368e6dad9582d9fbedee43126d990df51266eaee089a73c893653')
    version('2.25',   sha256='7e43273a9e2ab99b5a54ac914fddf5d08ba7ab9b114c550e9f03474672bd23a1')

    variant('python',
            default=False,
            description='Build with python bindings')

    depends_on('python@2.7:', when='+python')
    depends_on('pkgconfig')

    # Make it possible to disable util-linux's libuuid so that you may
    # reliably depend_on(`libuuid`).
    variant('libuuid', default=True, description='Build libuuid')

    def url_for_version(self, version):
        url = "https://www.kernel.org/pub/linux/utils/util-linux/v{0}/util-linux-{1}.tar.gz"
        return url.format(version.up_to(2), version)

    def configure_args(self):
        config_args = [
            '--disable-use-tty-group',
            '--disable-makeinstall-chown',
        ]
        config_args.extend(self.enable_or_disable('libuuid'))
        config_args.extend(self.with_or_without('python'))
        return config_args
