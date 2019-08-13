from conans import ConanFile, CMake, tools


class PythonRequires(ConanFile):
    name = "theo_conanfile"
    version = "dev"

def get_conanfile(additional_options = dict(), additional_default_options = dict()):
    class BaseConanFile(ConanFile):
        settings = "os", "compiler", "build_type", "arch"

        @property
        def cross_building(self):
            return tools.cross_building(self.settings)

        @property
        def should_build_tests(self):
            # develop is false when the package is used as a requirement.
            return self.develop and (not self.cross_building or self.settings.os == "Emscripten")

        def build_requirements(self):
            if self.should_build_tests:
                #self.build_requires("docopt.cpp/0.6.2@theo/testing")
                #self.build_requires("doctest/2.2.3@theo/testing")
                #self.build_requires("doctest-async/2.0.12@theo/testing")
                pass

    return BaseConanFile
