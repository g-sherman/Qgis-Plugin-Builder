# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pluginbuilder.ui'
#
# Created: Sun Feb  6 08:00:03 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PluginBuilder(object):
    def setupUi(self, PluginBuilder):
        PluginBuilder.setObjectName(_fromUtf8("PluginBuilder"))
        PluginBuilder.resize(846, 456)
        self.gridLayout = QtGui.QGridLayout(PluginBuilder)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(PluginBuilder)
        self.webView.setMinimumSize(QtCore.QSize(380, 390))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(",Verdana,sans"))
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.webView.setFont(font)
        self.webView.setStyleSheet(_fromUtf8("QWebView{\n"
"    font: Georgia, Verdana, sans;\n"
"    font-size:1.0em;\n"
"    background-color: rgb(210, 255, 217);\n"
"    border-left: solid 2px black;\n"
"}"))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 9, 1)
        self.line = QtGui.QFrame(PluginBuilder)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 1, 9, 1)
        self.label = QtGui.QLabel(PluginBuilder)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.lineEdit_class_name = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_class_name.setText(_fromUtf8(""))
        self.lineEdit_class_name.setObjectName(_fromUtf8("lineEdit_class_name"))
        self.gridLayout.addWidget(self.lineEdit_class_name, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(PluginBuilder)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.lineEdit_title = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_title.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_title.setText(_fromUtf8(""))
        self.lineEdit_title.setObjectName(_fromUtf8("lineEdit_title"))
        self.gridLayout.addWidget(self.lineEdit_title, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(PluginBuilder)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.lineEdit_description = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_description.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_description.setText(_fromUtf8(""))
        self.lineEdit_description.setObjectName(_fromUtf8("lineEdit_description"))
        self.gridLayout.addWidget(self.lineEdit_description, 2, 3, 1, 1)
        self.label_4 = QtGui.QLabel(PluginBuilder)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)
        self.lineEdit_version_no = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_version_no.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_version_no.setObjectName(_fromUtf8("lineEdit_version_no"))
        self.gridLayout.addWidget(self.lineEdit_version_no, 3, 3, 1, 1)
        self.label_5 = QtGui.QLabel(PluginBuilder)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)
        self.lineEdit_min_version_no = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_min_version_no.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_min_version_no.setObjectName(_fromUtf8("lineEdit_min_version_no"))
        self.gridLayout.addWidget(self.lineEdit_min_version_no, 4, 3, 1, 1)
        self.label_6 = QtGui.QLabel(PluginBuilder)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)
        self.lineEdit_menu_text = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_menu_text.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_menu_text.setText(_fromUtf8(""))
        self.lineEdit_menu_text.setObjectName(_fromUtf8("lineEdit_menu_text"))
        self.gridLayout.addWidget(self.lineEdit_menu_text, 5, 3, 1, 1)
        self.label_7 = QtGui.QLabel(PluginBuilder)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 2, 1, 1)
        self.lineEdit_company_name = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_company_name.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_company_name.setText(_fromUtf8(""))
        self.lineEdit_company_name.setObjectName(_fromUtf8("lineEdit_company_name"))
        self.gridLayout.addWidget(self.lineEdit_company_name, 6, 3, 1, 1)
        self.label_8 = QtGui.QLabel(PluginBuilder)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 7, 2, 1, 1)
        self.lineEdit_email_address = QtGui.QLineEdit(PluginBuilder)
        self.lineEdit_email_address.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_email_address.setText(_fromUtf8(""))
        self.lineEdit_email_address.setObjectName(_fromUtf8("lineEdit_email_address"))
        self.gridLayout.addWidget(self.lineEdit_email_address, 7, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(PluginBuilder)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 8, 3, 1, 1)
        self.line_2 = QtGui.QFrame(PluginBuilder)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 9, 0, 1, 2)

        self.retranslateUi(PluginBuilder)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PluginBuilder.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginBuilder)

    def retranslateUi(self, PluginBuilder):
        PluginBuilder.setWindowTitle(QtGui.QApplication.translate("PluginBuilder", "QGIS Plugin Builder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PluginBuilder", "Class name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PluginBuilder", "Descriptive title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PluginBuilder", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PluginBuilder", "Version number", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_version_no.setText(QtGui.QApplication.translate("PluginBuilder", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PluginBuilder", "Minimum QGIS version", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_min_version_no.setText(QtGui.QApplication.translate("PluginBuilder", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PluginBuilder", "Text for the menu item", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PluginBuilder", "Company name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PluginBuilder", "Email address", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
