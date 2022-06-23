# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaPersonale.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_PaginaPersonale(object):
    def setupUi(self, PaginaPersonale):
        PaginaPersonale.setObjectName("PaginaPersonale")
        PaginaPersonale.resize(840, 571)
        PaginaPersonale.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/SfondoPersonale.png);")
        self.TablePersonale = QtWidgets.QTableWidget(PaginaPersonale)
        self.TablePersonale.setGeometry(QtCore.QRect(100, 200, 621, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TablePersonale.sizePolicy().hasHeightForWidth())
        self.TablePersonale.setSizePolicy(sizePolicy)
        self.TablePersonale.setStyleSheet(
            "background-color: rgb(122, 122, 122);\n"
            "alternate-background-color: rgb(218, 218, 218);\n"
            "background: none;\n"
            "border: 2px solid white;\n"
            "border-bottom-color: #20730b;\n"
            "td: 100px;\n"
            "\n"
            "")
        self.TablePersonale.setObjectName("TablePersonale")
        self.TablePersonale.setColumnCount(9)
        self.TablePersonale.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablePersonale.setHorizontalHeaderItem(8, item)
        self.ButtonAggiungiPersonale = QtWidgets.QPushButton(PaginaPersonale)
        self.ButtonAggiungiPersonale.setGeometry(QtCore.QRect(60, 450, 221, 40))
        self.ButtonAggiungiPersonale.setStyleSheet("background-position: center;\n"
                                                   "background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/ButtonAggiungiPersonale.png);\n"
                                                   "border: 2px solid black;\n"
                                                   "border-radius: 10px;\n"
                                                   "border-color: #20730b;")
        self.ButtonAggiungiPersonale.setText("")
        self.ButtonAggiungiPersonale.setObjectName("ButtonAggiungiPersonale")

        self.ButtonRimuoviPersonale = QtWidgets.QPushButton(PaginaPersonale)
        self.ButtonRimuoviPersonale.setGeometry(QtCore.QRect(300, 450, 221, 40))
        self.ButtonRimuoviPersonale.setStyleSheet("background-position: center;\n"
                                                   "background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/ButtonRimuoviPersonale.png);\n"
                                                   "border: 2px solid black;\n"
                                                   "border-radius: 10px;\n"
                                                   "border-color: #20730b;")
        self.ButtonRimuoviPersonale.setText("")
        self.ButtonRimuoviPersonale.setObjectName("ButtonRimuoviPersonale")

        self.ButtonCercaPersonale = QtWidgets.QPushButton(PaginaPersonale)
        self.ButtonCercaPersonale.setGeometry(QtCore.QRect(500, 120, 220, 40))
        self.ButtonCercaPersonale.setStyleSheet("background-position: center;\n"
                                                "background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/ButtonCercaPersonale.png);\n"
                                                "border: 2px solid black;\n"
                                                "border-radius: 10px;\n"
                                                "border-color: #20730b;")
        self.ButtonCercaPersonale.setText("")
        self.ButtonCercaPersonale.setObjectName("ButtonCercaPersonale")
        self.ButtonModificaPermessi = QtWidgets.QPushButton(PaginaPersonale)
        self.ButtonModificaPermessi.setGeometry(QtCore.QRect(540, 450, 220, 40))
        self.ButtonModificaPermessi.setStyleSheet("background-position: center;\n"
                                               "background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/ButtonModificaPermessi.png);\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 10px;\n"
                                               "border-color: #20730b;")
        self.ButtonModificaPermessi.setText("")
        self.ButtonModificaPermessi.setObjectName("ButtonModificaPermessi")
        self.ButtonHomePersonale = QtWidgets.QPushButton(PaginaPersonale)
        self.ButtonHomePersonale.setGeometry(QtCore.QRect(540, 500, 220, 40))
        self.ButtonHomePersonale.setStyleSheet("background-position: center;\n"
                                               "background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/ButtonHome.png);\n"
                                               "border: 2px solid black;\n"
                                               "border-radius: 10px;\n"
                                               "border-color: #20730b;")
        self.ButtonHomePersonale.setText("")
        self.ButtonHomePersonale.setObjectName("ButtonHomePersonale")
        self.lineEditPersonale = QtWidgets.QLineEdit(PaginaPersonale)
        self.lineEditPersonale.setGeometry(QtCore.QRect(100, 120, 381, 41))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.lineEditPersonale.setFont(font)
        self.lineEditPersonale.setStyleSheet("background: none;\n"
                                             "border: 2px solid black;\n"
                                             "border-radius: 5px;\n"
                                             "border-color: #20730b;\n"
                                             "text-align: center;")
        self.lineEditPersonale.setObjectName("lineEditPersonale")

        self.TablePersonale.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.caricaDatiPersonale()
        self.ButtonCercaPersonale.clicked.connect(self.cercaDatiPersonale)
        self.IdentificatoreUtilizzatore = 0

        self.retranslateUi(PaginaPersonale)
        QtCore.QMetaObject.connectSlotsByName(PaginaPersonale)

    def retranslateUi(self, PaginaPersonale):
        _translate = QtCore.QCoreApplication.translate
        PaginaPersonale.setWindowTitle(_translate("PaginaPersonale", "Form"))
        item = self.TablePersonale.horizontalHeaderItem(0)
        item.setText(_translate("PaginaPersonale", "Codice Personale"))
        item = self.TablePersonale.horizontalHeaderItem(1)
        item.setText(_translate("PaginaPersonale", "Nome"))
        item = self.TablePersonale.horizontalHeaderItem(2)
        item.setText(_translate("PaginaPersonale", "Cognome"))
        item = self.TablePersonale.horizontalHeaderItem(3)
        item.setText(_translate("PaginaPersonale", "Codice Fiscale"))
        item = self.TablePersonale.horizontalHeaderItem(4)
        item.setText(_translate("PaginaPersonale", "Data Nascita"))
        item = self.TablePersonale.horizontalHeaderItem(5)
        item.setText(_translate("PaginaPersonale", "Stipendio"))
        item = self.TablePersonale.horizontalHeaderItem(6)
        item.setText(_translate("PaginaPersonale", "Permessi"))
        item = self.TablePersonale.horizontalHeaderItem(7)
        item.setText(_translate("PaginaPersonale", "Email"))
        item = self.TablePersonale.horizontalHeaderItem(8)
        item.setText(_translate("PaginaPersonale", "Telefono"))

    def caricaDatiPersonale(self):
        mydb = mysql.connector.connect(host="localhost",user="alessio",password="alessio",database="prova")
        mycursor = mydb.cursor()

        queryTablePersonale = "SELECT * FROM utilizzatore WHERE utilizzatore.Impiegato = 'true'"
        mycursor.execute(queryTablePersonale)
        risultatoQueryPersonale = mycursor.fetchall()
        rigaTabella = 0
        righeTotali = 0

        for row in risultatoQueryPersonale:
            righeTotali += 1

        self.TablePersonale.setRowCount(righeTotali)

        for row in risultatoQueryPersonale:
            self.TablePersonale.verticalHeader().setVisible(bool(0))
            self.TablePersonale.setItem(rigaTabella, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.TablePersonale.setItem(rigaTabella, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.TablePersonale.setItem(rigaTabella, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TablePersonale.setItem(rigaTabella, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.TablePersonale.setItem(rigaTabella, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.TablePersonale.setItem(rigaTabella, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.TablePersonale.setItem(rigaTabella, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.TablePersonale.setItem(rigaTabella, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.TablePersonale.setItem(rigaTabella, 8, QtWidgets.QTableWidgetItem(str(row[8])))

            rigaTabella += 1

    def cercaDatiPersonale(self):
        richiesta = self.lineEditPersonale.text()
        mydb = mysql.connector.connect(host="localhost",user="alessio",password="alessio",database="prova")
        mycursor = mydb.cursor()
        queryRicercaPersonale = "SELECT * FROM utilizzatore WHERE (utilizzatore.Impiegato = 'true') AND (utilizzatore.Nome = '" + richiesta + "' OR utilizzatore.Cognome = '" + richiesta + "' OR utilizzatore.IDUtilizzatore ='" + richiesta + "')"
        mycursor.execute(queryRicercaPersonale)
        risultatoRicercaPersonale = mycursor.fetchall()

        rigaTabella = 0
        righeTotali = 0

        for row in risultatoRicercaPersonale:
            righeTotali += 1

        self.TablePersonale.setRowCount(righeTotali)

        for row in risultatoRicercaPersonale:
            self.TablePersonale.verticalHeader().setVisible(bool(0))
            self.TablePersonale.setItem(rigaTabella, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.TablePersonale.setItem(rigaTabella, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.TablePersonale.setItem(rigaTabella, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.TablePersonale.setItem(rigaTabella, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.TablePersonale.setItem(rigaTabella, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.TablePersonale.setItem(rigaTabella, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.TablePersonale.setItem(rigaTabella, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.TablePersonale.setItem(rigaTabella, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.TablePersonale.setItem(rigaTabella, 8, QtWidgets.QTableWidgetItem(str(row[8])))

            rigaTabella += 1

    def setIdentificatoreUtilizzatore(self, CodiceUtilizzatore):
        self.IdentificatoreUtilizzatore = CodiceUtilizzatore

    def controllaPermessiUtilizzatore(self):
        mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
        mycursor = mydb.cursor()
        queryPermessiUtilizzatore = "SELECT utilizzatore.Permessi FROM utilizzatore WHERE utilizzatore.IDUtilizzatore = '" + str(self.IdentificatoreUtilizzatore) +"'"
        mycursor.execute(queryPermessiUtilizzatore)
        risultatoPermessiUtilizzatore = mycursor.fetchall()

        livelloPermessi = ''

        for row in risultatoPermessiUtilizzatore:
            livelloPermessi = str(row[0])

        if livelloPermessi == 'medium' or livelloPermessi == 'high' :
            return bool(1)
        else:
            return bool(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaginaPersonale = QtWidgets.QWidget()
    ui = Ui_PaginaPersonale()
    ui.setupUi(PaginaPersonale)
    PaginaPersonale.show()
    sys.exit(app.exec_())
