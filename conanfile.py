from conans import tools, ConanFile, CMake

import os


class Bzip2Conan(ConanFile):
    name = 'bzip2'
    version = '1.0.8'
    description = 'bzip2 is a freely available, patent free, '\
                  'high-quality data compressor. It typically compresses '\
                  'files to within 10% to 15% of the best available '\
                  'techniques (the PPM family of statistical compressors), '\
                  'whilst being around twice as fast at compression and six '\
                  'times faster at decompression.'
    homepage = 'http://www.bzip.org/'
    license = 'BSD-style license'
    url = 'https://github.com/conan-burrito/bzip2'


    settings = 'os', 'arch', 'compiler', 'build_type'
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = ['CMakeLists.txt']
    generators = 'cmake'

    build_policy = 'missing'

    @property
    def _source_subfolder(self):
        return 'src'

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def configure(self):
        # It's a C project - remove irrelevant settings
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd

    def source(self):
        tools.get(**self.conan_data['sources'][self.version])
        folder_name = '%s-%s' % (self.name, self.version)
        os.rename(folder_name, self._source_subfolder)

    def build(self):
        major = self.version.split(".")[0]
        cmake = CMake(self)
        cmake.definitions["BZ2_VERSION_STRING"] = self.version
        cmake.definitions["BZ2_VERSION_MAJOR"] = major
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)

    def package_info(self):
        self.cpp_info.libs = ['bz2']
