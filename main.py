import sys
import mysql.connector
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QGraphicsTextItem

from LoginFinito import Ui_Login
from PaginaAggiungiPersonale import Ui_AggiungiPersonale  //Ui connessione alla "pagina"
from PaginaAggiungiPrenotazioni import Ui_AggiungiPrenotazione
from PaginaAggiungiSconti import Ui_PaginaAggiungiSconti
from PaginaErrore import Ui_Errore
from PaginaHome import Ui_HomePage
from PaginaFidelity2 import Ui_PaginaFidelity
from PaginaAggiungiFidelity import  Ui_AggiungiFidelity
from PaginaMagazzino import Ui_PaginaMagazzino
from PaginaOrdini import Ui_PaginaOrdini
from PaginaPersonale import Ui_PaginaPersonale
from PaginaAggiungiOrdine import Ui_PaginaAggiungiOrdini
from PaginaModificaStatoOrdine import Ui_PaginaModificaStatoOrdini
from PaginaPrenotazioni import Ui_PaginaPrenotazioni
from PaginaRimuoviPersonale import Ui_PaginaRimuoviDipendenti
from PaginaScontrini import Ui_PaginaScontrini
from PaginaAggiungiScontrino import Ui_PaginaAggiungiScontrini
from PaginaProdotti import Ui_PaginaProdotti
from PaginaStatistiche import Ui_Statistiche
from PaginaModificaPermessi import Ui_PaginaModificaPermessi

mydb = mysql.connector.connect(host="localhost",user="alessio",password="alessio",database="prova") 
mycursor = mydb.cursor() 

def controlla():
    myresult = 0
    query = ''
    query2 = ''

    mail = uiLogin.lEmail.text()
    psw = uiLogin.lEpassword.text()

    query = "SELECT utilizzatore.Email, utilizzatore.Psw FROM utilizzatore WHERE utilizzatore.Email = '" + mail + "' "
    query2 = " && utilizzatore.Psw = '" + psw + "'"

    query += query2
    mycursor.execute(query)
    myresult = mycursor.fetchone()

    if myresult == None :
        uiLogin.lineEdit.setText("L'Email o la Password inserite non sono corrette")
    else:
        uiLogin.lineEdit.setText('')
        queryCodiceUtilizzatore = "SELECT utilizzatore.IDUtilizzatore FROM utilizzatore WHERE utilizzatore.Email = '" + mail + "' && utilizzatore.Psw = '" + psw + "'"
        mycursor.execute(queryCodiceUtilizzatore)
        myresult = mycursor.fetchone()



        for x in myresult:
            uiAggiungiFidelityCard.setIdentificatoreUtilizzatore(x)
            uiAggiungiOrdine.setIdentificatoreUtilizzatore(x)
            uiAggiungiScontrino.setIdentificatoreUtilizzatore(x)
            uiPersonale.setIdentificatoreUtilizzatore(x)
            uiProdotti.setIdentificatoreUtilizzatore(x)
            uiAggiungiPrenotazioni.setIdentificatoreUtilizzatore(x)




        finestraLogin.close()
        finestraHome.show()

        uiHome.ButtonDipendenti.clicked.connect(onClickButtonPersonale)
        uiHome.ButtonFidelity.clicked.connect(onClickButtonFidelity)
        uiHome.ButtoOrdini.clicked.connect(onClickButtonOrdini)
        uiHome.ButtonMagazzino.clicked.connect(onClickButtonMagazzino)
        uiHome.ButtonScontrini.clicked.connect(onClickButtonScontrini)
        uiHome.ButtonDipendenti.clicked.connect(onClickButtonPersonale)
        uiHome.ButtonProdotti.clicked.connect(onClickButtonProdotti)
        uiHome.ButtonHome.clicked.connect(onClickButtonLogout)
        uiHome.ButtonPrenotazioni.clicked.connect(onClickButtonPrenotazioni)
        uiHome.ButtonStatistiche.clicked.connect(onClickButtonStatistiche)

