from conans import python_requires


base = python_requires("theo_conanfile/dev@theo/testing")

class TheoTestHelpersConan(base.get_conanfile()):
    name = "theo_test-helpers"

    def build_requirements(self):
        # important to override the base one, since test-helpers will be 
        # used as a build requirement
        pass

    def requirements(self):
        self.requires("fmt/5.3.0@bincrafters/stable")

