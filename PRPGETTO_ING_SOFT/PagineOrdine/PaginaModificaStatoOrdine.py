# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaModificaStatoOrdine.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import datetime
from datetime import date

class Ui_PaginaModificaStatoOrdini(object):
    def setupUi(self, PaginaModificaStatoOrdini):
        PaginaModificaStatoOrdini.setObjectName("PaginaModificaStatoOrdini")
        PaginaModificaStatoOrdini.resize(840, 571)
        PaginaModificaStatoOrdini.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiOrdini/SfondoModificaStatoOrdine.png);")
        self.ButtonConfermaModificaOrdine = QtWidgets.QPushButton(PaginaModificaStatoOrdini)
        self.ButtonConfermaModificaOrdine.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonConfermaModificaOrdine.setStyleSheet("background-position: center;\n"
                                                        "background-image: url(ImmaginiProgetto/ImmaginiOrdini/ButtonConfermaModifica.png);\n"
                                                        "border: 2px solid black;\n"
                                                        "border-radius: 10px;\n"
                                                        "border-color: #20730b;")
        self.ButtonConfermaModificaOrdine.setText("")
        self.ButtonConfermaModificaOrdine.setObjectName("ButtonConfermaModificaOrdine")
        self.ButtonAnnullaModificaOrdine = QtWidgets.QPushButton(PaginaModificaStatoOrdini)
        self.ButtonAnnullaModificaOrdine.setGeometry(QtCore.QRect(300, 500, 220, 40))
        self.ButtonAnnullaModificaOrdine.setStyleSheet("background-position: center;\n"
                                                       "background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiOrdini/ButtonAnnullaModifica.png);\n"
                                                       "border: 2px solid black;\n"
                                                       "border-radius: 10px;\n"
                                                       "border-color: #20730b;")
        self.ButtonAnnullaModificaOrdine.setText("")
        self.ButtonAnnullaModificaOrdine.setObjectName("ButtonAnnullaModificaOrdine")
        self.lECodiceOrdine = QtWidgets.QLineEdit(PaginaModificaStatoOrdini)
        self.lECodiceOrdine.setGeometry(QtCore.QRect(140, 180, 581, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lECodiceOrdine.setFont(font)
        self.lECodiceOrdine.setStyleSheet("background: none;\n"
                                          "border: 2px solid black;\n"
                                          "border-radius: 5px;\n"
                                          "border-color: #20730b;\n"
                                          "text-align: center;")
        self.lECodiceOrdine.setAlignment(QtCore.Qt.AlignCenter)
        self.lECodiceOrdine.setObjectName("lECodiceOrdine")
        self.labelDNM = QtWidgets.QLabel(PaginaModificaStatoOrdini)
        self.labelDNM.setGeometry(QtCore.QRect(140, 160, 581, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.labelDNM.setFont(font)
        self.labelDNM.setStyleSheet("background: transparent;\n"
                                    "color: #20730b;")
        self.labelDNM.setObjectName("labelDNM")

        self.retranslateUi(PaginaModificaStatoOrdini)
        QtCore.QMetaObject.connectSlotsByName(PaginaModificaStatoOrdini)

    def retranslateUi(self, PaginaModificaStatoOrdini):
        _translate = QtCore.QCoreApplication.translate
        PaginaModificaStatoOrdini.setWindowTitle(_translate("PaginaModificaStatoOrdini", "Form"))
        self.labelDNM.setText(_translate("PaginaModificaStatoOrdini", "INSERISCI IL CODICE DELL\'ORDINE DI CUI MODIFICARE LO STATO:"))

    def controllaCodiceOrdine(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codiceOrdine = self.lECodiceOrdine.text()

        queryRicercaOrdine = "SELECT ordine.IDOrdine FROM ordine WHERE ordine.IDOrdine = '" + str(codiceOrdine) + "'"
        mycursor.execute(queryRicercaOrdine)
        risultatoRicercaOrdine = mycursor.fetchall()

        codiceOrdineEsistente = None

        for row in risultatoRicercaOrdine:
            codiceOrdineEsistente = row[0]

        if codiceOrdineEsistente != None:
            return 1
        else:
            return 0

    def modificaStatoOrdine(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codiceOrdine = self.lECodiceOrdine.text()

        queryModificaStatoOrdine = "UPDATE ordine SET ordine.Consegnato = 'true', ordine.DataConsegna = '" + str(date.today()) +  "' WHERE ordine.IDOrdine = " + codiceOrdine
        mycursor.execute(queryModificaStatoOrdine)
        mydb.commit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaModificaStatoOrdini = QtWidgets.QWidget()
    ui = Ui_PaginaModificaStatoOrdini()
    ui.setupUi(PaginaModificaStatoOrdini)
    PaginaModificaStatoOrdini.show()
    sys.exit(app.exec_())
