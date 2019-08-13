from conans import ConanFile


class TheoTestHelpersConan(ConanFile):
    name = "theo_test-helpers"

    def requirements(self):
        self.requires("fmt/5.3.0@bincrafters/stable")

