#include <pybind11/pybind11.h>
#include "foo.h"
#include <QtCore/QObject>
#include <iostream>

namespace ABQ {



int add(int i, int j) {
    return i + j;
}

int foo2() {
  Counter a(600), b(300);
  QObject::connect(&a, SIGNAL(valueChanged(int)), &b, SLOT(setValue(int)));
  a.setValue(12); // a.value() == 12, b.value() == 12

  cout << a.getCounter().data() << endl;
  cout << a.squared(44) << endl;
  return a.squared(55);
}

namespace py = pybind11;

PYBIND11_MODULE(libfoo, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: cmake_example

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers

        Some other explanation about the add function.
    )pbdoc");

    m.def("foo2", &foo2, R"pbdoc(
        foo fffffff Add two numbers

        Some other explanation about the add function.
    )pbdoc");

    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
        Subtract two numbers

        Some other explanation about the subtract function.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}

} // namespace ABQ
