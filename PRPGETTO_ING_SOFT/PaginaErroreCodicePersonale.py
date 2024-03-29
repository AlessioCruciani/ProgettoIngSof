from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErroreCodicePersonale(object):
    def setupUi(self, Errore):
        Errore.setObjectName("Errore")
        Errore.resize(487, 122)
        self.ButtonIndietro = QtWidgets.QPushButton(Errore)
        self.ButtonIndietro.setGeometry(QtCore.QRect(320, 80, 150, 30))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(12)
        self.ButtonIndietro.setFont(font)
        self.ButtonIndietro.setStyleSheet("background-image: url(ImmaginiProgetto/ImmaginiErrore/ButtonIndietro.png);\n"
                                          "background-position: center;\n"
                                          "border: 2px solid black;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: #20730b;")
        self.ButtonIndietro.setText("")
        self.ButtonIndietro.setObjectName("ButtonIndietro")
        self.labelDNMerrore = QtWidgets.QLabel(Errore)
        self.labelDNMerrore.setGeometry(QtCore.QRect(20, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.labelDNMerrore.setFont(font)
        self.labelDNMerrore.setStyleSheet("color: red;")
        self.labelDNMerrore.setObjectName("labelDNMerrore")
        self.labelNomeErrore = QtWidgets.QLabel(Errore)
        self.labelNomeErrore.setGeometry(QtCore.QRect(120, 20, 321, 21))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(14)
        self.labelNomeErrore.setFont(font)
        self.labelNomeErrore.setStyleSheet("color: red;")
        self.labelNomeErrore.setObjectName("labelNomeErrore")
        self.labelDescrizioneErrore = QtWidgets.QLabel(Errore)
        self.labelDescrizioneErrore.setGeometry(QtCore.QRect(20, 36, 461, 40))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        self.labelDescrizioneErrore.setFont(font)
        self.labelDescrizioneErrore.setObjectName("labelDescrizioneErrore")

        self.retranslateUi(Errore)
        QtCore.QMetaObject.connectSlotsByName(Errore)

    def retranslateUi(self, Errore):
        _translate = QtCore.QCoreApplication.translate
        Errore.setWindowTitle(_translate("Errore", "Form"))
        self.labelDNMerrore.setText(_translate("Errore", "ERRORE :"))
        self.labelNomeErrore.setText(_translate("Errore", "CODICE PERSONALE ERRATO"))
        self.labelDescrizioneErrore.setText(_translate("Errore", "Il codice del personale inserito non esiste."))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Errore = QtWidgets.QWidget()
    ui = Ui_ErroreCodicePersonale()
    ui.setupUi(Errore)
    Errore.show()
    sys.exit(app.exec_())