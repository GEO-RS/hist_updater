# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'histogram_handler_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HistogramHandlerDialogBase(object):
    def setupUi(self, HistogramHandlerDialogBase):
        HistogramHandlerDialogBase.setObjectName("HistogramHandlerDialogBase")
        HistogramHandlerDialogBase.resize(670, 460)
        self.button_box = QtWidgets.QDialogButtonBox(HistogramHandlerDialogBase)
        self.button_box.setGeometry(QtCore.QRect(400, 370, 191, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.comboBox = QtWidgets.QComboBox(HistogramHandlerDialogBase)
        self.comboBox.setGeometry(QtCore.QRect(400, 160, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(HistogramHandlerDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(580, 220, 71, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(400, 220, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEditNa = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEditNa.setGeometry(QtCore.QRect(180, 100, 161, 31))
        self.lineEditNa.setObjectName("lineEditNa")
        self.lineEditHo = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEditHo.setGeometry(QtCore.QRect(180, 140, 161, 31))
        self.lineEditHo.setObjectName("lineEditHo")
        self.lineEditPo = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEditPo.setGeometry(QtCore.QRect(180, 180, 161, 31))
        self.lineEditPo.setObjectName("lineEditPo")
        self.lineEditUs = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEditUs.setGeometry(QtCore.QRect(180, 220, 161, 31))
        self.lineEditUs.setObjectName("lineEditUs")
        self.lineEditPa = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEditPa.setGeometry(QtCore.QRect(180, 260, 161, 31))
        self.lineEditPa.setObjectName("lineEditPa")
        self.lineEditSc = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEditSc.setGeometry(QtCore.QRect(180, 300, 161, 31))
        self.lineEditSc.setObjectName("lineEditSc")
        self.lineEditTa = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEditTa.setGeometry(QtCore.QRect(180, 340, 161, 31))
        self.lineEditTa.setObjectName("lineEditTa")
        self.textEdit = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 140, 151, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 220, 151, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 260, 151, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 300, 151, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit_7.setGeometry(QtCore.QRect(10, 340, 151, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit_8.setGeometry(QtCore.QRect(400, 120, 101, 31))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(HistogramHandlerDialogBase)
        self.textEdit_9.setGeometry(QtCore.QRect(10, 380, 151, 31))
        self.textEdit_9.setObjectName("textEdit_9")
        self.lineEditSk = QtWidgets.QLineEdit(HistogramHandlerDialogBase)
        self.lineEditSk.setGeometry(QtCore.QRect(180, 380, 161, 31))
        self.lineEditSk.setObjectName("lineEditSk")

        self.retranslateUi(HistogramHandlerDialogBase)
        self.button_box.accepted.connect(HistogramHandlerDialogBase.accept)
        self.button_box.rejected.connect(HistogramHandlerDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(HistogramHandlerDialogBase)

    def retranslateUi(self, HistogramHandlerDialogBase):
        _translate = QtCore.QCoreApplication.translate
        HistogramHandlerDialogBase.setWindowTitle(_translate("HistogramHandlerDialogBase", "Histogram Handler"))
        self.pushButton.setText(_translate("HistogramHandlerDialogBase", "Select folder"))
        self.textEdit.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DB_NAME</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DB_HOST</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DB_PORT</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DB_USERNAME</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DB_PASSWORD</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DB_SCHEMA</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">DB_TABLE</span></p></body></html>"))
        self.textEdit_8.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Select drive</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("HistogramHandlerDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">SKIPFACTOR</span></p></body></html>"))

