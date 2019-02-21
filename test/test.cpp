#include "foo.h"
#include <iostream>
#include <QtCore/QObject>
using namespace std;
using namespace ABQ;

void foo() {
  Counter a(600), b(300);
  QObject::connect(&a, SIGNAL(valueChanged(int)),
                   &b, SLOT(setValue(int)));
  a.setValue(12);  // a.value() == 12, b.value() == 12

  cout << a.getCounter().data() << endl;
  cout << a.squared(44) << endl;
}

int main(int argc, char *argv[]) {
  foo();
  return 0;
}
