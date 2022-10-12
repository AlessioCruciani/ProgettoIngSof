# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaAggiungiOrdine.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
import  mysql.connector
from datetime import date

class Ui_PaginaAggiungiOrdini(object):
    def setupUi(self, PaginaAggiungiOrdini):
        PaginaAggiungiOrdini.setObjectName("PaginaAggiungiOrdini")
        PaginaAggiungiOrdini.resize(840, 571)
        PaginaAggiungiOrdini.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiOrdini/SfondoAggiungiOrdine.png);")
        self.TableProdottiOrdine = QtWidgets.QTableWidget(PaginaAggiungiOrdini)
        self.TableProdottiOrdine.setGeometry(QtCore.QRect(80, 240, 681, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableProdottiOrdine.sizePolicy().hasHeightForWidth())
        self.TableProdottiOrdine.setSizePolicy(sizePolicy)
        self.TableProdottiOrdine.setStyleSheet(
            "background-color: rgb(122, 122, 122);\n"
            "alternate-background-color: rgb(218, 218, 218);\n"
            "background: none;\n"
            "border: 2px solid white;\n"
            "border-bottom-color: #20730b;\n"
            "td: 100px;\n"
            "\n"
            "")
        self.TableProdottiOrdine.setObjectName("TableProdottiOrdine")
        self.TableProdottiOrdine.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiOrdine.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiOrdine.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiOrdine.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiOrdine.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProdottiOrdine.setHorizontalHeaderItem(4, item)
        self.TableProdottiOrdine.horizontalHeader().setDefaultSectionSize(128)
        self.TableProdottiOrdine.horizontalHeader().setStretchLastSection(True)
        self.TableProdottiOrdine.verticalHeader().setCascadingSectionResizes(False)
        self.TableProdottiOrdine.verticalHeader().setStretchLastSection(False)
        self.ButtonAggiungiProdotto = QtWidgets.QPushButton(PaginaAggiungiOrdini)
        self.ButtonAggiungiProdotto.setGeometry(QtCore.QRect(600, 160, 220, 40))
        self.ButtonAggiungiProdotto.setStyleSheet("background-position: center;\n"
                                                  "background-image: url(ImmaginiProgetto/ImmaginiOrdini/ButtonAggiungiAlCarrello.png);\n"
                                                  "border: 2px solid black;\n"
                                                  "border-radius: 10px;\n"
                                                  "border-color: #20730b;")
        self.ButtonAggiungiProdotto.setText("")
        self.ButtonAggiungiProdotto.setObjectName("ButtonAggiungiProdotto")
        self.ButtonConfermaOrdine = QtWidgets.QPushButton(PaginaAggiungiOrdini)
        self.ButtonConfermaOrdine.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonConfermaOrdine.setStyleSheet("background-position: center;\n"
                                                "background-image: url(ImmaginiProgetto/ImmaginiOrdini/ButtonConfermaOrdine.png);\n"
                                                "border: 2px solid black;\n"
                                                "border-radius: 10px;\n"
                                                "border-color: #20730b;")
        self.ButtonConfermaOrdine.setText("")
        self.ButtonConfermaOrdine.setObjectName("ButtonConfermaOrdine")
        self.ButtonAnnullaOrdine = QtWidgets.QPushButton(PaginaAggiungiOrdini)
        self.ButtonAnnullaOrdine.setGeometry(QtCore.QRect(300, 500, 220, 40))
        self.ButtonAnnullaOrdine.setStyleSheet("background-position: center;\n"
                                               "background-image: url(ImmaginiProgetto/ImmaginiOrdini/ButtonAnnullaOrdine.png);\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 10px;\n"
                                               "border-color: #20730b;")
        self.ButtonAnnullaOrdine.setText("")
        self.ButtonAnnullaOrdine.setObjectName("ButtonAnnullaOrdine")
        self.lECodiceProdotto = QtWidgets.QLineEdit(PaginaAggiungiOrdini)
        self.lECodiceProdotto.setGeometry(QtCore.QRect(20, 160, 121, 41))
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
        self.labelDNM = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelDNM.setGeometry(QtCore.QRect(20, 100, 361, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.labelDNM.setFont(font)
        self.labelDNM.setStyleSheet("background: transparent;\n"
                                    "color: #20730b;")
        self.labelDNM.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDNM.setObjectName("labelDNM")
        self.labelCodiceOrdine = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelCodiceOrdine.setGeometry(QtCore.QRect(380, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.labelCodiceOrdine.setFont(font)
        self.labelCodiceOrdine.setStyleSheet("background: transparent;\n"
                                             "color: #20730b;")
        self.labelCodiceOrdine.setText("")
        self.labelCodiceOrdine.setObjectName("labelCodiceOrdine")
        self.labelCodiceProdotto = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelCodiceProdotto.setGeometry(QtCore.QRect(20, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.labelCodiceProdotto.setFont(font)
        self.labelCodiceProdotto.setStyleSheet("background: transparent;\n"
                                               "color: #20730b;")
        self.labelCodiceProdotto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCodiceProdotto.setObjectName("labelCodiceProdotto")
        self.labelNomeProdotto = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelNomeProdotto.setGeometry(QtCore.QRect(160, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.labelNomeProdotto.setFont(font)
        self.labelNomeProdotto.setStyleSheet("background: transparent;\n"
                                             "color: #20730b;")
        self.labelNomeProdotto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNomeProdotto.setObjectName("labelNomeProdotto")
        self.labelPrezzoAcquisto = QtWidgets.QLabel(PaginaAggiungiOrdini)
        self.labelPrezzoAcquisto.setGeometry(QtCore.QRect(300, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.labelPrezzoAcquisto.setFont(font)
        self.labelPrezzoAcquisto.setStyleSheet("background: transparent;\n"
                                               "color: #20730b;")
        self.labelPrezzoAcquisto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPrezzoAcquisto.setObjectName("labelPrezzoAcquisto")
        self.lENomeProdotto = QtWidgets.QLineEdit(PaginaAggiungiOrdini)
        self.lENomeProdotto.setGeometry(QtCore.QRect(160, 160, 121, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lENomeProdotto.setFont(font)
        self.lENomeProdotto.setStyleSheet("background: none;\n"
                                          "border: 2px solid black;\n"
                                          "border-radius: 5px;\n"
                                          "border-color: #20730b;\n"
                                          "text-align: center;")
        self.lENomeProdotto.setAlignment(QtCore.Qt.AlignCenter)
        self.lENomeProdotto.setObjectName("lENomeProdotto")
        self.lEPrezzoAcquisto = QtWidgets.QLineEdit(PaginaAggiungiOrdini)
        self.lEPrezzoAcquisto.setGeometry(QtCore.QRect(300, 160, 121, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lEPrezzoAcquisto.setFont(font)
        self.lEPrezzoAcquisto.setStyleSheet("background: none;\n"
                                            "border: 2px solid black;\n"
                                            "border-radius: 5px;\n"
                                            "border-color: #20730b;\n"
                                            "text-align: center;")
        self.lEPrezzoAcquisto.setAlignment(QtCore.Qt.AlignCenter)
        self.lEPrezzoAcquisto.setObjectName("lEPrezzoAcquisto")
        self.lEQuantita = QtWidgets.QLineEdit(PaginaAggiungiOrdini)
        self.lEQuantita.setGeometry(QtCore.QRect(440, 160, 121, 41))
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
        self.labelQuantita.setGeometry(QtCore.QRect(440, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.labelQuantita.setFont(font)
        self.labelQuantita.setStyleSheet("background: transparent;\n"
                                         "color: #20730b;")
        self.labelQuantita.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuantita.setObjectName("labelQuantita")

        self.identificatoreUtilizzatore = 0

        #self.creaNuovoOrdine()

        self.TableProdottiOrdine.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.retranslateUi(PaginaAggiungiOrdini)
        QtCore.QMetaObject.connectSlotsByName(PaginaAggiungiOrdini)

    def retranslateUi(self, PaginaAggiungiOrdini):
        _translate = QtCore.QCoreApplication.translate
        PaginaAggiungiOrdini.setWindowTitle(_translate("PaginaAggiungiOrdini", "Form"))
        item = self.TableProdottiOrdine.horizontalHeaderItem(0)
        item.setText(_translate("PaginaAggiungiOrdini", "Numero PagineOrdine"))
        item = self.TableProdottiOrdine.horizontalHeaderItem(1)
        item.setText(_translate("PaginaAggiungiOrdini", "Codice Prodotto"))
        item = self.TableProdottiOrdine.horizontalHeaderItem(2)
        item.setText(_translate("PaginaAggiungiOrdini", "Nome Prodotto"))
        item = self.TableProdottiOrdine.horizontalHeaderItem(3)
        item.setText(_translate("PaginaAggiungiOrdini", "Prezzo Acquisto"))
        item = self.TableProdottiOrdine.horizontalHeaderItem(4)
        item.setText(_translate("PaginaAggiungiOrdini", "Quantità"))
        self.labelDNM.setText(_translate("PaginaAggiungiOrdini", "Inserendo prodotti nell\'ordine numero: "))
        self.labelCodiceProdotto.setText(_translate("PaginaAggiungiOrdini", "CODICE PRODOTTO"))
        self.labelNomeProdotto.setText(_translate("PaginaAggiungiOrdini", "NOME PRODOTTO"))
        self.labelPrezzoAcquisto.setText(_translate("PaginaAggiungiOrdini", "PREZZO ACQUISTO"))
        self.labelQuantita.setText(_translate("PaginaAggiungiOrdini", "QUANTITA\'"))

        self.ButtonAggiungiProdotto.clicked.connect(self.aggiungiNuovoProdotto)


    def setIdentificatoreUtilizzatore(self, codiceUtilizzatore):
        self.identificatoreUtilizzatore = codiceUtilizzatore

    def creaNuovoOrdine(self):

        mydb = mysql.connector.connect(
            host="localhost",
            user="alessio",
            password="alessio",
            database="prova"
        )

        mycursor = mydb.cursor()

        dataOdierna = date.today()
        dataFutura = date.today() + datetime.timedelta(days=3)

        if dataFutura.isoweekday() == 6:
            dataFutura = dataFutura + datetime.timedelta(days=2)

        if dataFutura.isoweekday() == 7:
            dataFutura = dataFutura + datetime.timedelta(days=1)

        dataOdierna = str(dataOdierna)
        dataFutura = str(dataFutura)

        idUtilizzatoreStr = str(self.identificatoreUtilizzatore)

        queryNuovoOrdine = "INSERT INTO ordine VALUES('', '" + dataOdierna + "' , 'false', '" + dataFutura + "', " + idUtilizzatoreStr + ")"
        mycursor.execute(queryNuovoOrdine)

        mydb.commit()

        queryUltimoCodiceOrdine = "SELECT MAX(ordine.IDOrdine) FROM ordine"
        mycursor.execute(queryUltimoCodiceOrdine)
        myresult = mycursor.fetchone()

        maxIdOrdine = 0

        for x in myresult:
            maxIdOrdine = x

        self.labelCodiceOrdine.setText(str(maxIdOrdine))
        #self.ButtonAggiungiProdotto.clicked.connect(self.aggiungiNuovoProdotto)

    def aggiungiNuovoProdotto(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="alessio",
            password="alessio",
            database="prova"
        )

        mycursor = mydb.cursor()

        codiceProdotto = self.lECodiceProdotto.text()
        nomeProdotto = self.lENomeProdotto.text()
        prezzoAcquisto = self.lEPrezzoAcquisto.text()
        quantitaAcquistata = self.lEQuantita.text()

        queryProdottoEsistente = "SELECT * FROM prodotto WHERE prodotto.IDProdotto = " + codiceProdotto
        mycursor.execute(queryProdottoEsistente)
        myresult = mycursor.fetchall()

        contaProdotti = 0

        for row in myresult:
            contaProdotti += 1

        if contaProdotti != 0:
            queryProdottoEsistent = "SELECT prodotto.PrezzoAcquisto FROM prodotto WHERE prodotto.IDProdotto = " + codiceProdotto
            mycursor.execute(queryProdottoEsistent)
            myresult = mycursor.fetchall()

            prezzoAcquisto = 0

            for row in myresult:
                #print(str(row[0]))
                prezzoAcquisto = str(row[0])


            self.aggiungiProdottoInOrdine(prezzoAcquisto, quantitaAcquistata, codiceProdotto)
        else:
            prezzoVendita = (float(prezzoAcquisto) * 50) / 100 + float(prezzoAcquisto)

            queryAggiungiProdotto = "INSERT INTO prodotto VALUES(" + codiceProdotto + " , '" + nomeProdotto + "' , " + str(prezzoAcquisto) + " , " + str(prezzoVendita) + " , 'null' , 1 )"
            mycursor.execute(queryAggiungiProdotto)
            mydb.commit()

            self.aggiungiProdottoInOrdine(prezzoAcquisto, quantitaAcquistata, codiceProdotto)

    def aggiungiProdottoInOrdine(self, prezzoAcquisto, quantitaAcquistata, codiceProdotto):

        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()



        totaleAcquisto = float(prezzoAcquisto) * int(quantitaAcquistata)
        codiceOrdine = str(self.labelCodiceOrdine.text())
        queryAggiungiAcquisto = "INSERT INTO prodottoacquistato VALUES( " + codiceOrdine + ", " + codiceProdotto + ", " + str(quantitaAcquistata) + ", " + str(totaleAcquisto) + ")"
        mycursor.execute(queryAggiungiAcquisto)
        mydb.commit()
        self.caricaDatiProdotto(codiceOrdine)

    def caricaDatiProdotto(self, codiceOrdine):
        mydb = mysql.connector.connect(
            host="localhost",
            user="alessio",
            password="alessio",
            database="prova"
        )

        mycursor = mydb.cursor()

        queryCaricaDati = "SELECT DISTINCT prodottoacquistato.IDOrdine, prodotto.IDProdotto, prodotto.NomeProdotto, prodotto.PrezzoAcquisto, prodottoacquistato.QuantitaAcquistata FROM prodottoacquistato INNER JOIN prodotto ON prodottoacquistato.IDProdotto = prodotto.IDProdotto WHERE prodottoacquistato.IDOrdine = " + codiceOrdine
        mycursor.execute(queryCaricaDati)
        risultatoQueryCaricaDati = mycursor.fetchall()
        rigaTabella = 0
        righeTotali = 0

        for row in risultatoQueryCaricaDati:
            righeTotali += 1

        self.TableProdottiOrdine.setRowCount(righeTotali)

        for row in risultatoQueryCaricaDati:
            self.TableProdottiOrdine.verticalHeader().setVisible(bool(0))
            self.TableProdottiOrdine.setItem(rigaTabella, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.TableProdottiOrdine.setItem(rigaTabella, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.TableProdottiOrdine.setItem(rigaTabella, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TableProdottiOrdine.setItem(rigaTabella, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.TableProdottiOrdine.setItem(rigaTabella, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            rigaTabella += 1

    def annullaOrdine(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()

        codiceOrdine = str(self.labelCodiceOrdine.text())
        queryRimuoviProdottiOrdine = "DELETE FROM prodottoacquistato WHERE prodottoacquistato.IDOrdine = " + codiceOrdine
        mycursor.execute(queryRimuoviProdottiOrdine)
        mydb.commit()

        queryRimuoviOrdine = "DELETE FROM ordine WHERE ordine.IDOrdine = " + codiceOrdine
        mycursor.execute(queryRimuoviOrdine)
        mydb.commit()

        self.cancellaDatiPrecendeti()

    def cancellaDatiPrecendeti(self):
        self.lENomeProdotto.setText('')
        self.lEPrezzoAcquisto.setText('')
        self.lEQuantita.setText('')
        self.lECodiceProdotto.setText('')

        righeTabella = self.TableProdottiOrdine.rowCount()
        x = 0
        for x in range(righeTabella):
            self.TableProdottiOrdine.removeRow(x)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaAggiungiOrdini = QtWidgets.QWidget()
    ui = Ui_PaginaAggiungiOrdini()
    ui.setupUi(PaginaAggiungiOrdini)
    PaginaAggiungiOrdini.show()
    sys.exit(app.exec_())
