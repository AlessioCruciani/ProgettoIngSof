from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import mysql.connector

class Ui_ModificaPrenotazione(object):
        def setupUi(self, AggiungiPrenotazione):
                AggiungiPrenotazione.setObjectName("AggiungiPrenotazione")
                AggiungiPrenotazione.resize(840, 571)
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                AggiungiPrenotazione.setFont(font)
                AggiungiPrenotazione.setStyleSheet("\n"
                                                   "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/SfondoModificaPrenotazione.png);")

                self.labelCodicePrenotazione = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelCodicePrenotazione.setGeometry(QtCore.QRect(60, 100, 220, 40))
                self.labelCodicePrenotazione.setStyleSheet(
                    "background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/LabelCodicePrenotazione.png);\n"
                    "background-position: center;\n"
                    "border-bottom: 2px solid black;\n"
                    "border-radius: 20px;\n"
                    "border-color: #20730b;")
                self.labelCodicePrenotazione.setText("")
                self.labelCodicePrenotazione.setObjectName("labelCodicePrenotazione")
                self.lineEditCodicePrenotazione = QtWidgets.QLineEdit(AggiungiPrenotazione)
                self.lineEditCodicePrenotazione.setGeometry(QtCore.QRect(300, 100, 381, 40))
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                self.lineEditCodicePrenotazione.setFont(font)
                self.lineEditCodicePrenotazione.setStyleSheet("background-position: center;\n"
                                                "border: 2px solid black;\n"
                                                "border-radius: 10px;\n"
                                                "border-color: #20730b;\n"
                                                "padding-left: 10px;")
                self.lineEditCodicePrenotazione.setObjectName("lineEditCodicePrenotazione")

                self.labelNome = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelNome.setGeometry(QtCore.QRect(60, 160, 220, 40))
                self.labelNome.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/NomeFidelity.png);\n"
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
                self.labelCognome.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/CognomeFidelity.png);\n"
                                                "background-position: center;\n"
                                                "border-bottom: 2px solid black;\n"
                                                "border-radius: 20px;\n"
                                                "border-color: #20730b;")
                self.labelCognome.setText("")
                self.labelCognome.setObjectName("labelCognome")
                self.labelData = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelData.setGeometry(QtCore.QRect(60, 340, 220, 40))
                self.labelData.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/labelData.png);\n"
                                             "background-position: center;\n"
                                             "border-bottom: 2px solid black;\n"
                                             "border-radius: 20px;\n"
                                             "border-color: #20730b;")
                self.labelData.setText("")
                self.labelData.setObjectName("labelData")
                self.labelMail = QtWidgets.QLabel(AggiungiPrenotazione)
                self.labelMail.setGeometry(QtCore.QRect(60, 280, 220, 40))
                self.labelMail.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/EmailFidelity.png);\n"
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
                self.labelOra.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/labelOrario.png);\n"
                                            "background-position: center;\n"
                                            "border-bottom: 2px solid black;\n"
                                            "border-radius: 20px;\n"
                                            "border-color: #20730b;")
                self.labelOra.setText("")
                self.labelOra.setObjectName("labelOra")
                self.ButtonConferma = QtWidgets.QPushButton(AggiungiPrenotazione)
                self.ButtonConferma.setGeometry(QtCore.QRect(540, 500, 220, 40))
                self.ButtonConferma.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonConfermaPrenotazioni.png);\n"
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
                self.ButtonAnnulla.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiPrenotazioni/ButtonAnnullaPrenotazioni.png);\n"
                                                 "background-position: center;\n"
                                                 "border: 2px solid black;\n"
                                                 "border-radius: 10px;\n"
                                                 "border-color: #20730b;")
                self.ButtonAnnulla.setText("")
                self.ButtonAnnulla.setObjectName("ButtonAnnulla")

                self.identificatoreUtilizzatore = 0

                self.retranslateUi(AggiungiPrenotazione)
                QtCore.QMetaObject.connectSlotsByName(AggiungiPrenotazione)

        def retranslateUi(self, AggiungiPrenotazione):
                _translate = QtCore.QCoreApplication.translate
                AggiungiPrenotazione.setWindowTitle(_translate("AggiungiPrenotazione", "Form"))

        def setIdentificatoreUtilizzatore(self, codiceUtilizzatore):
                self.identificatoreUtilizzatore = codiceUtilizzatore

        def controllaCodicePrenotazione(self):
            mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
            mycursor = mydb.cursor()

            codicePrenotazione = self.lineEditCodicePrenotazione.text()

            queryRicercaPrenotazione = "SELECT prenotazioni.IDPrenotazioni FROM prenotazioni WHERE prenotazioni.IDPrenotazioni = '" + str(
                codicePrenotazione) + "'"
            mycursor.execute(queryRicercaPrenotazione)
            risultatoRicercaPrenotazione = mycursor.fetchall()

            codicePrenotazioneEsistente = None

            for row in risultatoRicercaPrenotazione:
                codicePrenotazioneEsistente = row[0]

            if codicePrenotazioneEsistente != None:
                return 1
            else:
                return 0

        def modificaPrenotazione(self):
                codicePrenotazione = self.lineEditCodicePrenotazione.text()
                nome = self.lineEditNome.text()
                cognome = self.lineEditCognome.text()
                email = self.lineEditEmail.text()
                data = (self.dateEdit.date()).toString(QtCore.Qt.ISODate)
                #data = self.dateEdit.text()
                ora = self.timeEdit.text()
                idutilizzatoreStr = str(self.identificatoreUtilizzatore)

                mydb = mysql.connector.connect(host="localhost",user="alessio",password="alessio",database="prova")
                mycursor = mydb.cursor()

                queryModificaPrenotazione = "UPDATE prenotazioni SET prenotazioni.NomeCliente = '"+ nome +"', prenotazioni.CognomeCliente = '"+ cognome +"', prenotazioni.EmailCliente ='"+ email +"', prenotazioni.DataPrenotazione = '"+ str(data) +"', prenotazioni.OrarioPrenotazione = '"+ ora +"', prenotazioni.IDUtilizzatore = '"+ idutilizzatoreStr +"' WHERE prenotazioni.IDPrenotazioni = '"+ codicePrenotazione +"'"
                mycursor.execute(queryModificaPrenotazione)

                mydb.commit()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        AggiungiPrenotazione = QtWidgets.QWidget()
        ui = Ui_ModificaPrenotazione()
        ui.setupUi(AggiungiPrenotazione)
        AggiungiPrenotazione.show()
        sys.exit(app.exec_())
