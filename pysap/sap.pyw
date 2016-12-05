#! /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from sap_main import Sap

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app = Sap()
    my_app.show()
    sys.exit(app.exec_())
