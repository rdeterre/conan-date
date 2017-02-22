from conans import ConanFile, CMake

class ConanDate(ConanFile):
    name = "date"
    version = "master"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/HowardHinnant/date"
    license = "MIT"
    generators = "cmake"
    exports = "*"
    requires = "libcurl/7.50.3@lasote/stable"

    def source(self):
        self.run("git clone {} --depth 1".format(self.url))

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "{}" {}'.format(self.conanfile_directory,
                                             cmake.command_line))
        self.run('cmake --build . {}'.format(cmake.build_config))

    def package(self):
        self.copy("*.h", dst="include/date", src="date")
        self.copy("*.so*", dst="lib", src="lib")
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["tz"]
        self.cpp_info.includedirs = ["include/date"]
