#! /usr/bin/python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from sap_prog import SAPprog

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_main_app = SAPprog()
    my_main_app.show()
    sys.exit(app.exec_())
