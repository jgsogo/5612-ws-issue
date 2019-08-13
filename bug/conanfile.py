from conans import python_requires


base = python_requires("theo_conanfile/dev@theo/testing")

class BugConan(base.get_conanfile()):
    name = "bug"

    def build_requirements(self):
        if self.should_build_tests:
            # commenting the following line avoids the assert
            self.build_requires("functional-helpers/%s@theo/testing" % self.version)
        # The following adds 3 build requirements, but functional-helpers is not one of them
        super().build_requirements()

    def requirements(self):
        pass
        #self.requires("log/%s@theo/testing" % self.version)
        #self.requires("errors/%s@theo/testing" % self.version)

        #self.requires("fmt/5.3.0@bincrafters/stable")
        #self.requires("jsonformoderncpp/3.4.0@theo/testing")
        #self.requires("optional-lite/3.1.1@theo/testing")
