# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaAggiungiScontrino.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import  mysql.connector
import datetime
from datetime import date


class Ui_PaginaAggiungiScontrini(object):
    def setupUi(self, PaginaAggiungiOrdini):
        PaginaAggiungiOrdini.setObjectName("PaginaAggiungiOrdini")
        PaginaAggiungiOrdini.resize(840, 571)
        PaginaAggiungiOrdini.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiScontrini/SfondoAggiungiScontrini.png);")
        self.TableProdottiScontrini = QtWidgets.QTableWidget(PaginaAggiungiOrdini)
        self.TableProdottiScontrini.setGeometry(QtCore.QRect(80, 220, 681, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableProdottiScontrini.sizePolicy().hasHeightForWidth())
        self.TableProdottiScontrini.setSizePolicy(sizePolicy)
        self.TableProdottiScontrini.setStyleSheet(
                                                  "background-color: rgb(122, 122, 122);\n"
                                                  "alternate-background-color: rgb(218, 218, 218);\n"
                                                  "background: none;\n"
                                                  "border: 2px solid white;\n"
                                                  "border-bottom-color: #20730b;\n"
                                                  "td: 100px;\n"
                                                  "\n"
                                                  "")
        self.TableProdottiScontrini.setObjectName("TableProdottiScontrini")
        self.TableProdottiScontrini.setColumnCount(5)
        self.TableProdottiScontrini.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiScontrini.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiScontrini.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiScontrini.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiScontrini.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiScontrini.setHorizontalHeaderItem(4, item)
        self.TableProdottiScontrini.horizontalHeader().setDefaultSectionSize(135)
        self.TableProdottiScontrini.horizontalHeader().setStretchLastSection(True)
        self.TableProdottiScontrini.verticalHeader().setCascadingSectionResizes(False)
        self.TableProdottiScontrini.verticalHeader().setStretchLastSection(False)
        self.ButtonAggiungiProdotto = QtWidgets.QPushButton(PaginaAggiungiOrdini)
        self.ButtonAggiungiProdotto.setGeometry(QtCore.QRect(600, 160, 220, 40))
        self.ButtonAggiungiProdotto.setStyleSheet("background-position: center;\n"
                                                  "background-image: url(ImmaginiProgetto/ImmaginiScontrini/ButtonAggiungiAlCarrello.png);\n"
                                                  "border: 2px solid black;\n"
                                                  "border-radius: 10px;\n"
                                                  "border-color: #20730b;")
        self.ButtonAggiungiProdotto.setText("")
        self.ButtonAggiungiProdotto.setObjectName("ButtonAggiungiProdotto")
        self.ButtonConfermaScontrino = QtWidgets.QPushButton(PaginaAggiungiOrdini)
        self.ButtonConfermaScontrino.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonConfermaScontrino.setStyleSheet("background-position: center;\n"
                                                   "background-image: url(ImmaginiProgetto/ImmaginiScontrini/ButtonConfermaScontrini.png);\n"
                                                   "border: 2px solid black;\n"
                                                   "border-radius: 10px;\n"
                                                   "border-color: #20730b;")
        self.ButtonConfermaScontrino.setText("")
        self.ButtonConfermaScontrino.setObjectName("ButtonConfermaScontrino")
        self.ButtonAnnullaScontrino = QtWidgets.QPushButton(PaginaAggiungiOrdini)
        self.ButtonAnnullaScontrino.setGeometry(QtCore.QRect(300, 500, 220, 40))
        self.ButtonAnnullaScontrino.setStyleSheet("background-position: center;\n"
                                                  "background-image: url(ImmaginiProgetto/ImmaginiScontrini/ButtonAnnullaScontrini.png);\n"
                                                  "border: 2px solid black;\n"
                                                  "border-radius: 10px;\n"
                                                  "border-color: #20730b;")
        self.ButtonAnnullaScontrino.setText("")
        self.ButtonAnnullaScontrino.setObjectName("ButtonAnnullaScontrino")
        self.lECodiceProdotto = QtWidgets.QLineEdit(PaginaAggiungiOrdini)
        self.lECodiceProdotto.setGeometry(QtCore.QRect(80, 160, 141, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lECodiceProdotto.setFont(font)
        self.lECodiceProdotto.setStyleSheet("background: none;\n"
                                            "border: 2px solid black;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: #20730b;\n"
                                            "text-align: center;")
        self.lECodiceProdotto.setAlignment(QtCore.Qt.AlignCenter)
        self.lECodiceProdotto.setObjectName("lECodiceProdotto")
        self.labelDNMscontrino = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelDNMscontrino.setGeometry(QtCore.QRect(60, 100, 361, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(13)
        self.labelDNMscontrino.setFont(font)
        self.labelDNMscontrino.setStyleSheet("background: transparent;\n"
                                             "color: #20730b;")
        self.labelDNMscontrino.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelDNMscontrino.setObjectName("labelDNMscontrino")
        self.labelCodiceOrdine = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelCodiceOrdine.setGeometry(QtCore.QRect(440, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.labelCodiceOrdine.setFont(font)
        self.labelCodiceOrdine.setStyleSheet("background: transparent;\n"
                                             "color: #20730b;")
        self.labelCodiceOrdine.setText("")
        self.labelCodiceOrdine.setObjectName("labelCodiceOrdine")
        self.labelCodiceProdotto = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelCodiceProdotto.setGeometry(QtCore.QRect(80, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.labelCodiceProdotto.setFont(font)
        self.labelCodiceProdotto.setStyleSheet("background: transparent;\n"
                                               "color: #20730b;")
        self.labelCodiceProdotto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCodiceProdotto.setObjectName("labelCodiceProdotto")
        self.lEQuantita = QtWidgets.QLineEdit(PaginaAggiungiOrdini)
        self.lEQuantita.setGeometry(QtCore.QRect(240, 160, 141, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lEQuantita.setFont(font)
        self.lEQuantita.setStyleSheet("background: none;\n"
                                      "border: 2px solid black;\n"
                                      "border-radius: 5px;\n"
                                      "border-color: #20730b;\n"
                                      "text-align: center;")
        self.lEQuantita.setAlignment(QtCore.Qt.AlignCenter)
        self.lEQuantita.setObjectName("lEQuantita")
        self.labelQuantita = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelQuantita.setGeometry(QtCore.QRect(240, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.labelQuantita.setFont(font)
        self.labelQuantita.setStyleSheet("background: transparent;\n"
                                         "color: #20730b;")
        self.labelQuantita.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuantita.setObjectName("labelQuantita")
        self.labelDNMtotale = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelDNMtotale.setGeometry(QtCore.QRect(300, 460, 361, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(13)
        self.labelDNMtotale.setFont(font)
        self.labelDNMtotale.setStyleSheet("background: transparent;\n"
                                          "color: #20730b;")
        self.labelDNMtotale.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelDNMtotale.setObjectName("labelDNMtotale")
        self.labelTotaleVendita = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelTotaleVendita.setGeometry(QtCore.QRect(680, 460, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.labelTotaleVendita.setFont(font)
        self.labelTotaleVendita.setStyleSheet("background: transparent;\n"
                                              "color: #20730b;")
        self.labelTotaleVendita.setText("")
        self.labelTotaleVendita.setObjectName("labelTotaleVendita")
        self.lECodiceFidelity = QtWidgets.QLineEdit(PaginaAggiungiOrdini)
        self.lECodiceFidelity.setGeometry(QtCore.QRect(400, 160, 141, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lECodiceFidelity.setFont(font)
        self.lECodiceFidelity.setStyleSheet("background: none;\n"
                                            "border: 2px solid black;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: #20730b;\n"
                                            "text-align: center;")
        self.lECodiceFidelity.setAlignment(QtCore.Qt.AlignCenter)
        self.lECodiceFidelity.setObjectName("lECodiceFidelity")
        self.labelQuantita_2 = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelQuantita_2.setGeometry(QtCore.QRect(400, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(11)
        self.labelQuantita_2.setFont(font)
        self.labelQuantita_2.setStyleSheet("background: transparent;\n"
                                           "color: #20730b;")
        self.labelQuantita_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuantita_2.setObjectName("labelQuantita_2")



        self.retranslateUi(PaginaAggiungiOrdini)
        QtCore.QMetaObject.connectSlotsByName(PaginaAggiungiOrdini)

    def retranslateUi(self, PaginaAggiungiOrdini):
        _translate = QtCore.QCoreApplication.translate
        PaginaAggiungiOrdini.setWindowTitle(_translate("PaginaAggiungiOrdini", "Form"))
        item = self.TableProdottiScontrini.horizontalHeaderItem(0)
        item.setText(_translate("PaginaAggiungiOrdini", "Numero Scontrino"))
        item = self.TableProdottiScontrini.horizontalHeaderItem(1)
        item.setText(_translate("PaginaAggiungiOrdini", "Codice Prodotto"))
        item = self.TableProdottiScontrini.horizontalHeaderItem(2)
        item.setText(_translate("PaginaAggiungiOrdini", "Nome Prodotto"))
        item = self.TableProdottiScontrini.horizontalHeaderItem(3)
        item.setText(_translate("PaginaAggiungiOrdini", "Prezzo Vendita"))
        item = self.TableProdottiScontrini.horizontalHeaderItem(4)
        item.setText(_translate("PaginaAggiungiOrdini", "Quantità"))
        self.labelDNMscontrino.setText(
            _translate("PaginaAggiungiOrdini", "Inserendo prodotti nello scontrino numero: "))
        self.labelCodiceProdotto.setText(_translate("PaginaAggiungiOrdini", "CODICE PRODOTTO"))
        self.labelQuantita.setText(_translate("PaginaAggiungiOrdini", "QUANTITA\'"))
        self.labelDNMtotale.setText(_translate("PaginaAggiungiOrdini", "Totale Scontrino: "))
        self.labelQuantita_2.setText(_translate("PaginaAggiungiOrdini", "CODICE FIDELITY"))

        self.identificatoreUtilizzatore = 0

        self.ButtonAggiungiProdotto.clicked.connect(self.aggiungiProdottoDaVendere)

        self.TableProdottiScontrini.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def setIdentificatoreUtilizzatore(self, codiceUtilizzatore):
        self.identificatoreUtilizzatore = codiceUtilizzatore

    def creaNuovoScontrino(self):

        mydb = mysql.connector.connect(host="localhost",user="alessio",password="alessio",database="prova")
        mycursor = mydb.cursor()

        dataOdierna = date.today()
        dataOdierna = str(dataOdierna)

        orarioAttuale = time.strftime('%H:%M:%S', time.localtime())

        idUtilizzatoreStr = str(self.identificatoreUtilizzatore)

        queryNuovoScontrino = "INSERT INTO vendita VALUES('', '" + dataOdierna + "','" + orarioAttuale + "', " + idUtilizzatoreStr + ")"
        mycursor.execute(queryNuovoScontrino)

        mydb.commit()

        queryUltimoCodiceScontrino = "SELECT MAX(vendita.IDVendita) FROM vendita"
        mycursor.execute(queryUltimoCodiceScontrino)
        myresult = mycursor.fetchone()

        maxIdOrdine = 0

        for x in myresult:
            maxIdOrdine = x

        self.labelCodiceOrdine.setText(str(maxIdOrdine))


    def aggiungiProdottoDaVendere(self):
        mydb = mysql.connector.connect(host="localhost",user="alessio",password="alessio",database="prova")
        mycursor = mydb.cursor()

        codiceProdotto = self.lECodiceProdotto.text()
        quantita = self.lEQuantita.text()

        queryControllaQuantita = "SELECT SUM(prodottoacquistato.QuantitaAcquistata) FROM ordine INNER JOIN (prodotto INNER JOIN prodottoacquistato ON prodotto.IDProdotto = prodottoacquistato.IDProdotto) ON ordine.IDOrdine = prodottoacquistato.IDOrdine WHERE (ordine.Consegnato = 'true' AND prodotto.IDProdotto = '" + codiceProdotto + "')"
        mycursor.execute(queryControllaQuantita)
        myresult = mycursor.fetchall()

        quantitaAcquistata = 0
        for row in myresult:
            quantitaAcquistata = row[0]

        queryQuantitaVenduta = "SELECT SUM(prodottovenduto.QuantitaVenduta) FROM prodottovenduto WHERE prodottovenduto.IDProdotto = '" + codiceProdotto + "'"
        mycursor.execute(queryQuantitaVenduta)
        risultatoQueryQuantitaVenduta = mycursor.fetchall()

        quantitaVenduta = 0

        for riga in risultatoQueryQuantitaVenduta:
            quantitaVenduta = riga[0]

        if (quantitaVenduta != None):
            quantitaResidua = int(quantitaAcquistata) - int(quantitaVenduta)
        else:
            quantitaResidua = int(quantitaAcquistata)


        if int(quantitaResidua) >= int(quantita):
            self.aggiungiProdottoInScontrino(quantita,codiceProdotto)
            self.aggiornaDataUltimaVendita(codiceProdotto)

    def aggiungiProdottoInScontrino(self, quantitaVenduta, codiceProdotto):

        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codiceScontrino = str(self.labelCodiceOrdine.text())

        queryPrezzoVendita = "SELECT prodotto.PrezzoVendita FROM prodotto WHERE prodotto.IDProdotto = '" + codiceProdotto + "'"
        mycursor.execute(queryPrezzoVendita)
        myresult = mycursor.fetchall()

        prezzoVendita = 0

        for row in myresult:
            prezzoVendita = row[0]

        totaleVendita = float(prezzoVendita) * int(quantitaVenduta)

        queryAggiungiVendita = "INSERT INTO prodottovenduto VALUES( " + codiceScontrino + ", " + codiceProdotto + ", " + str(quantitaVenduta) + ", " + str(totaleVendita) + ")"
        mycursor.execute(queryAggiungiVendita)
        mydb.commit()

        self.caricaDatiProdotto(codiceScontrino)

    def caricaDatiProdotto(self, codiceScontrino):
        mydb = mysql.connector.connect(host="localhost",user="alessio",password="alessio",database="prova")
        mycursor = mydb.cursor()

        queryCaricaDati = "SELECT DISTINCT prodottovenduto.IDVendita, prodotto.IDProdotto, prodotto.NomeProdotto, prodotto.PrezzoVendita, prodottovenduto.QuantitaVenduta FROM prodottovenduto INNER JOIN prodotto ON prodottovenduto.IDProdotto = prodotto.IDProdotto WHERE prodottovenduto.IDVendita = " + codiceScontrino
        mycursor.execute(queryCaricaDati)
        risultatoQueryCaricaDati = mycursor.fetchall()
        rigaTabella = 0
        righeTotali = 0

        for row in risultatoQueryCaricaDati:
            righeTotali += 1

        self.TableProdottiScontrini.setRowCount(righeTotali)

        for row in risultatoQueryCaricaDati:
            self.TableProdottiScontrini.verticalHeader().setVisible(bool(0))
            self.TableProdottiScontrini.setItem(rigaTabella, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.TableProdottiScontrini.setItem(rigaTabella, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.TableProdottiScontrini.setItem(rigaTabella, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TableProdottiScontrini.setItem(rigaTabella, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.TableProdottiScontrini.setItem(rigaTabella, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            rigaTabella += 1

        queryTotaleVendita = "SELECT SUM(prodottovenduto.TotaleVendita) FROM prodottovenduto INNER JOIN prodotto ON prodottovenduto.IDProdotto = prodotto.IDProdotto WHERE prodottovenduto.IDVendita = " + codiceScontrino
        mycursor.execute(queryTotaleVendita)
        risultatoQueryTotaleVendita = mycursor.fetchall()

        totaleVendita = 0
        for row in risultatoQueryTotaleVendita:
            totaleVendita = row[0]

        self.labelTotaleVendita.setText(str(totaleVendita))

    def aggiornaDataUltimaVendita(self, codiceProdotto):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()
        dataOdierna = str(date.today())
        queryAggiornaDataUltimaVendita = "UPDATE prodotto SET prodotto.DataUltimaVendita = '"+ dataOdierna +"' WHERE prodotto.IDProdotto = '"+  codiceProdotto+ "'"
        mycursor.execute(queryAggiornaDataUltimaVendita)
        mydb.commit()

    def annullaScontrino(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codiceScontrino = str(self.labelCodiceOrdine.text())
        queryRimuoviProdottiScontrino = "DELETE FROM prodottovenduto WHERE prodottovenduto.IDVendita = " + codiceScontrino
        mycursor.execute(queryRimuoviProdottiScontrino)
        mydb.commit()

        queryRimuoviScontrino = "DELETE FROM vendita WHERE vendita.IDVendita = " + codiceScontrino
        mycursor.execute(queryRimuoviScontrino)
        mydb.commit()

        self.cancellaDatiPrecendeti()

    def confermaScontrino(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        if self.lECodiceFidelity.text() != '':
            querySaldoCashback = "SELECT fidelitycard.SaldoCashback FROM fidelitycard WHERE fidelitycard.IDFidelityCard = '" + self.lECodiceFidelity.text() + "'"
            mycursor.execute(querySaldoCashback)
            risultatoQuerySaldoCashback = mycursor.fetchall()

            saldoPrecedente = 0

            for row in risultatoQuerySaldoCashback:
                saldoPrecedente = row[0]

            caskBack = saldoPrecedente + (float(self.labelTotaleVendita.text()) * 5)/100

            queryAggiornaSaldoCashback = "UPDATE fidelitycard SET fidelitycard.SaldoCashback = '" + str(caskBack) + "' WHERE fidelitycard.IDFidelityCard = '" + self.lECodiceFidelity.text() + "'"
            mycursor.execute(queryAggiornaSaldoCashback)
            mydb.commit()

        self.cancellaDatiPrecendeti()

    def cancellaDatiPrecendeti(self):
        self.lEQuantita.setText('')
        self.lECodiceProdotto.setText('')
        self.lECodiceFidelity.setText('')

        righeTabella = self.TableProdottiScontrini.rowCount()
        x = 0
        for x in range(righeTabella):
            self.TableProdottiScontrini.removeRow(x)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaAggiungiOrdini = QtWidgets.QWidget()
    ui = Ui_PaginaAggiungiScontrini()
    ui.setupUi(PaginaAggiungiOrdini)
    PaginaAggiungiOrdini.show()
    sys.exit(app.exec_())
