# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaAggiungiPrenotazione.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import mysql.connector

class Ui_AggiungiPrenotazione(object):
        def setupUi(self, AggiungiPrenotazione):
                AggiungiPrenotazione.setObjectName("AggiungiPrenotazione")
                AggiungiPrenotazione.resize(840, 571)
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                AggiungiPrenotazione.setFont(font)
                AggiungiPrenotazione.setStyleSheet("\n"
                                                   "background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPrenotazioni/SfondoAggiungiPrenotazioni.png);")
                self.labelNome = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelNome.setGeometry(QtCore.QRect(60, 160, 220, 40))
                self.labelNome.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPrenotazioni/NomeFidelity.png);\n"
                                             "background-position: center;\n"
                                             "border-bottom: 2px solid black;\n"
                                             "border-radius: 20px;\n"
                                             "border-color: #20730b;")
                self.labelNome.setText("")
                self.labelNome.setObjectName("labelNome")
                self.lineEditNome = QtWidgets.QLineEdit(AggiungiPrenotazione)
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
                self.labelCognome = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelCognome.setGeometry(QtCore.QRect(60, 220, 220, 40))
                self.labelCognome.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPrenotazioni/CognomeFidelity.png);\n"
                                                "background-position: center;\n"
                                                "border-bottom: 2px solid black;\n"
                                                "border-radius: 20px;\n"
                                                "border-color: #20730b;")
                self.labelCognome.setText("")
                self.labelCognome.setObjectName("labelCognome")
                self.labelData = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelData.setGeometry(QtCore.QRect(60, 340, 220, 40))
                self.labelData.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPrenotazioni/labelData.png);\n"
                                             "background-position: center;\n"
                                             "border-bottom: 2px solid black;\n"
                                             "border-radius: 20px;\n"
                                             "border-color: #20730b;")
                self.labelData.setText("")
                self.labelData.setObjectName("labelData")
                self.labelMail = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelMail.setGeometry(QtCore.QRect(60, 280, 220, 40))
                self.labelMail.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPrenotazioni/EmailFidelity.png);\n"
                                             "background-position: center;\n"
                                             "border-bottom: 2px solid black;\n"
                                             "border-radius: 20px;\n"
                                             "border-color: #20730b;")
                self.labelMail.setText("")
                self.labelMail.setObjectName("labelMail")
                self.lineEditEmail = QtWidgets.QLineEdit(AggiungiPrenotazione)
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
                self.lineEditCognome = QtWidgets.QLineEdit(AggiungiPrenotazione)
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
                self.labelOra = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelOra.setGeometry(QtCore.QRect(60, 400, 220, 40))
                self.labelOra.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPrenotazioni/labelOrario.png);\n"
                                            "background-position: center;\n"
                                            "border-bottom: 2px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "border-color: #20730b;")
                self.labelOra.setText("")
                self.labelOra.setObjectName("labelOra")
                self.ButtonConferma = QtWidgets.QPushButton(AggiungiPrenotazione)
                self.ButtonConferma.setGeometry(QtCore.QRect(540, 500, 220, 40))
                self.ButtonConferma.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPrenotazioni/ButtonConfermaPrenotazioni.png);\n"
                                                  "background-position: center;\n"
                                                  "border: 2px solid black;\n"
                                                  "border-radius: 10px;\n"
                                                  "border-color: #20730b;")
                self.ButtonConferma.setText("")
                self.ButtonConferma.setObjectName("ButtonConferma")
                self.dateEdit = QtWidgets.QDateEdit(AggiungiPrenotazione)
                self.dateEdit.setGeometry(QtCore.QRect(300, 340, 381, 41))
                self.dateEdit.setStyleSheet("background-position: center;\n"
                                            "border: 2px solid black;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: #20730b;\n"
                                            "padding-left: 10px;")
                self.dateEdit.setWrapping(True)
                self.dateEdit.setFrame(True)
                self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
                self.dateEdit.setAccelerated(False)
                self.dateEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
                self.dateEdit.setProperty("showGroupSeparator", True)
                self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
                self.dateEdit.setCalendarPopup(True)
                self.dateEdit.setDate(QtCore.QDate(2022, 5, 19))
                self.dateEdit.setObjectName("dateEdit")
                self.timeEdit = QtWidgets.QTimeEdit(AggiungiPrenotazione)
                self.timeEdit.setGeometry(QtCore.QRect(300, 400, 381, 41))
                self.timeEdit.setStyleSheet("background-position: center;\n"
                                            "border: 2px solid black;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: #20730b;\n"
                                            "padding-left: 10px;")
                self.timeEdit.setWrapping(True)
                self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
                self.timeEdit.setCalendarPopup(True)
                self.timeEdit.setTimeSpec(QtCore.Qt.LocalTime)
                self.timeEdit.setObjectName("timeEdit")
                self.ButtonAnnulla = QtWidgets.QPushButton(AggiungiPrenotazione)
                self.ButtonAnnulla.setGeometry(QtCore.QRect(300, 500, 220, 40))
                self.ButtonAnnulla.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPrenotazioni/ButtonAnnullaPrenotazioni.png);\n"
                                                 "background-position: center;\n"
                                                 "border: 2px solid black;\n"
                                                 "border-radius: 10px;\n"
                                                 "border-color: #20730b;")
                self.ButtonAnnulla.setText("")
                self.ButtonAnnulla.setObjectName("ButtonAnnulla")

                self.identificatoreUtilizzatore = 0

                self.retranslateUi(AggiungiPrenotazione)
                QtCore.QMetaObject.connectSlotsByName(AggiungiPrenotazione)  //carica i dati nella tabella

        def retranslateUi(self, AggiungiPrenotazione):
                _translate = QtCore.QCoreApplication.translate
                AggiungiPrenotazione.setWindowTitle(_translate("AggiungiPrenotazione", "Form"))

        def setIdentificatoreUtilizzatore(self, codiceUtilizzatore):
                self.identificatoreUtilizzatore = codiceUtilizzatore

        def creaNuovaPrenotazione(self):   //PASSA I DATI PER CREARE UNA NUOVA PRENOTAZIONE (NOME, COGNOME, EMAIL, DATA E ORA) E GLI INSERISCE IN UNA STRINGA
                nome = self.lineEditNome.text()
                cognome = self.lineEditCognome.text()
                email = self.lineEditEmail.text()
                data = (self.dateEdit.date()).toString(QtCore.Qt.ISODate)
                #data = self.dateEdit.text()
                ora = self.timeEdit.text()
                idutilizzatoreStr = str(self.identificatoreUtilizzatore)

                mydb = mysql.connector.connect(host="localhost",user="alessio",password="alessio",database="prova")
                mycursor = mydb.cursor()

                queryAggiungiPrenotazione = "INSERT INTO prenotazioni VALUES ('', '" + nome + "','" + cognome + "','" + email + "','" + str(data) + "', '" + ora + "' ," + idutilizzatoreStr + ")"
                mycursor.execute(queryAggiungiPrenotazione)

                mydb.commit()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        AggiungiPrenotazione = QtWidgets.QWidget()
        ui = Ui_AggiungiPrenotazione()
        ui.setupUi(AggiungiPrenotazione)
        AggiungiPrenotazione.show()
        sys.exit(app.exec_())
