# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results_dialog_base.ui'
#
# Created: Wed Dec  5 15:36:03 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName(_fromUtf8("Results"))
        Results.resize(751, 576)
        self.gridLayout = QtGui.QGridLayout(Results)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(Results)
        self.webView.setStyleSheet(_fromUtf8("QWebView{\n"
"\n"
"}"))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Results)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Results)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Results.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Results.reject)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        Results.setWindowTitle(QtGui.QApplication.translate("Results", "Plugin Builder Results", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
