import os
from conans import ConanFile, CMake, tools

class Bzip2TestConan(ConanFile):
    settings = 'os', 'arch', 'compiler', 'build_type'
    generators = 'cmake'

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        assert os.path.isfile(os.path.join(self.deps_cpp_info["bzip2"].rootpath, "licenses", "LICENSE"))

        if not tools.cross_building(self.settings):
            self.run(os.path.join("bin", "example"), run_environment=True)

        if self.settings.os == 'Emscripten':
            self.run("node %s" % os.path.join("bin", "example"), run_environment=True)
