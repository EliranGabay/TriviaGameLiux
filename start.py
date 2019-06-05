#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
import game
import sql

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(596, 349)
        Dialog.setMinimumSize(QtCore.QSize(596, 0))
        Dialog.setMaximumSize(QtCore.QSize(596, 349))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("brainstorm.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 284, 306))
        self.scrollAreaWidgetContents.setObjectName(
            _fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(
            QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(
            1, QtGui.QFormLayout.LabelRole, self.lineEdit)
        spacerItem = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(
            3, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(
            9, QtGui.QFormLayout.LabelRole, self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtGui.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtGui.QFormLayout.LabelRole, spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtGui.QFormLayout.LabelRole, spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(
            20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem4)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.pushButton.clicked.connect(self.start_game)
        self.pushButton_2.clicked.connect(
            QtCore.QCoreApplication.instance().quit)
        self.retranslateUi(Dialog)

        Dialog.setTabOrder(self.lineEdit, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.scrollArea)
        Dialog.setTabOrder(self.scrollArea, self.pushButton_2)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate(
            "Dialog", "--- Code Trivia ---", None))
        self.label_2.setText(_translate("Dialog", "Leaderboard", None))
        self.label.setText(_translate("Dialog", "Enter your name", None))
        self.pushButton.setText(_translate("Dialog", "START A GAME", None))
        self.pushButton_2.setText(_translate("Dialog", "Exit", None))

    def leader_board(self):
        self.scores = sql.getAllScore()
        cnt = 0
        textEdit = QtGui.QTextEdit()
        self.scrollArea.setWidget(textEdit)
        textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        text = "No | NAME\t\t| SCORE"
        textEdit.setText(text)
        text = "-----------------------------------------------------------"
        textEdit.append(text)
        for s in self.scores:
            text = str(cnt)+"    |  "+s[0] + "\t\t|" + str(s[1])
            textEdit.append(text)
            cnt += 1

    def start_game(self):
        player = [self.lineEdit.text(), 0]
        Dialog.hide()
        self.MainWindow = QtGui.QMainWindow()
        self.ui = game.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.setPlayer(player)
        self.ui.get_questions()
        self.ui.addqs(1)
        self.MainWindow.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.leader_board()
    sys.exit(app.exec_())
