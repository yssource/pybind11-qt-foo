#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class YsalphaConan(ConanFile):
    name = "ysalpha"
    version = "0.0.0"
    description = "Keep it short"
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "ysalpha", "logging")
    url = "https://github.com/bincrafters/conan-ysalpha"
    homepage = "https://github.com/original_author/original_lib"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    exports = ["LICENSE.md"]      # Packages the license for the conanfile.py
    # Remove following lines if the target lib does not use cmake.
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    # default_options = {"shared": False, "fPIC": False}

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "src"
    _build_subfolder = "build"

    # requires = (
    #     "OpenSSL/1.0.2p@conan/stable",
    #     "zlib/1.2.11@conan/stable"
    # )

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def requirements(self):
        # self.requires("cmake_findboost_modular/1.66.0@{}/{}".format("bincrafters", "stable"))
        self.requires("pybind11/2.2.4@{}/{}".format("conan", "stable"))
        # self.requires(
        #     "libodb-sqlite/2.5.0-b.9@{}/{}".format("yssource", "testing"))
        # # self.requires("boost_asio/1.67.0@{}/{}".format("bincrafters", "stable"))
        # # self.requires(
        # #     "boost_python/1.67.0@{}/{}".format("bincrafters", "stable"))
        # self.requires(
        #     "boost_algorithm/1.67.0@{}/{}".format("bincrafters", "stable"))
        # self.requires(
        #     "boost_filesystem/1.67.0@{}/{}".format("bincrafters", "stable"))
        # self.requires(
        #     "mongo-cxx-driver/3.3.0@{}/{}".format("bincrafters", "stable"))
        # # self.requires(
        # #     "mongo-c-driver/[~=1.9]@{}/{}".format("bincrafters", "stable"))
        # # self.requires("boost/1.67.0@{}/{}".format("conan", "stable"))
        # # self.requires("boost_format/1.67.0@{}/{}".format("bincrafters", "stable"))
        # # self.requires("boost_python/1.67.0@{}/{}".format("bincrafters", "stable"))

    # def source(self):
    #     source_url = "https://github.com/libauthor/ysalpha"
    #     tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version), sha256="Please-provide-a-checksum")
    #     extracted_dir = self.name + "-" + self.version

    #     # Rename to "source_subfolder" is a convention to simplify later steps
    #     os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.definitions["BUILD_TESTS"] = False  # example
        # cmake.configure(build_folder=self._build_subfolder)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        cmake.install()
        # cmake.test()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses",
                  src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()
        # If the CMakeLists.txt has a proper install method, the steps below may be redundant
        # If so, you can just remove the lines below
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="*", dst="include", src=include_folder)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        # if self.settings.compiler == "gcc":
        #      self.cpp_info.cppflags = "-std=c++11"
