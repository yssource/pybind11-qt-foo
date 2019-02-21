cmake_minimum_required(VERSION 2.8.12)
project(cmake_example)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# find_package(pybind11 REQUIRED)  # or add_subdirectory(pybind11)


find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
# find_package(PythonLibs REQUIRED)
# find_package(Shiboken REQUIRED)

# find_program(GENERATOR generatorrunner REQUIRED)
# if (NOT GENERATOR)
#     message(FATAL_ERROR "You need to specify GENERATOR variable (-DGENERATOR=value)")
# endif()

# find_package(Qt5Core)
find_package(Qt5 REQUIRED Core)

get_target_property(QtCore_location Qt5::Core LOCATION)
get_filename_component(QtCore_libdir ${QtCore_location} DIRECTORY)
message(STATUS "${QtCore_libdir}")
message(STATUS "${QtCore_location}")

enable_testing()
message(status ${CONAN_LIBS})
add_subdirectory(binding)

# pybind11_add_module(cmake_example cc/src/data/main.cpp)
# pybind11_add_module(driver cc/src/data/db.cxx)

