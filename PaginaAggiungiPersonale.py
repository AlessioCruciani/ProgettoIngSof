# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aless\Desktop\uiFILEs\PaginaAggiungiPersonale.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_AggiungiPersonale(object):
        def setupUi(self, AggiungiPersonale):
                AggiungiPersonale.setObjectName("AggiungiPersonale")
                AggiungiPersonale.resize(840, 571)
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                AggiungiPersonale.setFont(font)
                AggiungiPersonale.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/SfondoAggiungiPersonale.png);")
                self.labelNome = QtWidgets.QLabel(AggiungiPersonale) //INDICA IL RIQUADRO DI INSERIMENTO DEL NOME (LO INTESTA SOLO)
                self.labelNome.setGeometry(QtCore.QRect(40, 160, 161, 40))
                self.labelNome.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/NomeFidelity.png);\n"
                                             "background-position: center;\n"
                                             "border-bottom: 2px solid black;\n"
                                             "border-radius: 20px;\n"
                                             "border-color: #20730b;")
                self.labelNome.setText("")
                self.labelNome.setObjectName("labelNome")
                self.lineEditNome = QtWidgets.QLineEdit(AggiungiPersonale) // CI PERMETTE DI INSERIRE IL COME DA AGGIUNGERE (LineEdit)
                self.lineEditNome.setGeometry(QtCore.QRect(220, 160, 181, 40))
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
                self.labelCognome = QtWidgets.QLabel(AggiungiPersonale)
                self.labelCognome.setGeometry(QtCore.QRect(40, 220, 161, 40))
                self.labelCognome.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/CognomeFidelity.png);\n"
                                                "background-position: center;\n"
                                                "border-bottom: 2px solid black;\n"
                                                "border-radius: 20px;\n"
                                                "border-color: #20730b;")
                self.labelCognome.setText("")
                self.labelCognome.setObjectName("labelCognome")
                self.LabelTelefono = QtWidgets.QLabel(AggiungiPersonale)
                self.LabelTelefono.setGeometry(QtCore.QRect(40, 340, 161, 40))
                self.LabelTelefono.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/TelefonoFidelity.png);\n"
                                                 "background-position: center;\n"
                                                 "border-bottom: 2px solid black;\n"
                                                 "border-radius: 20px;\n"
                                                 "border-color: #20730b;")
                self.LabelTelefono.setText("")
                self.LabelTelefono.setObjectName("LabelTelefono")
                self.labelMail = QtWidgets.QLabel(AggiungiPersonale)
                self.labelMail.setGeometry(QtCore.QRect(40, 280, 161, 40))
                self.labelMail.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/EmailFidelity.png);\n"
                                             "background-position: center;\n"
                                             "border-bottom: 2px solid black;\n"
                                             "border-radius: 20px;\n"
                                             "border-color: #20730b;")
                self.labelMail.setText("")
                self.labelMail.setObjectName("labelMail")
                self.lineEditEmail = QtWidgets.QLineEdit(AggiungiPersonale)
                self.lineEditEmail.setGeometry(QtCore.QRect(220, 280, 181, 40))
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
                self.lineEditCognome = QtWidgets.QLineEdit(AggiungiPersonale)
                self.lineEditCognome.setGeometry(QtCore.QRect(220, 220, 181, 40))
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
                self.lineEditTelefono = QtWidgets.QLineEdit(AggiungiPersonale)
                self.lineEditTelefono.setGeometry(QtCore.QRect(220, 340, 181, 40))
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                self.lineEditTelefono.setFont(font)
                self.lineEditTelefono.setStyleSheet("background-position: center;\n"
                                                    "border: 2px solid black;\n"
                                                    "border-radius: 10px;\n"
                                                    "border-color: #20730b;\n"
                                                    "padding-left: 10px;")
                self.lineEditTelefono.setObjectName("lineEditTelefono")
                self.buttonConfermaInserimento = QtWidgets.QPushButton(AggiungiPersonale)
                self.buttonConfermaInserimento.setGeometry(QtCore.QRect(520, 500, 220, 40))
                self.buttonConfermaInserimento.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/ButtonConfermaInserimento.png);\n"
                                                             "background-position: center;\n"
                                                             "border: 2px solid black;\n"
                                                             "border-radius: 10px;\n"
                                                             "border-color: #20730b;")
                self.buttonConfermaInserimento.setText("") //CREIAMO SOLO IL BOTTONE
                self.buttonConfermaInserimento.setObjectName("buttonConfermaInserimento")
                self.labelStipendio = QtWidgets.QLabel(AggiungiPersonale)
                self.labelStipendio.setGeometry(QtCore.QRect(440, 220, 161, 40))
                self.labelStipendio.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/labelStipendio.png);\n"
                                                  "background-position: center;\n"
                                                  "border-bottom: 2px solid black;\n"
                                                  "border-radius: 20px;\n"
                                                  "border-color: #20730b;")
                self.labelStipendio.setText("")
                self.labelStipendio.setObjectName("labelStipendio")
                self.labelCF = QtWidgets.QLabel(AggiungiPersonale)
                self.labelCF.setGeometry(QtCore.QRect(440, 160, 161, 40))
                self.labelCF.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/labelCodiceFiscale.png);\n"
                                           "background-position: center;\n"
                                           "border-bottom: 2px solid black;\n"
                                           "border-radius: 20px;\n"
                                           "border-color: #20730b;")
                self.labelCF.setText("")
                self.labelCF.setObjectName("labelCF")
                self.labelDataNascita = QtWidgets.QLabel(AggiungiPersonale)
                self.labelDataNascita.setGeometry(QtCore.QRect(440, 280, 161, 40))
                self.labelDataNascita.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/labelDataNascita.png);\n"
                                                    "background-position: center;\n"
                                                    "border-bottom: 2px solid black;\n"
                                                    "border-radius: 20px;\n"
                                                    "border-color: #20730b;")
                self.labelDataNascita.setText("")
                self.labelDataNascita.setObjectName("labelDataNascita")
                self.labelPassword = QtWidgets.QLabel(AggiungiPersonale)
                self.labelPassword.setGeometry(QtCore.QRect(440, 340, 161, 40))
                self.labelPassword.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/labelPassword.png);\n"
                                                 "background-position: center;\n"
                                                 "border-bottom: 2px solid black;\n"
                                                 "border-radius: 20px;\n"
                                                 "border-color: #20730b;")
                self.labelPassword.setText("")
                self.labelPassword.setObjectName("labelPassword")
                self.lineEditCF = QtWidgets.QLineEdit(AggiungiPersonale)
                self.lineEditCF.setGeometry(QtCore.QRect(620, 160, 181, 40))
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                self.lineEditCF.setFont(font)
                self.lineEditCF.setStyleSheet("background-position: center;\n"
                                              "border: 2px solid black;\n"
                                              "border-radius: 10px;\n"
                                              "border-color: #20730b;\n"
                                              "padding-left: 10px;")
                self.lineEditCF.setObjectName("lineEditCF")
                self.lineEditStipendio = QtWidgets.QLineEdit(AggiungiPersonale)
                self.lineEditStipendio.setGeometry(QtCore.QRect(620, 220, 181, 40))
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                self.lineEditStipendio.setFont(font)
                self.lineEditStipendio.setStyleSheet("background-position: center;\n"
                                                     "border: 2px solid black;\n"
                                                     "border-radius: 10px;\n"
                                                     "border-color: #20730b;\n"
                                                     "padding-left: 10px;")
                self.lineEditStipendio.setObjectName("lineEditStipendio")
                self.lineEditDataNascita = QtWidgets.QLineEdit(AggiungiPersonale)
                self.lineEditDataNascita.setGeometry(QtCore.QRect(620, 280, 181, 40))
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                self.lineEditDataNascita.setFont(font)
                self.lineEditDataNascita.setStyleSheet("background-position: center;\n"
                                                       "border: 2px solid black;\n"
                                                       "border-radius: 10px;\n"
                                                       "border-color: #20730b;\n"
                                                       "padding-left: 10px;")
                self.lineEditDataNascita.setObjectName("lineEditDataNascita")
                self.lineEditPassword = QtWidgets.QLineEdit(AggiungiPersonale)
                self.lineEditPassword.setGeometry(QtCore.QRect(620, 340, 181, 40))
                font = QtGui.QFont()
                font.setFamily("OpenSymbol")
                font.setPointSize(14)
                self.lineEditPassword.setFont(font)
                self.lineEditPassword.setStyleSheet("background-position: center;\n"
                                                    "border: 2px solid black;\n"
                                                    "border-radius: 10px;\n"
                                                    "border-color: #20730b;\n"
                                                    "padding-left: 10px;")
                self.lineEditPassword.setObjectName("lineEditPassword")
                self.pushButton_2 = QtWidgets.QPushButton(AggiungiPersonale)
                self.pushButton_2.setGeometry(QtCore.QRect(280, 500, 220, 40))
                self.pushButton_2.setStyleSheet("background-image: url(C:/Users/aless/Desktop/uiFILEs/ImmaginiPersonale/ButtonAnnullaInserimento.png);\n"
                                                "background-position: center;\n"
                                                "border: 2px solid black;\n"
                                                "border-radius: 10px;\n"
                                                "border-color: #20730b;")
                self.pushButton_2.setText("")
                self.pushButton_2.setObjectName("pushButton_2")

                self.buttonConfermaInserimento.clicked.connect(self.creaNuovoPersonale)

                self.retranslateUi(AggiungiPersonale)
                QtCore.QMetaObject.connectSlotsByName(AggiungiPersonale)

        def retranslateUi(self, AggiungiPersonale):
                _translate = QtCore.QCoreApplication.translate
                AggiungiPersonale.setWindowTitle(_translate("AggiungiPersonale", "Form"))

        def creaNuovoPersonale(self): //QUELLA DI PRIMA è LA PARTE GRAFICA, INVECE QUESTA è DI IMPLEMENTAZIONE VERA E PROPRIA
            mydb = mysql.connector.connect(host="localhost", user="alessio", password="alessio", database="prova")
            mycursor = mydb.cursor()

            nome = self.lineEditNome.text()
            cognome = self.lineEditCognome.text()
            email = self.lineEditEmail.text()
            telefono = self.lineEditTelefono.text()
            cf = self.lineEditCF.text()
            stipendio = self.lineEditStipendio.text()
            datanascita = self.lineEditDataNascita.text()
            psw = self.lineEditPassword.text()


            queryAggiungiPersonale = "INSERT INTO utilizzatore VALUES ('', '" + nome + "','" + cognome + "','" + cf + "','" + datanascita + "','"+ stipendio +"','low', '" + email + "','" + telefono + "','" + psw + "', 'true' )"
            mycursor.execute(queryAggiungiPersonale)
            mydb.commit()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        AggiungiPersonale = QtWidgets.QWidget()
        ui = Ui_AggiungiPersonale()
        ui.setupUi(AggiungiPersonale)
        AggiungiPersonale.show()
        sys.exit(app.exec_())