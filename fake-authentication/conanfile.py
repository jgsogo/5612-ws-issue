from conans import ConanFile


class TheoFakeAuthenticationConan(ConanFile):
    name = "theo_fake-authentication"
    version = "dev"

    def build_requirements(self):
        self.build_requires("theo_crypto/%s@theo/testing" % self.version)

    def requirements(self):
        self.requires("fmt/5.3.0@bincrafters/stable")
