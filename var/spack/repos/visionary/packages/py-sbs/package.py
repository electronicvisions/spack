from spack import *


class PySbs(PythonPackage):
    """Spike based Sampling framework"""

    homepage = "https://github.com/electronicvisions/spike-based-sampling.git"
    url      = "https://github.com/electronicvisions/spike-based-sampling.git"
    git      = "https://github.com/electronicvisions/spike-based-sampling.git"

    version('master')
    version('1.8.1', commit='aa8a9d9ab9985fe62f819e7837ea313a1b52ec83')
    version('1.8.0', commit='45ad25018f91a0d03391621eaece507df92f8c87')
    version('1.7.2', commit='c4fcb563c580af9ff7b132295fe1620b31ab3829')
    version('1.7.1', commit='d5a97cfd8c0cd6ec9f98b0bfbd1f0a284eaf569e')
    version('1.6.5', commit='3ce21de823b7df37fb83b87ec7f9607e781aaa1a')
    version('1.6.2', commit='318ed67dbf6330323c4eb398219701c14eb7a945')
    version('1.5.2', commit='c0adeed57a467b4edaa399a623fb2865ac2a06c6')
    version('1.4.1', commit='655c930dc07efec01ffe02e44fcc99660e4c96c3')
    version('1.4.0', commit='68889dbd832cb6b8bf17f38684634e3126adac1f')
    version('1.3.2', commit='87bb9787b4bdc741e349ad17191165a496e85042')

    depends_on('pkgconfig', type="build")
    depends_on('python@:2.8', type=("build", "run"))
    depends_on('py-setuptools', type="build")
    depends_on('py-cython', type='build')
    depends_on('py-numpy', type=("build", "link", "run"))
    depends_on('py-scipy', type=("build", "run"))
    depends_on('py-matplotlib', type=("build", "run"))
    depends_on('py-pynn@0.8:', type=("build", "run"))

    @when("@1.0.0:1.5.2")
    def patch(self):
        # remove unnecessary h5py dependency from source code
        filter_file("^import h5py$", "# import h5py", "sbs/meta.py")

    @when("@:1.7.0")
    def patch(self):
        filter_file(r"import os$", r"import os, numpy", "setup.py")
        filter_file("zip_safe=True,", "zip_safe=True, include_dirs=[numpy.get_include()],",
                    "setup.py", )
