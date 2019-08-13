from conans import python_requires


base = python_requires("theo_conanfile/dev@theo/testing")

class TheoFunctionalHelpersConan(base.get_conanfile()):
    name = "theo_functional-helpers"

    def build_requirements(self):
        # important to override the base one, since functional-helpers will be 
        # used as a build requirement
        pass

    def requirements(self):
        # self.requires("theo_test-helpers/%s@theo/testing" % self.version)
        self.requires("theo_core-cpp/%s@theo/testing" % self.version)

