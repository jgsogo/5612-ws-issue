from conans import python_requires


base = python_requires("theo_conanfile/dev@theo/testing")

class TheoCoreCppConan(base.get_conanfile()):
    name = "theo_core-cpp"

    def requirements(self):
        self.requires("theo_crypto/%s@theo/testing" % self.version)
