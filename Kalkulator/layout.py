# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(322, 503)
        self.dodajButton = QtWidgets.QPushButton(parent=Dialog)
        self.dodajButton.setGeometry(QtCore.QRect(210, 10, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dodajButton.setFont(font)
        self.dodajButton.setStyleSheet("background-color: lightgreen;\n"
"")
        self.dodajButton.setObjectName("dodajButton")
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(10, 290, 301, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 440, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 10, 201, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: darkgreen;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.danieInp = QtWidgets.QLineEdit(parent=self.widget)
        self.danieInp.setObjectName("danieInp")
        self.horizontalLayout.addWidget(self.danieInp)
        self.widget1 = QtWidgets.QWidget(parent=Dialog)
        self.widget1.setGeometry(QtCore.QRect(0, 40, 201, 24))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: darkgreen;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.kalorieInp = QtWidgets.QLineEdit(parent=self.widget1)
        self.kalorieInp.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.kalorieInp.setObjectName("kalorieInp")
        self.horizontalLayout_2.addWidget(self.kalorieInp)
        self.widget2 = QtWidgets.QWidget(parent=Dialog)
        self.widget2.setGeometry(QtCore.QRect(10, 310, 97, 49))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.kobietaRadio = QtWidgets.QRadioButton(parent=self.widget2)
        self.kobietaRadio.setObjectName("kobietaRadio")
        self.verticalLayout_2.addWidget(self.kobietaRadio)
        self.mezczyznaRadio = QtWidgets.QRadioButton(parent=self.widget2)
        self.mezczyznaRadio.setObjectName("mezczyznaRadio")
        self.verticalLayout_2.addWidget(self.mezczyznaRadio)
        self.widget3 = QtWidgets.QWidget(parent=Dialog)
        self.widget3.setGeometry(QtCore.QRect(10, 390, 183, 76))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mAktRadio = QtWidgets.QRadioButton(parent=self.widget3)
        self.mAktRadio.setObjectName("mAktRadio")
        self.verticalLayout_3.addWidget(self.mAktRadio)
        self.sAktRadio = QtWidgets.QRadioButton(parent=self.widget3)
        self.sAktRadio.setObjectName("sAktRadio")
        self.verticalLayout_3.addWidget(self.sAktRadio)
        self.dAktRadio = QtWidgets.QRadioButton(parent=self.widget3)
        self.dAktRadio.setObjectName("dAktRadio")
        self.verticalLayout_3.addWidget(self.dAktRadio)
        self.widget4 = QtWidgets.QWidget(parent=Dialog)
        self.widget4.setGeometry(QtCore.QRect(10, 70, 301, 217))
        self.widget4.setObjectName("widget4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(parent=self.widget4)
        self.listWidget.setEnabled(True)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.suma = QtWidgets.QLabel(parent=self.widget4)
        self.suma.setStyleSheet("background-color: green;\n"
"color: white;")
        self.suma.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.suma.setObjectName("suma")
        self.verticalLayout.addWidget(self.suma)
        self.sumaOut = QtWidgets.QLabel(parent=self.widget4)
        self.sumaOut.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sumaOut.setObjectName("sumaOut")
        self.verticalLayout.addWidget(self.sumaOut)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kalkulator kalorii"))
        self.dodajButton.setText(_translate("Dialog", "Dodaj"))
        self.pushButton.setText(_translate("Dialog", "oblicz"))
        self.label.setText(_translate("Dialog", "Posiłek"))
        self.label_2.setText(_translate("Dialog", "Kalorie"))
        self.kobietaRadio.setText(_translate("Dialog", "kobieta"))
        self.mezczyznaRadio.setText(_translate("Dialog", "mężczyzna"))
        self.mAktRadio.setText(_translate("Dialog", "mała aktywność fizyczna"))
        self.sAktRadio.setText(_translate("Dialog", "średnia aktywność fizyczna"))
        self.dAktRadio.setText(_translate("Dialog", "duża aktywność fizyczna"))
        self.suma.setText(_translate("Dialog", "suma spożytych kalorii"))
        self.sumaOut.setText(_translate("Dialog", "0"))
