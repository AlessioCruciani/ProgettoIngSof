import sys
import time

from PyQt5.QtWidgets import (QApplication, QWidget, QDialog,
                             QProgressBar, QPushButton)
from PaginaOrdini import Ui_PaginaOrdini

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PaginaOrdini(object):
    def setupUi(self, PaginaOrdini):
        PaginaOrdini.setObjectName("PaginaOrdini")
        PaginaOrdini.resize(840, 571)
        PaginaOrdini.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiOrdini/SfondoPaginaOrdini.png);")
        self.TableOrdini = QtWidgets.QTableWidget(PaginaOrdini)
        self.TableOrdini.setGeometry(QtCore.QRect(160, 240, 521, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableOrdini.sizePolicy().hasHeightForWidth())
        self.TableOrdini.setSizePolicy(sizePolicy)
        self.TableOrdini.setStyleSheet(
"background-color: rgb(122, 122, 122);\n"
"alternate-background-color: rgb(218, 218, 218);\n"
"background: none;\n"
"border: 2px solid white;\n"
"border-bottom-color: #20730b;\n"
"td: 100px;\n"
"\n"
"")
        self.TableOrdini.setObjectName("TableOrdini")
        self.TableOrdini.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.TableOrdini.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableOrdini.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableOrdini.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableOrdini.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableOrdini.setHorizontalHeaderItem(4, item)
        self.ButtonAggiungi = QtWidgets.QPushButton(PaginaOrdini)
        self.ButtonAggiungi.setGeometry(QtCore.QRect(60, 500, 221, 40))
        self.ButtonAggiungi.setStyleSheet("background-position: center;\n"
"background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiOrdini/ButtonAggiungiOrdini.png);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"border-color: #20730b;")
        self.ButtonAggiungi.setText("")
        self.ButtonAggiungi.setObjectName("ButtonAggiungi")
        self.ButtonCerca = QtWidgets.QPushButton(PaginaOrdini)
        self.ButtonCerca.setGeometry(QtCore.QRect(500, 160, 220, 40))
        self.ButtonCerca.setStyleSheet("background-position: center;\n"
"background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiOrdini/ButtonCercaOrdini.png);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"border-color: #20730b;")
        self.ButtonCerca.setText("")
        self.ButtonCerca.setObjectName("ButtonCerca")
        self.ButtonHome = QtWidgets.QPushButton(PaginaOrdini)
        self.ButtonHome.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonHome.setStyleSheet("background-position: center;\n"
"background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiOrdini/ButtonHome.png);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"border-color: #20730b;")
        self.ButtonHome.setText("")
        self.ButtonHome.setObjectName("ButtonHome")
        self.ButtonModifica = QtWidgets.QPushButton(PaginaOrdini)
        self.ButtonModifica.setGeometry(QtCore.QRect(300, 500, 220, 40))
        self.ButtonModifica.setStyleSheet("background-position: center;\n"
"background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiOrdini/ButtonModificaStatoOrdini.png);\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"border-color: #20730b;")
        self.ButtonModifica.setText("")
        self.ButtonModifica.setObjectName("ButtonModifica")
        self.lineEdit = QtWidgets.QLineEdit(PaginaOrdini)
        self.lineEdit.setGeometry(QtCore.QRect(100, 160, 381, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background: none;\n"
"border: 2px solid black;\n"
"border-radius: 5px;\n"
"border-color: #20730b;\n"
"text-align: center;")
        self.lineEdit.setObjectName("lineEdit")

        self.TableOrdini.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        #self.caricadatiOrdine()
        #self.ButtonCerca.clicked.connect(self.cercaOrdini)

        self.retranslateUi(PaginaOrdini)
        QtCore.QMetaObject.connectSlotsByName(PaginaOrdini)

    def cercaOrdini(self):
        richiesta = self.lineEdit.text()
        mydb = mysql.connector.connect(
            host="localhost",
            user="alessio",
            password="alessio",
            database="prova"
        )

        mycursor = mydb.cursor()
        queryRicercaOrdini = "SELECT * FROM ordine WHERE ordine.IdOrdine = '" + richiesta + "'"

        mycursor.execute(queryRicercaOrdini)
        risultatoRicercaOrdini = mycursor.fetchall()

        rigaTabella = 0
        righeTotali = 0

        for row in risultatoRicercaOrdini:
            righeTotali += 1

        self.TableOrdini.setRowCount(righeTotali)

        for row in risultatoRicercaOrdini:
            self.TableOrdini.verticalHeader().setVisible(bool(0))
            self.TableOrdini.setItem(rigaTabella, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.TableOrdini.setItem(rigaTabella, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.TableOrdini.setItem(rigaTabella, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TableOrdini.setItem(rigaTabella, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.TableOrdini.setItem(rigaTabella, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            rigaTabella += 1

    def caricadatiOrdine(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="alessio",
            password="alessio",
            database="prova"
        )

        mycursor = mydb.cursor()

        queryTableOrdine = "SELECT * FROM ordine"
        mycursor.execute(queryTableOrdine)
        risultatoQueryOrdine = mycursor.fetchall()
        rigaTabella = 0
        righeTotali = 0

        for row in risultatoQueryOrdine:
            righeTotali+=1

        self.TableOrdini.setRowCount(righeTotali)

        for row in risultatoQueryOrdine:
            self.TableOrdini.verticalHeader().setVisible(bool(0))
            self.TableOrdini.setItem(rigaTabella, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.TableOrdini.setItem(rigaTabella, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.TableOrdini.setItem(rigaTabella, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TableOrdini.setItem(rigaTabella, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.TableOrdini.setItem(rigaTabella, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            rigaTabella += 1

    def retranslateUi(self, PaginaOrdini):
        _translate = QtCore.QCoreApplication.translate
        PaginaOrdini.setWindowTitle(_translate("PaginaOrdini", "Form"))
        item = self.TableOrdini.horizontalHeaderItem(0)
        item.setText(_translate("PaginaOrdini", "Numero Ordine"))
        item = self.TableOrdini.horizontalHeaderItem(1)
        item.setText(_translate("PaginaOrdini", "Data Ordine"))
        item = self.TableOrdini.horizontalHeaderItem(2)
        item.setText(_translate("PaginaOrdini", "Data Consegna"))
        item = self.TableOrdini.horizontalHeaderItem(3)
        item.setText(_translate("PaginaOrdini", "Consegnato"))
        item = self.TableOrdini.horizontalHeaderItem(4)
        item.setText(_translate("PaginaOrdini", "ID Utilizzatore"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PaginaOrdini = QtWidgets.QWidget()
    ui = Ui_PaginaOrdini()
    ui.setupUi(PaginaOrdini)
    PaginaOrdini.show()
    sys.exit(app.exec_())