def onClickButtonStatistiche():
    finestraHome.hide()
    finestraStatistiche.show()
    uiStatistiche.ButtonHome.clicked.connect(onClickButtonHomeStatistiche)

def onClickButtonHomeStatistiche():
    finestraStatistiche.hide()
    finestraHome.show()


def onClickButtonLogout():
    uiLogin.lEmail.setText('')
    uiLogin.lEpassword.setText('')
    finestraHome.hide()
    finestraLogin.show()

def onClickButtonPrenotazioni():
    finestraHome.hide()
    uiPrenotazioni.caricaDatiPrenotazioni()
    finestraPrenotazioni.show()
    uiPrenotazioni.ButtonHome.clicked.connect(onClickButtonHomePrenotazioni)
    uiPrenotazioni.ButtonAggiungiPrenotazioni.clicked.connect(onClickButtonAggiungiPrenotazioni)

def onClickButtonAggiungiPrenotazioni():
    finestraPrenotazioni.hide()
    finestraAggiungiPrenotazioni.show()
    uiAggiungiPrenotazioni.ButtonConferma.clicked.connect(onClickButtonConfermaPrenotazione)
    uiAggiungiPrenotazioni.ButtonAnnulla.clicked.connect(onClickButtonAnnullaPrenotazione)

def onClickButtonConfermaPrenotazione():
    uiAggiungiPrenotazioni.creaNuovaPrenotazione()
    finestraAggiungiPrenotazioni.hide()
    uiPrenotazioni.caricaDatiPrenotazioni()
    finestraPrenotazioni.show()

def onClickButtonAnnullaPrenotazione():
    finestraAggiungiPrenotazioni.hide()
    finestraPrenotazioni.show()

def onClickButtonHomePrenotazioni():
    finestraPrenotazioni.hide()
    finestraHome.show()

def onClickButtonProdotti():
    finestraHome.hide()
    uiProdotti.caricaDatiProdotti()
    finestraProdotti.show()
    uiProdotti.ButtonHome.clicked.connect(onClickButtonHomeProdotti)
    uiProdotti.ButtonAggiungiSconto.clicked.connect(onClickButtonAggiungiSconto)

def onClickButtonAggiungiSconto():
    if uiProdotti.controllaPermessiUtilizzatore():
        finestraProdotti.hide()
        finestraAggiungiSconti.show()
    else:
        finestraProdotti.hide()
        finestraErrore.show()

    uiAggiungiSconti.ButtonAnnullaSconto.clicked.connect(onClickButtonAnnullaSconto)
    uiAggiungiSconti.ButtonConfermaSconto.clicked.connect(onClickButtonConfermaSconto)
    uiErrore.ButtonIndietro.clicked.connect(onClickButtonIndietroErrore)

def onClickButtonAnnullaSconto():
    finestraAggiungiSconti.hide()
    finestraProdotti.show()

def onClickButtonConfermaSconto():
    uiAggiungiSconti.creaSconto()
    finestraAggiungiSconti.hide()
    finestraProdotti.show()

def onClickButtonHomeProdotti():
    finestraProdotti.hide()
    finestraHome.show()

def onClickButtonMagazzino():
    finestraHome.hide()
    uiMagazzino.caricaDatiMagazzino()
    finestraMagazzino.show()
    uiMagazzino.ButtonHome.clicked.connect(onClickButtonHomeMagazzino)

def onClickButtonHomeMagazzino():
    finestraMagazzino.hide()
    finestraHome.show()

