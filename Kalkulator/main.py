import sys
from PyQt6.QtWidgets import QDialog, QApplication
from layout import *


potrzeby = [
    [1700, 1900, 2100],    #kobieta
    [1900, 2200, 2500]     #menzczyzna
]


daniaArray = []

class MyForm(QDialog):
    def addToList(self):

        if not self.ui.kalorieInp.text().isdigit() or self.ui.danieInp.text().isspace() or self.ui.danieInp.text() == "":
            return

        danie = self.ui.danieInp.text()
        kalorie = int(self.ui.kalorieInp.text())

        daniaArray.append([danie, kalorie])

        self.ui.listWidget.addItem(danie + " " + str(kalorie))

        allKalorie = 0

        for i in range(len(daniaArray)):
            allKalorie += daniaArray[i][1]

        self.ui.sumaOut.setText(str(allKalorie))
        
        self.checked(allKalorie)


    def checked(self, kal):

        plec = -1
        aktywnosc = -1

        if self.ui.kobietaRadio.isChecked():
            plec = 0
        if self.ui.mezczyznaRadio.isChecked():
            plec = 1

        if self.ui.mAktRadio.isChecked():
           aktywnosc = 0
        if self.ui.sAktRadio.isChecked():
           aktywnosc = 1
        if self.ui.dAktRadio.isChecked():
           aktywnosc = 2

        potrzebaProc = (kal / potrzeby[plec][aktywnosc]) * 100
        print(kal)

        if(potrzebaProc < 80):
            self.ui.sumaOut.setStyleSheet("background-color: yellow;")
        if(potrzebaProc >= 80 and potrzebaProc <= 100):
            self.ui.sumaOut.setStyleSheet("background-color: green;")  
        if(potrzebaProc > 100):
            self.ui.sumaOut.setStyleSheet("background-color: red;")
        return
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.dodajButton.clicked.connect(self.addToList)
        self.ui.pushButton.clicked.connect(self.checked)
        self.show()
        print()

        #self.ui.listView.ad


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())