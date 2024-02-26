# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VisionarySlurmviz(BundlePackage):
    """Visionary Meta Package to make sure the dependecies for slurmviz are built."""

    # TODO: Make new versions once we upgrade from 17.11 -> hwloc 2.0+ is supported
    version('1.0')


    # OJB (2018-08-07): taken from slurm package, default values ajdusted
    # from False to True for all variants
    variant('mariadb', default=True, description='Use MariaDB instead of MySQL')
    variant('hwloc', default=True, description='Enable hwloc support')
    variant('hdf5', default=True, description='Enable hdf5 support')
    variant('readline', default=True, description='Enable readline support')

    depends_on('autoconf')
    depends_on('automake')
    depends_on('curl')
    depends_on('glib')
    depends_on('json-c')
    depends_on('libtomlc99')
    depends_on('libtool')
    depends_on('lz4')
    depends_on('munge localstatedir="/opt/spack_views/visionary-slurmviz/var"')
    depends_on('openssl')
    # package is used to build slurmviz externally
    # -> need pkgconfig as non-build dependency
    depends_on('pkgconfig')
    depends_on('readline', when='+readline')
    depends_on('zlib')

    depends_on('gtkplus@2')
    depends_on('hdf5', when='+hdf5')
    # currently there is no support for hwloc 2.0+ in slurm-17.11 it seems
    depends_on('hwloc@:1.999.999', when='+hwloc')
    depends_on('mariadb', when='+mariadb')
