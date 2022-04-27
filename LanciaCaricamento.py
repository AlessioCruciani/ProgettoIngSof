import time

from PyQt5.QtWidgets import QApplication, QWidget
from Caricamento import Ui_Caricamento
from PyQt5.QtCore import QBasicTimer
import sys



app2 = QApplication([])
finestraCaricamento = QWidget()
uiCaricamento = Ui_Caricamento()
uiCaricamento.setupUi(finestraCaricamento)
finestraCaricamento.show()
pro = 0
completato = 0
while pro < 100 :
    completato+= 0.01
    pro = int(completato/1000)
    uiCaricamento.caricamento.setValue(pro)









app2.exec()