def onClickButtonPersonale():
    if uiPersonale.controllaPermessiUtilizzatore():
        finestraHome.hide()
        finestraPersonale.show()
        uiPersonale.ButtonAggiungiPersonale.clicked.connect(onClickButtonAggiungiPersonale)
        uiPersonale.ButtonRimuoviPersonale.clicked.connect(onClickButtonRimuoviPersonale)
        uiPersonale.ButtonModificaPermessi.clicked.connect(onClickButtonModificaPermessi)
    else:
        finestraHome.hide()
        finestraErrore.show()
    uiPersonale.ButtonHomePersonale.clicked.connect(onClickButtonHomePersonale)
    uiErrore.ButtonIndietro.clicked.connect(onClickButtonIndietroErrore)

def onClickButtonModificaPermessi():
    finestraPersonale.hide()
    finestraModificaPermessi.show()
    uiModificaPermessi.ButtonConfermaModifica.clicked.connect(onClickButtonConfermaModificaPermessi)
    uiModificaPermessi.ButtonAnnullaModifica.clicked.connect(onClickButtonAnnullaModificaPermessi)

def onClickButtonConfermaModificaPermessi():
    finestraModificaPermessi.hide()
    uiPersonale.caricaDatiPersonale()
    finestraPersonale.show()

def onClickButtonAnnullaModificaPermessi():
    finestraModificaPermessi.hide()
    finestraPersonale.show()


def onClickButtonRimuoviPersonale():
    finestraPersonale.hide()
    finestraRimuoviPersonale.show()
    uiRimuoviPersonale.ButtonAnnullaModificaPersonale.clicked.connect(onClickButtonAnnullaRimozionePersonale)
    uiRimuoviPersonale.ButtonConfermaModificaOrdine.clicked.connect(onClickButtonConfermaRimozionePersonale)

def onClickButtonAnnullaRimozionePersonale():
    finestraRimuoviPersonale.hide()
    finestraPersonale.show()

def onClickButtonConfermaRimozionePersonale():
    uiRimuoviPersonale.rimuoviPersonale()
    uiPersonale.caricaDatiPersonale()
    finestraRimuoviPersonale.hide()
    finestraPersonale.show()

def onClickButtonAggiungiPersonale():
    finestraPersonale.hide()
    finestraAggiungiPersonale.show()
    uiAggiungiPersonale.buttonConfermaInserimento.clicked.connect(onClickButtonConfermaPersonale)
    uiAggiungiPersonale.pushButton_2.clicked.connect(onClickButtonAnnullaPersonale)

def onClickButtonConfermaPersonale():
    uiPersonale.caricaDatiPersonale()
    finestraAggiungiPersonale.hide()
    finestraPersonale.show()

def onClickButtonAnnullaPersonale():
    finestraAggiungiPersonale.hide()
    finestraPersonale.show()


def onClickButtonHomePersonale():
    finestraPersonale.hide()
    finestraHome.show()

def onClickButtonIndietroErrore():
    finestraErrore.hide()
    finestraHome.show()

def onClickButtonFidelity():
    finestraHome.hide()
    uiFidelity.caricaDatiFidelity()
    finestraFidelity.show()
    uiFidelity.ButtonAggiungi.clicked.connect(onclickButtonAggiungiFidelity)
    uiFidelity.ButtonHome.clicked.connect(onClickButtonHomeFidelity)

def onClickButtonHomeFidelity():
    finestraFidelity.hide()
    finestraHome.show()

def onclickButtonAggiungiFidelity():
    finestraAggiungiFidelityCard.show()
    uiAggiungiFidelityCard.creaNuovaFidelity()


def onClickButtonOrdini():
    finestraHome.hide()
    uiOrdini.caricaDatiOrdine()
    finestraOrdini.show()
    uiOrdini.ButtonHome.clicked.connect(onClickButtonHomeOrdini)
    uiOrdini.ButtonAggiungi.clicked.connect(onClickButtonAggiungiOrdine)
    uiOrdini.ButtonModifica.clicked.connect(onClickButtonModificaStatoOrdine)

