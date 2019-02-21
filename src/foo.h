#pragma once
// #include <QString>
#include <QtCore/QObject>
#include <string>
using namespace std;

namespace ABQ {
#if defined _WIN32
#if LIBFOO_BUILD
#define LIBFOO_API __declspec(dllexport)
#else
#define LIBFOO_API __declspec(dllimport)
#endif
#else
#define LIBFOO_API
#endif

class LIBFOO_API Counter : public QObject {
  Q_OBJECT
  int m_value;

public:
  Counter(const int);
  int value() const;
  string getCounter() const;
  int squared(int x);
public slots:
  void setValue(int value);
signals:
  void valueChanged(int newValue);
};

} // namespace ABQ
