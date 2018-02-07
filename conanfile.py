from conans import ConanFile, CMake, tools


class DateConan(ConanFile):
    name = "date"
    version = "2.4"
    license = "MIT"
    url = "https://github.com/StiventoUser/conan-date"
    description = "A package for HowardHinnant's date"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "libcurl/7.56.1@bincrafters/stable"

    def configure(self):
        if self.settings.compiler.libcxx == "libstdc++":
            raise Exception("This package is only compatible with libstdc++11")
        else:
            self.cpp_info.cppflags = "-std=c++11"

    def source(self):
        self.run("git clone https://github.com/HowardHinnant/date")
        with tools.chdir("date"):
            self.run("git checkout v%s" % self.version)
            # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
            # if the packaged project doesn't have variables to set it properly
            tools.replace_in_file("CMakeLists.txt", "project( date_prj )", '''project( date_prj )
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CURL_ROOT_DIR"] = self.deps_cpp_info["libcurl"].rootpath
        cmake.definitions["BUILD_TZ_STATIC"] = "OFF" if self.options.shared else "ON"
        cmake.configure(source_folder="date")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="date/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tz"]