def onClickButtonModificaStatoOrdine():
    finestraOrdini.hide()
    finestraModificaStatoOrdine.show()
    uiModificaStatoOrdine.ButtonConfermaModificaOrdine.clicked.connect(onClickButtonConfermaModifiche)
    uiModificaStatoOrdine.ButtonAnnullaModificaOrdine.clicked.connect(onCLickButtonAnnullaModifiche)

def onCLickButtonAnnullaModifiche():
    finestraModificaStatoOrdine.hide()
    finestraOrdini.show()
def onClickButtonConfermaModifiche():
    uiModificaStatoOrdine.modificaStatoOrdine()
    uiOrdini.caricaDatiOrdine()
    finestraModificaStatoOrdine.hide()
    finestraOrdini.show()

def onClickButtonAggiungiOrdine():
    uiAggiungiOrdine.creaNuovoOrdine()
    finestraOrdini.hide()
    finestraAggiungiOrdine.show()

    uiAggiungiOrdine.ButtonAnnullaOrdine.clicked.connect(onClickButtonAnnullaOrdine)
    uiAggiungiOrdine.ButtonConfermaOrdine.clicked.connect(onClickButtonConfermaOrdine)

def onClickButtonAnnullaOrdine():
    uiAggiungiOrdine.annullaOrdine()
    finestraAggiungiOrdine.hide()
    uiOrdini.caricaDatiOrdine()
    finestraOrdini.show()

def onClickButtonConfermaOrdine():
    finestraAggiungiOrdine.hide()
    uiAggiungiOrdine.cancellaDatiPrecendeti()
    uiOrdini.caricaDatiOrdine()
    finestraOrdini.show()

def onClickButtonHomeOrdini():
    finestraOrdini.hide()
    finestraHome.show()

def onClickButtonScontrini():
    finestraHome.hide()
    uiScontrino.caricaDatiScontrini()
    finestraScontrini.show()
    uiScontrino.ButtonHome.clicked.connect(onClickButtonHomeScontrini)
    uiScontrino.ButtonAggiungiScontrini.clicked.connect(onClickButtonAggiungiScontrini)

def onClickButtonAggiungiScontrini():
    uiAggiungiScontrino.creaNuovoScontrino()
    finestraScontrini.hide()
    finestraAggiungiScontrino.show()
    uiAggiungiScontrino.ButtonConfermaScontrino.clicked.connect(onClickButtonConfermaScontrino)
    uiAggiungiScontrino.ButtonAnnullaScontrino.clicked.connect(onClickButtonAnnullaScontrino)

def onClickButtonConfermaScontrino():
    finestraAggiungiScontrino.hide()
    uiAggiungiScontrino.confermaScontrino()
    uiScontrino.caricaDatiScontrini()
    finestraScontrini.show()

def onClickButtonAnnullaScontrino():
    uiAggiungiScontrino.annullaScontrino()
    finestraAggiungiScontrino.hide()
    uiScontrino.caricaDatiScontrini()
    finestraScontrini.show()

def onClickButtonHomeScontrini():
    finestraScontrini.hide()
    finestraHome.show()



app = QApplication([])  //import di PyQt 
finestraLogin = QWidget()
uiLogin = Ui_Login()
uiLogin.setupUi(finestraLogin)
finestraLogin.show()
uiLogin.buttonLogin.clicked.connect(controlla)

app2 = QApplication([])
finestraHome = QWidget()
uiHome = Ui_HomePage()
uiHome.setupUi(finestraHome)
finestraHome.hide()

app3 = QApplication([])
finestraFidelity = QWidget()
uiFidelity = Ui_PaginaFidelity()
uiFidelity.setupUi(finestraFidelity)
finestraFidelity.hide()

appAggiungiFidelity = QApplication([])
finestraAggiungiFidelityCard = QWidget()
uiAggiungiFidelityCard = Ui_AggiungiFidelity()
uiAggiungiFidelityCard.setupUi(finestraAggiungiFidelityCard)
finestraAggiungiFidelityCard.hide()

