# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaModificaPermessi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_PaginaModificaPermessi(object):
    def setupUi(self, PaginaModificaPermessi):
        PaginaModificaPermessi.setObjectName("PaginaModificaStatoOrdini")
        PaginaModificaPermessi.resize(840, 571)
        self.FrameSfondo = QtWidgets.QFrame(PaginaModificaPermessi)
        self.FrameSfondo.resize(840,571)
        self.FrameSfondo.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPersonale/SfondoModificaPermessi.png);")
        self.ButtonConfermaModifica = QtWidgets.QPushButton(PaginaModificaPermessi)
        self.ButtonConfermaModifica.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonConfermaModifica.setStyleSheet("background-position: center;\n"
                                                  "background-image: url(ImmaginiProgetto/ImmaginiPersonale/ButtonConfermaModifica.png);\n"
                                                  "border: 2px solid black;\n"
                                                  "border-radius: 10px;\n"
                                                  "border-color: #20730b;")
        self.ButtonConfermaModifica.setText("")
        self.ButtonConfermaModifica.setObjectName("ButtonConfermaModificaOrdine")
        self.ButtonAnnullaModifica = QtWidgets.QPushButton(PaginaModificaPermessi)
        self.ButtonAnnullaModifica.setGeometry(QtCore.QRect(300, 500, 220, 40))
        self.ButtonAnnullaModifica.setStyleSheet("background-position: center;\n"
                                                 "background-image: url(ImmaginiProgetto/ImmaginiPersonale/ButtonAnnullaModifica.png);\n"
                                                 "border: 2px solid black;\n"
                                                 "border-radius: 10px;\n"
                                                 "border-color: #20730b;")
        self.ButtonAnnullaModifica.setText("")
        self.ButtonAnnullaModifica.setObjectName("ButtonAnnullaModificaOrdine")
        self.lEImportoStipendio = QtWidgets.QLineEdit(PaginaModificaPermessi)
        self.lEImportoStipendio.setGeometry(QtCore.QRect(140, 340, 581, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lEImportoStipendio.setFont(font)
        self.lEImportoStipendio.setStyleSheet("background: none;\n"
                                              "border: 2px solid black;\n"
                                              "border-radius: 5px;\n"
                                              "border-color: #20730b;\n"
                                              "text-align: center;")
        self.lEImportoStipendio.setAlignment(QtCore.Qt.AlignCenter)
        self.lEImportoStipendio.setObjectName("lEImportoStipendio")
        self.labelDNMpermessi = QtWidgets.QLabel(PaginaModificaPermessi)
        self.labelDNMpermessi.setGeometry(QtCore.QRect(140, 240, 581, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.labelDNMpermessi.setFont(font)
        self.labelDNMpermessi.setStyleSheet("background: transparent;\n"
                                            "color: #20730b;")
        self.labelDNMpermessi.setObjectName("labelDNMpermessi")
        self.comboBoxPernessi = QtWidgets.QComboBox(PaginaModificaPermessi)
        self.comboBoxPernessi.setGeometry(QtCore.QRect(140, 260, 581, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.comboBoxPernessi.setFont(font)
        self.comboBoxPernessi.setStyleSheet("background: white;\n"
                                            "backface-visibility: hidden;\n"
                                            "border: 2px solid black;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: #20730b;\n"
                                            "text-align: center;")
        self.comboBoxPernessi.setObjectName("comboBoxPernessi")
        self.labelDNMstipendio = QtWidgets.QLabel(PaginaModificaPermessi)
        self.labelDNMstipendio.setGeometry(QtCore.QRect(140, 320, 581, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.labelDNMstipendio.setFont(font)
        self.labelDNMstipendio.setStyleSheet("background: transparent;\n"
                                             "color: #20730b;")
        self.labelDNMstipendio.setObjectName("labelDNMstipendio")
        self.lECodiceDipendente = QtWidgets.QLineEdit(PaginaModificaPermessi)
        self.lECodiceDipendente.setGeometry(QtCore.QRect(140, 180, 581, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lECodiceDipendente.setFont(font)
        self.lECodiceDipendente.setStyleSheet("background: none;\n"
                                              "border: 2px solid black;\n"
                                              "border-radius: 5px;\n"
                                              "border-color: #20730b;\n"
                                              "text-align: center;")
        self.lECodiceDipendente.setAlignment(QtCore.Qt.AlignCenter)
        self.lECodiceDipendente.setObjectName("lECodiceDipendente")
        self.labelDNMcodiceDip = QtWidgets.QLabel(PaginaModificaPermessi)
        self.labelDNMcodiceDip.setGeometry(QtCore.QRect(140, 160, 581, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.labelDNMcodiceDip.setFont(font)
        self.labelDNMcodiceDip.setStyleSheet("background: transparent;\n"
                                             "color: #20730b;")
        self.labelDNMcodiceDip.setObjectName("labelDNMcodiceDip")

        #self.ButtonConfermaModifica.clicked.connect(self.aggiornaPermessiDipendenti)
        self.comboBoxPernessi.addItems(['low', 'medium', 'high'])

        self.retranslateUi(PaginaModificaPermessi)
        QtCore.QMetaObject.connectSlotsByName(PaginaModificaPermessi)

    def retranslateUi(self, PaginaModificaPermessi):
        _translate = QtCore.QCoreApplication.translate
        PaginaModificaPermessi.setWindowTitle(_translate("PaginaModificaStatoOrdini", "Form"))
        self.labelDNMpermessi.setText(_translate("PaginaModificaStatoOrdini", "INSERISCI IL LIVELLO DI PERMESSI DA ASSEGNARE:"))
        self.labelDNMstipendio.setText(_translate("PaginaModificaStatoOrdini", "INSERISCI L\'IMPORTO DELLO STIPENDIO DA ATTRIBUIRE AL DIPENDENTE:"))
        self.labelDNMcodiceDip.setText(_translate("PaginaModificaStatoOrdini", "INSERISCI IL CODICE DEL DIPENDENTE DA PROMUOVERE:"))

    def controllaCodicePersonale(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codicePersonale = self.lECodiceDipendente.text()

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

    def aggiornaPermessiDipendenti(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codicePersonale = self.lECodiceDipendente.text()
        livelloPermessi = self.comboBoxPernessi.currentText()
        importoStipendi = self.lEImportoStipendio.text()

        queryAggiornaPermessi = "UPDATE utilizzatore SET utilizzatore.Permessi = '"+livelloPermessi+"', utilizzatore.Stipendio = '"+importoStipendi+"' WHERE utilizzatore.IDUtilizzatore = '"+codicePersonale+"'"
        mycursor.execute(queryAggiornaPermessi)
        mydb.commit()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaModificaPermessi = QtWidgets.QWidget()
    ui = Ui_PaginaModificaPermessi()
    ui.setupUi(PaginaModificaPermessi)
    PaginaModificaPermessi.show()
    sys.exit(app.exec_())
