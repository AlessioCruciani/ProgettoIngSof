from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_PaginaRimuoviPrenotazione(object):
    def setupUi(self, PaginaRimuoviDipendenti):
        PaginaRimuoviDipendenti.setObjectName("PaginaRimuoviDipendenti")
        PaginaRimuoviDipendenti.resize(840, 571)
        PaginaRimuoviDipendenti.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/SfondoRimuoviPrenotazione.png);")
        self.ButtonConferma = QtWidgets.QPushButton(PaginaRimuoviDipendenti)
        self.ButtonConferma.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonConferma.setStyleSheet("background-position: center;\n"
                                                        "background-image: url(ImmaginiProgetto/ImmaginiPersonale/ButtonConfermaModifica.png);\n"
                                                        "border: 2px solid black;\n"
                                                        "border-radius: 10px;\n"
                                                        "border-color: #20730b;")
        self.ButtonConferma.setText("")
        self.ButtonConferma.setObjectName("ButtonConfermaModificaOrdine")
        self.ButtonAnnulla = QtWidgets.QPushButton(PaginaRimuoviDipendenti)
        self.ButtonAnnulla.setGeometry(QtCore.QRect(300, 500, 220, 40))
        self.ButtonAnnulla.setStyleSheet("background-position: center;\n"
                                                          "background-image: url(ImmaginiProgetto/ImmaginiPersonale/ButtonAnnullaModifica.png);\n"
                                                          "border: 2px solid black;\n"
                                                          "border-radius: 10px;\n"
                                                          "border-color: #20730b;")
        self.ButtonAnnulla.setText("")
        self.ButtonAnnulla.setObjectName("ButtonAnnullaModificaPersonale")
        self.lECodicePrenotazione = QtWidgets.QLineEdit(PaginaRimuoviDipendenti)
        self.lECodicePrenotazione.setGeometry(QtCore.QRect(140, 180, 581, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lECodicePrenotazione.setFont(font)
        self.lECodicePrenotazione.setStyleSheet("background: none;\n"
                                             "border: 2px solid black;\n"
                                             "border-radius: 5px;\n"
                                             "border-color: #20730b;\n"
                                             "text-align: center;")
        self.lECodicePrenotazione.setAlignment(QtCore.Qt.AlignCenter)
        self.lECodicePrenotazione.setObjectName("lECodicePersonale")
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
        self.labelDNM.setText(_translate("PaginaRimuoviDipendenti", "INSERISCI IL CODICE DELLA PRENOTAZIONE DA RIMUOVERE:"))

    def controllaCodicePrenotazione(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codicePrenotazione = self.lECodicePrenotazione.text()

        queryRicercaPrenotazione = "SELECT prenotazioni.IDPrenotazioni FROM prenotazioni WHERE prenotazioni.IDPrenotazioni = '" + str(codicePrenotazione) + "'"
        mycursor.execute(queryRicercaPrenotazione)
        risultatoRicercaPrenotazione = mycursor.fetchall()

        codicePrenotazioneEsistente = None

        for row in risultatoRicercaPrenotazione:
            codicePrenotazioneEsistente = row[0]

        if codicePrenotazioneEsistente != None:
            return 1
        else:
            return 0

    def rimuoviPrenotazione(self):
        codicePrenotazione = self.lECodicePrenotazione.text()
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        queryRimuoviPrenotazione = "DELETE FROM prenotazioni WHERE prenotazioni.IDPrenotazioni = '" + codicePrenotazione + "'"
        mycursor.execute(queryRimuoviPrenotazione)
        mydb.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaRimuoviDipendenti = QtWidgets.QWidget()
    ui = Ui_PaginaRimuoviPrenotazione()
    ui.setupUi(PaginaRimuoviDipendenti)
    PaginaRimuoviDipendenti.show()
    sys.exit(app.exec_())