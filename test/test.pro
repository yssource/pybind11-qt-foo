######################################################################
# Automatically generated by qmake (3.1) Wed Feb 20 10:24:09 2019
######################################################################
TEMPLATE = app
TARGET = test
QT += core
config -= gui
OBJECTS_DIR = obj
# includepath += . ../src

# HEADERS += test.h
SOURCES += test.cpp
DEFINES += LIBFOO_BUILD

unix:LIBS += -Wl,-rpath,. -Wl,-rpath,../lib -L../lib -lfoo
unix:INCLUDEPATH += ../src
linux-*:LIBS += -lrt

# target.path = ../lib
# INSTALLS += target
# Directories
