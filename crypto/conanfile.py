from conans import ConanFile


class TheoCryptoConan(ConanFile):
    name = "theo_crypto"
    version = "dev"

    def build_requirements(self):
        self.build_requires("theo_test-helpers/dev@theo/testing")

    def requirements(self):
        self.requires("fmt/5.3.0@bincrafters/stable")
        