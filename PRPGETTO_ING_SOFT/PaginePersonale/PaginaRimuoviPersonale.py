# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaRimuoviPersonale.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_PaginaRimuoviDipendenti(object):
    def setupUi(self, PaginaRimuoviDipendenti):
        PaginaRimuoviDipendenti.setObjectName("PaginaRimuoviDipendenti")
        PaginaRimuoviDipendenti.resize(840, 571)
        PaginaRimuoviDipendenti.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPersonale/SfondoRimuoviPersonale.png);")
        self.ButtonConfermaModificaOrdine = QtWidgets.QPushButton(PaginaRimuoviDipendenti)
        self.ButtonConfermaModificaOrdine.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonConfermaModificaOrdine.setStyleSheet("background-position: center;\n"
                                                        "background-image: url(ImmaginiProgetto/ImmaginiPersonale/ButtonConfermaModifica.png);\n"
                                                        "border: 2px solid black;\n"
                                                        "border-radius: 10px;\n"
                                                        "border-color: #20730b;")
        self.ButtonConfermaModificaOrdine.setText("")
        self.ButtonConfermaModificaOrdine.setObjectName("ButtonConfermaModificaOrdine")
        self.ButtonAnnullaModificaPersonale = QtWidgets.QPushButton(PaginaRimuoviDipendenti)
        self.ButtonAnnullaModificaPersonale.setGeometry(QtCore.QRect(300, 500, 220, 40))
        self.ButtonAnnullaModificaPersonale.setStyleSheet("background-position: center;\n"
                                                          "background-image: url(ImmaginiProgetto/ImmaginiPersonale/ButtonAnnullaModifica.png);\n"
                                                          "border: 2px solid black;\n"
                                                          "border-radius: 10px;\n"
                                                          "border-color: #20730b;")
        self.ButtonAnnullaModificaPersonale.setText("")
        self.ButtonAnnullaModificaPersonale.setObjectName("ButtonAnnullaModificaPersonale")
        self.lECodicePersonale = QtWidgets.QLineEdit(PaginaRimuoviDipendenti)
        self.lECodicePersonale.setGeometry(QtCore.QRect(140, 180, 581, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lECodicePersonale.setFont(font)
        self.lECodicePersonale.setStyleSheet("background: none;\n"
                                             "border: 2px solid black;\n"
                                             "border-radius: 5px;\n"
                                             "border-color: #20730b;\n"
                                             "text-align: center;")
        self.lECodicePersonale.setAlignment(QtCore.Qt.AlignCenter)
        self.lECodicePersonale.setObjectName("lECodicePersonale")
        self.labelDNM = QtWidgets.QLabel(PaginaRimuoviDipendenti)
        self.labelDNM.setGeometry(QtCore.QRect(140, 160, 581, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.labelDNM.setFont(font)
        self.labelDNM.setStyleSheet("background: transparent;\n"
                                    "color: #20730b;")
        self.labelDNM.setObjectName("labelDNM")

        self.retranslateUi(PaginaRimuoviDipendenti)
        QtCore.QMetaObject.connectSlotsByName(PaginaRimuoviDipendenti)

    def retranslateUi(self, PaginaRimuoviDipendenti):
        _translate = QtCore.QCoreApplication.translate
        PaginaRimuoviDipendenti.setWindowTitle(_translate("PaginaRimuoviDipendenti", "Form"))
        self.labelDNM.setText(_translate("PaginaRimuoviDipendenti", "INSERISCI IL CODICE DEL DIPENDENTE  DA RIMUOVERE:"))

    def controllaCodicePersonale(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codicePersonale = self.lECodicePersonale.text()

        queryRicercaPersonale = "SELECT utilizzatore.IDUtilizzatore FROM utilizzatore WHERE utilizzatore.IDUtilizzatore = '" + str(codicePersonale) + "'"
        mycursor.execute(queryRicercaPersonale)
        risultatoRicercaPersonale = mycursor.fetchall()

        codicePersonaleEsistente = None

        for row in risultatoRicercaPersonale:
            codicePersonaleEsistente = row[0]

        if codicePersonaleEsistente != None:
            return 1
        else:
            return 0

    def rimuoviPersonale(self):
        codicePersonale = self.lECodicePersonale.text()
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        queryRimuoviPersonale = "UPDATE utilizzatore SET utilizzatore.Impiegato = 'false' WHERE utilizzatore.IDUtilizzatore = '" + codicePersonale + "'"
        mycursor.execute(queryRimuoviPersonale)
        mydb.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaRimuoviDipendenti = QtWidgets.QWidget()
    ui = Ui_PaginaRimuoviDipendenti()
    ui.setupUi(PaginaRimuoviDipendenti)
    PaginaRimuoviDipendenti.show()
    sys.exit(app.exec_())