appOrdini = QApplication([])
finestraOrdini = QWidget()
uiOrdini = Ui_PaginaOrdini()
uiOrdini.setupUi(finestraOrdini)

appPersonale = QApplication([])
finestraPersonale = QWidget()
uiPersonale = Ui_PaginaPersonale()
uiPersonale.setupUi(finestraPersonale)

appAggiungiOrdine = QApplication([])
finestraAggiungiOrdine = QWidget()
uiAggiungiOrdine = Ui_PaginaAggiungiOrdini()
uiAggiungiOrdine.setupUi(finestraAggiungiOrdine)

appModificaStatoOrdine = QApplication([])
finestraModificaStatoOrdine = QWidget()
uiModificaStatoOrdine = Ui_PaginaModificaStatoOrdini()
uiModificaStatoOrdine.setupUi(finestraModificaStatoOrdine)

appMagazzino = QApplication([])
finestraMagazzino = QWidget()
uiMagazzino = Ui_PaginaMagazzino()
uiMagazzino.setupUi(finestraMagazzino)

appScontrini = QApplication([])
finestraScontrini = QWidget()
uiScontrino = Ui_PaginaScontrini()
uiScontrino.setupUi(finestraScontrini)

appAggiungiScontrino = QApplication([])
finestraAggiungiScontrino = QWidget()
uiAggiungiScontrino = Ui_PaginaAggiungiScontrini()
uiAggiungiScontrino.setupUi(finestraAggiungiScontrino)

appErrore = QApplication([])
finestraErrore = QWidget()
uiErrore = Ui_Errore()
uiErrore.setupUi(finestraErrore)

appProdotti = QApplication([])
finestraProdotti = QWidget()
uiProdotti = Ui_PaginaProdotti()
uiProdotti.setupUi(finestraProdotti)

appAggiungiSconti = QApplication([])
finestraAggiungiSconti = QWidget()
uiAggiungiSconti = Ui_PaginaAggiungiSconti()
uiAggiungiSconti.setupUi(finestraAggiungiSconti)

appPrenotazioni = QApplication([])
finestraPrenotazioni = QWidget()
uiPrenotazioni = Ui_PaginaPrenotazioni()
uiPrenotazioni.setupUi(finestraPrenotazioni)

appAggiungiPrenotazioni = QApplication([])
finestraAggiungiPrenotazioni = QWidget()
uiAggiungiPrenotazioni = Ui_AggiungiPrenotazione()
uiAggiungiPrenotazioni.setupUi(finestraAggiungiPrenotazioni)

appStatistiche = QApplication([])
finestraStatistiche = QWidget()
uiStatistiche = Ui_Statistiche()
uiStatistiche.setupUi(finestraStatistiche)

appAggiungiPersonale = QApplication([])
finestraAggiungiPersonale = QWidget()
uiAggiungiPersonale = Ui_AggiungiPersonale()
uiAggiungiPersonale.setupUi(finestraAggiungiPersonale)

appRimuoviPersonale = QApplication([])
finestraRimuoviPersonale = QWidget()
uiRimuoviPersonale = Ui_PaginaRimuoviDipendenti()
uiRimuoviPersonale.setupUi(finestraRimuoviPersonale)

appModificaPermessi = QApplication([])
finestraModificaPermessi = QWidget()
uiModificaPermessi = Ui_PaginaModificaPermessi()
uiModificaPermessi.setupUi(finestraModificaPermessi)

app.exec_()
app2.exec_()
app3.exec_()
appAggiungiFidelity.exec_()
appOrdini.exec_()
appPersonale.exec_()
appAggiungiOrdine.exec_()
appModificaStatoOrdine.exec_()
appMagazzino.exec_()
appScontrini.exec_()
appAggiungiScontrino.exec_()
appErrore.exec_()
appProdotti.exec_()
appAggiungiSconti.exec_()
appPrenotazioni.exec_()
appAggiungiPrenotazioni.exec_()
