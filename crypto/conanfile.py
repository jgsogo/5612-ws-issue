from conans import python_requires


base = python_requires("theo_conanfile/dev@theo/testing")

class TheoCryptoConan(base.get_conanfile()):
    name = "theo_crypto"

    def build_requirements(self):
        if self.should_build_tests:
            self.build_requires("theo_test-helpers/%s@theo/testing" % self.version)
        super().build_requirements()

    def requirements(self):
        self.requires("fmt/5.3.0@bincrafters/stable")
