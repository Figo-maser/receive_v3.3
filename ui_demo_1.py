# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_demo_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 445)
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(20, 20, 167, 301))
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox1)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox1)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox1)
        self.open_button.setObjectName("open_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox1)
        self.close_button.setObjectName("close_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox1)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox1)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.state_label = QtWidgets.QLabel(self.formGroupBox1)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(20, 340, 171, 101))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formGroupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.auto_time = QtWidgets.QGroupBox(Form)
        self.auto_time.setGeometry(QtCore.QRect(280, 30, 331, 161))
        self.auto_time.setObjectName("auto_time")
        self.timedisplay = QtWidgets.QLCDNumber(self.auto_time)
        self.timedisplay.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.timedisplay.setObjectName("timedisplay")
        self.timetext = QtWidgets.QComboBox(self.auto_time)
        self.timetext.setGeometry(QtCore.QRect(170, 30, 69, 22))
        self.timetext.setObjectName("timetext")
        self.timetext.addItem("")
        self.timetext.addItem("")
        self.timetext.addItem("")
        self.timetext.addItem("")
        self.timetext.addItem("")
        self.label_2 = QtWidgets.QLabel(self.auto_time)
        self.label_2.setGeometry(QtCore.QRect(260, 30, 54, 21))
        self.label_2.setObjectName("label_2")
        self.start_rec = QtWidgets.QPushButton(self.auto_time)
        self.start_rec.setGeometry(QtCore.QRect(20, 110, 151, 31))
        self.start_rec.setObjectName("start_rec")
        self.settime = QtWidgets.QPushButton(self.auto_time)
        self.settime.setGeometry(QtCore.QRect(240, 60, 75, 23))
        self.settime.setObjectName("settime")
        self.groupBox2 = QtWidgets.QGroupBox(Form)
        self.groupBox2.setGeometry(QtCore.QRect(280, 210, 331, 181))
        self.groupBox2.setObjectName("groupBox2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox2)
        self.textEdit.setGeometry(QtCore.QRect(140, 20, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox1.setTitle(_translate("Form", "串口设置"))
        self.s1__lb_1.setText(_translate("Form", "串口检测："))
        self.s1__box_1.setText(_translate("Form", "检测串口"))
        self.s1__lb_2.setText(_translate("Form", "串口选择："))
        self.s1__lb_3.setText(_translate("Form", "波特率："))
        self.s1__box_3.setItemText(0, _translate("Form", "115200"))
        self.s1__box_3.setItemText(1, _translate("Form", "2400"))
        self.s1__box_3.setItemText(2, _translate("Form", "4800"))
        self.s1__box_3.setItemText(3, _translate("Form", "9600"))
        self.s1__box_3.setItemText(4, _translate("Form", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form", "19200"))
        self.s1__box_3.setItemText(6, _translate("Form", "38400"))
        self.s1__box_3.setItemText(7, _translate("Form", "57600"))
        self.s1__box_3.setItemText(8, _translate("Form", "76800"))
        self.s1__box_3.setItemText(9, _translate("Form", "12800"))
        self.s1__box_3.setItemText(10, _translate("Form", "230400"))
        self.s1__box_3.setItemText(11, _translate("Form", "460800"))
        self.s1__lb_4.setText(_translate("Form", "数据位："))
        self.s1__box_4.setItemText(0, _translate("Form", "8"))
        self.s1__box_4.setItemText(1, _translate("Form", "7"))
        self.s1__box_4.setItemText(2, _translate("Form", "6"))
        self.s1__box_4.setItemText(3, _translate("Form", "5"))
        self.s1__lb_5.setText(_translate("Form", "校验位："))
        self.s1__box_5.setItemText(0, _translate("Form", "N"))
        self.open_button.setText(_translate("Form", "打开串口"))
        self.close_button.setText(_translate("Form", "关闭串口"))
        self.s1__lb_6.setText(_translate("Form", "停止位："))
        self.s1__box_6.setItemText(0, _translate("Form", "1"))
        self.s1__box_6.setItemText(1, _translate("Form", "2"))
        self.formGroupBox.setTitle(_translate("Form", "串口状态"))
        self.label.setText(_translate("Form", "已接收："))
        self.auto_time.setTitle(_translate("Form", "自动定时存储"))
        self.timetext.setItemText(0, _translate("Form", "1"))
        self.timetext.setItemText(1, _translate("Form", "2"))
        self.timetext.setItemText(2, _translate("Form", "3"))
        self.timetext.setItemText(3, _translate("Form", "5"))
        self.timetext.setItemText(4, _translate("Form", "10"))
        self.label_2.setText(_translate("Form", "分钟"))
        self.start_rec.setText(_translate("Form", "开始接收"))
        self.settime.setText(_translate("Form", "设置"))
        self.groupBox2.setTitle(_translate("Form", "文件名输入"))
        self.label_3.setText(_translate("Form", "输入文件名："))
