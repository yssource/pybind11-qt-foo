#include "foo.h"
#include <QDate>
#include <QDebug>

using namespace std;

namespace ABQ {

Counter::Counter(const int m) : m_value(m) {
  qDebug() << "Date: " << m_value << " Date2:" << QDate::currentDate();
}

int Counter::value() const { return m_value; }

string Counter::getCounter() const { return to_string(m_value); }

void Counter::setValue(int value) {
  if (value != m_value) {
    m_value = value;
    emit valueChanged(value);
  }
}

int Counter::squared(int x) { return x * x; }

} // namespace ABQ
