# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results_dialog_base.ui'
#
# Created: Wed Apr 16 13:26:49 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ResultsDialogBase(object):
    def setupUi(self, ResultsDialogBase):
        ResultsDialogBase.setObjectName(_fromUtf8("ResultsDialogBase"))
        ResultsDialogBase.resize(751, 576)
        self.gridLayout = QtGui.QGridLayout(ResultsDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.web_view = QtWebKit.QWebView(ResultsDialogBase)
        self.web_view.setStyleSheet(_fromUtf8("QWebView{\n"
"\n"
"}"))
        self.web_view.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.web_view.setObjectName(_fromUtf8("web_view"))
        self.gridLayout.addWidget(self.web_view, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ResultsDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(ResultsDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ResultsDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ResultsDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ResultsDialogBase)

    def retranslateUi(self, ResultsDialogBase):
        ResultsDialogBase.setWindowTitle(_translate("ResultsDialogBase", "Plugin Builder Results", None))

from PyQt4 import QtWebKit
