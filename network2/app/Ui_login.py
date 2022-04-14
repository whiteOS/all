# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\OneDrive - stu.csust.edu.cn\桌面\Python\network\ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import views
from Ui_connect import Ui_connect
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_login, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, login_ui):
        login_ui.setObjectName("login_ui")
        login_ui.setWindowModality(QtCore.Qt.NonModal)
        login_ui.resize(300, 240)
        login_ui.setFixedSize(300, 240)
        self.centralwidget = QtWidgets.QWidget(login_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_1 = QtWidgets.QFormLayout()
        self.formLayout_1.setObjectName("formLayout_1")
        self.label_a = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.label_a.sizePolicy().hasHeightForWidth())
        self.label_a.setSizePolicy(sizePolicy)
        self.label_a.setObjectName("label_a")
        self.formLayout_1.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_a)
        self.editAccount = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.editAccount.sizePolicy().hasHeightForWidth())
        self.editAccount.setSizePolicy(sizePolicy)
        self.editAccount.setText("")
        self.editAccount.setMaxLength(36)
        self.editAccount.setObjectName("editAccount")
        self.formLayout_1.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editAccount)
        self.verticalLayout.addLayout(self.formLayout_1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_2.setObjectName("formLayout_2")
        self.editPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.editPassword.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.editPassword.sizePolicy().hasHeightForWidth())
        self.editPassword.setSizePolicy(sizePolicy)
        self.editPassword.setText("")
        self.editPassword.setMaxLength(36)
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword.setObjectName("editPassword")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editPassword)
        self.label_p = QtWidgets.QLabel(self.centralwidget)
        self.label_p.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.label_p.sizePolicy().hasHeightForWidth())
        self.label_p.setSizePolicy(sizePolicy)
        self.label_p.setWordWrap(False)
        self.label_p.setObjectName("label_p")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_p)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setAutoDefault(True)
        self.btn_login.setDefault(True)
        self.btn_login.setFlat(False)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout.addWidget(self.btn_login)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setAutoDefault(True)
        self.btn_exit.setDefault(True)
        self.btn_exit.setFlat(False)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        login_ui.setCentralWidget(self.centralwidget)

        self.editAccount.setText(views.getUUID())


        self.retranslateUi(login_ui)
        self.editAccount.returnPressed.connect(self.btn_login.click)
        self.editPassword.returnPressed.connect(self.btn_login.click)
        self.btn_login.clicked.connect(self.login)
        self.btn_exit.clicked.connect(views.close)
        QtCore.QMetaObject.connectSlotsByName(login_ui)

    def login(self):
        pd = self.editPassword.text()
        if pd == views.getPassword():
            MainWindow.close()
            connect.show()
        else:
            QtWidgets.QMessageBox.warning(self,
                    "警告",
                    "账号或密码错误！",
                    QtWidgets.QMessageBox.Yes)
            self.lineEdit.setFocus()



    def retranslateUi(self, login_ui):
        _translate = QtCore.QCoreApplication.translate
        login_ui.setWindowTitle(_translate("login_ui", "登录"))
        self.label_a.setText(_translate("login_ui", "<html><head/><body><p><span style=\" font-size:12pt;\">账号:</span></p></body></html>"))
        self.label_p.setText(_translate("login_ui", "<html><head/><body><p><span style=\" font-size:12pt;\">密码:</span></p></body></html>"))
        self.btn_login.setText(_translate("login_ui", "登录"))
        self.btn_exit.setText(_translate("login_ui", "退出"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    login = Ui_login()
    connect = Ui_connect()
    login.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())