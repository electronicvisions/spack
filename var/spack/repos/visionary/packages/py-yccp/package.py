from spack import *


class PyYccp(PythonPackage):
    """YAML with pre-Computed Common Parameters is a library for easy
    parameter-file handling. It allows for simple computations on common
    parameters which can then be referenced in the rest of the parameter
    file.
    """

    homepage = "https://github.com/obreitwi/yccp"
    url      = "https://github.com/obreitwi/yccp"

    version('1.0.0', git="https://github.com/obreitwi/yccp.git",
            commit="d3a83a40e3a30f9fb860afe5f0b977f3291e17d1")
    version('0.5.0', git="https://github.com/obreitwi/yccp.git",
            commit="d47dd39ad99704d43d29a205ae89a277b3b3bbdd")
    version('0.4.0', git="https://github.com/obreitwi/yccp.git",
            commit="055dfd62945f1b1e0990ba9318afeea325ed2de2")
    version('master', git="https://github.com/obreitwi/yccp.git")

    depends_on('python@3:', when="@1.0.0:")
    depends_on('python@:2.999.999', when="@:0.999.999")
    depends_on('pkgconfig', type="build")
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy')
    depends_on('py-pyyaml')
