if(WIN32)
    set(TEST_PYTHONPATH     "${foo_BINARY_DIR}")
    set(TEST_LIBRARY_PATH   "${libfoo_BINARY_DIR};$ENV{PATH}")
    set(LIBRARY_PATH_VAR    "PATH")
    string(REPLACE "//" "/" TEST_PYTHONPATH "${TEST_PYTHONPATH}")
    string(REPLACE "//" "/" TEST_LIBRARY_PATH "${TEST_LIBRARY_PATH}")

    string(REPLACE ";" "//;" TEST_PYTHONPATH "${TEST_PYTHONPATH}")
    string(REPLACE ";" "//;" TEST_LIBRARY_PATH "${TEST_LIBRARY_PATH}")
else()
    set(foo_BINARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../lib)
    set(libfoo_BINARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../lib)
    set(TEST_PYTHONPATH     "${foo_BINARY_DIR}:$ENV{PYTHONPATH}")
    set(TEST_LIBRARY_PATH   "${libfoo_BINARY_DIR}:$ENV{LD_LIBRARY_PATH}")
    set(LIBRARY_PATH_VAR    "LD_LIBRARY_PATH")
endif()
add_test(math ${python_interpreter} ${CMAKE_CURRENT_SOURCE_DIR}/test.py)
set_tests_properties(math PROPERTIES ENVIRONMENT "PYTHONPATH=${TEST_PYTHONPATH};${LIBRARY_PATH_VAR}=${TEST_LIBRARY_PATH}")
