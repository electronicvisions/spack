# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class VisionaryDls(BundlePackage):
    """Visionary Meta Package - software needed for various experiments running
    on DLS (be it spiking or hagen mode)
    """
    version('1.0')

    variant("dev", default=True, description="With visionary-dev-tools")

    depends_on("visionary-dls-core")

    depends_on("visionary-dev-tools", when="+dev")

    depends_on('arbor@0.8.1:')
    depends_on('py-breathe')
    depends_on('py-brian2')
    depends_on('py-deap')
    depends_on('py-flask')
    depends_on('py-h5py')
    depends_on('py-ipycanvas')
    depends_on('py-ipywidgets')
    depends_on('py-lxml')  # collab tests
    depends_on('nest')
    depends_on('py-norse')
    depends_on('py-notebook')
    depends_on('py-numba')
    depends_on('py-pandas')
    depends_on('py-python-socketio')
    depends_on('py-pytorch-ignite')
    depends_on('py-pytorch-lightning')
    depends_on('py-sacred')
    depends_on('py-sbi')
    depends_on('py-scikit-learn')
    depends_on('py-seaborn')
    depends_on('py-soundfile')
    depends_on('py-sphinx')
    depends_on('py-sphinx-rtd-theme')
    depends_on('py-sphinxcontrib-jupyter')
    depends_on('py-sqlalchemy')
    depends_on('py-tqdm')
    depends_on('py-torchvision')
    depends_on('py-wfdb-python')
    depends_on('py-yccp@1.0.0:')
    depends_on('xerces-c')
