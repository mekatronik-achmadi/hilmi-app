#-------------------------------------------------
#
# Project created by QtCreator 2016-05-27T14:19:27
#
#-------------------------------------------------

QT       += core gui printsupport

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = sap
TEMPLATE = app


SOURCES +=  main.cpp\
            sap.cpp \
            sqlsh.cpp \
            app.cpp \
    sqldata.cpp

HEADERS  += sap.h \
            sqlsh.h \
    sqldata.h

FORMS    += sap.ui
