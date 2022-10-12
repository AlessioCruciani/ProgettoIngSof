# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaAggiungiFidelity.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

class Ui_AggiungiFidelity(object):
    def setupUi(self, AggiungiFidelity):
        AggiungiFidelity.setObjectName("AggiungiFidelity")
        AggiungiFidelity.resize(840, 571)
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        AggiungiFidelity.setFont(font)
        AggiungiFidelity.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiFidelity/SfondoAggiungiFidelity.png);")
        self.labelNome = QtWidgets.QLabel(AggiungiFidelity)
        self.labelNome.setGeometry(QtCore.QRect(60, 160, 220, 40))
        self.labelNome.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiFidelity/NomeFidelity.png);\n"
                                     "background-position: center;\n"
                                     "border-bottom: 2px solid black;\n"
                                     "border-radius: 20px;\n"
                                     "border-color: #20730b;")
        self.labelNome.setText("")
        self.labelNome.setObjectName("labelNome")
        self.lineEditNome = QtWidgets.QLineEdit(AggiungiFidelity)
        self.lineEditNome.setGeometry(QtCore.QRect(300, 160, 381, 40))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lineEditNome.setFont(font)
        self.lineEditNome.setStyleSheet("background-position: center;\n"
                                        "border: 2px solid black;\n"
                                        "border-radius: 10px;\n"
                                        "border-color: #20730b;\n"
                                        "padding-left: 10px;")
        self.lineEditNome.setObjectName("lineEditNome")
        self.labelCognome = QtWidgets.QLabel(AggiungiFidelity)
        self.labelCognome.setGeometry(QtCore.QRect(60, 220, 220, 40))
        self.labelCognome.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiFidelity/CognomeFidelity.png);\n"
                                        "background-position: center;\n"
                                        "border-bottom: 2px solid black;\n"
                                        "border-radius: 20px;\n"
                                        "border-color: #20730b;")
        self.labelCognome.setText("")
        self.labelCognome.setObjectName("labelCognome")
        self.LabelTelefono = QtWidgets.QLabel(AggiungiFidelity)
        self.LabelTelefono.setGeometry(QtCore.QRect(60, 340, 220, 40))
        self.LabelTelefono.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiFidelity/TelefonoFidelity.png);\n"
                                         "background-position: center;\n"
                                         "border-bottom: 2px solid black;\n"
                                         "border-radius: 20px;\n"
                                         "border-color: #20730b;")
        self.LabelTelefono.setText("")
        self.LabelTelefono.setObjectName("LabelTelefono")
        self.labelMail = QtWidgets.QLabel(AggiungiFidelity)
        self.labelMail.setGeometry(QtCore.QRect(60, 280, 220, 40))
        self.labelMail.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiFidelity/EmailFidelity.png);\n"
                                     "background-position: center;\n"
                                     "border-bottom: 2px solid black;\n"
                                     "border-radius: 20px;\n"
                                     "border-color: #20730b;")
        self.labelMail.setText("")
        self.labelMail.setObjectName("labelMail")
        self.lineEditEmail = QtWidgets.QLineEdit(AggiungiFidelity)
        self.lineEditEmail.setGeometry(QtCore.QRect(300, 280, 381, 40))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lineEditEmail.setFont(font)
        self.lineEditEmail.setStyleSheet("background-position: center;\n"
                                         "border: 2px solid black;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: #20730b;\n"
                                         "padding-left: 10px;")
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditCognome = QtWidgets.QLineEdit(AggiungiFidelity)
        self.lineEditCognome.setGeometry(QtCore.QRect(300, 220, 381, 40))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lineEditCognome.setFont(font)
        self.lineEditCognome.setStyleSheet("background-position: center;\n"
                                           "border: 2px solid black;\n"
                                           "border-radius: 10px;\n"
                                           "border-color: #20730b;\n"
                                           "padding-left: 10px;")
        self.lineEditCognome.setObjectName("lineEditCognome")
        self.lineEditTelefono = QtWidgets.QLineEdit(AggiungiFidelity)
        self.lineEditTelefono.setGeometry(QtCore.QRect(300, 340, 381, 40))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lineEditTelefono.setFont(font)
        self.lineEditTelefono.setStyleSheet("background-position: center;\n"
                                            "border: 2px solid black;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: #20730b;\n"
                                            "padding-left: 10px;")
        self.lineEditTelefono.setObjectName("lineEditTelefono")

        self.ButtonCreaFidelity = QtWidgets.QPushButton(AggiungiFidelity)
        self.ButtonCreaFidelity.setGeometry(QtCore.QRect(520, 500, 220, 40))
        self.ButtonCreaFidelity.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiFidelity/ButtonAggiungiFidelity.png);\n"
                                              "background-position: center;\n"
                                              "border: 2px solid black;\n"
                                              "border-radius: 10px;\n"
                                              "border-color: #20730b;")
        self.ButtonCreaFidelity.setText("")
        self.ButtonCreaFidelity.setObjectName("pushButton")

        self.retranslateUi(AggiungiFidelity)
        QtCore.QMetaObject.connectSlotsByName(AggiungiFidelity)

        self.identificatoreUtilizzatore = 0

        self.ButtonCreaFidelity.clicked.connect(self.creaNuovaFidelity)

    def retranslateUi(self, AggiungiFidelity):
        _translate = QtCore.QCoreApplication.translate
        AggiungiFidelity.setWindowTitle(_translate("AggiungiFidelity", "Form"))

    def setIdentificatoreUtilizzatore(self, codiceUtilizzatore):
        self.identificatoreUtilizzatore = codiceUtilizzatore

    def creaNuovaFidelity(self):
        nome = self.lineEditNome.text()
        cognome = self.lineEditCognome.text()
        email = self.lineEditEmail.text()
        telefono = self.lineEditTelefono.text()
        idutilizzatoreStr = str(self.identificatoreUtilizzatore)

        mydb = mysql.connector.connect(
            host="localhost",
            user="alessio",
            password="alessio",
            database="prova"
        )

        mycursor = mydb.cursor()
        try:
            queryAggiungiFidelity = "INSERT INTO fidelitycard VALUES ('', '" + nome + "','" + cognome + "','" + email + "','" + telefono + "', 0, " + idutilizzatoreStr + ")"
            mycursor.execute(queryAggiungiFidelity)

            mydb.commit()
            AggiungiFidelity.hide()
        except:
            pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AggiungiFidelity = QtWidgets.QWidget()
    ui = Ui_AggiungiFidelity()
    ui.setupUi(AggiungiFidelity)
    AggiungiFidelity.show()
    sys.exit(app.exec_())