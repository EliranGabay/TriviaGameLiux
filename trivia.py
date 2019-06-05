# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trivia.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(911, 645)
        MainWindow.setMinimumSize(QtCore.QSize(911, 645))
        MainWindow.setMaximumSize(QtCore.QSize(911, 645))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("brainstorm.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 70, 851, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 849, 259))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 350, 851, 231))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.ansA = QtGui.QRadioButton(self.groupBox)
        self.ansA.setGeometry(QtCore.QRect(90, 30, 521, 29))
        self.ansA.setText(_fromUtf8(""))
        self.ansA.setObjectName(_fromUtf8("ansA"))
        self.ansC = QtGui.QRadioButton(self.groupBox)
        self.ansC.setGeometry(QtCore.QRect(90, 130, 521, 29))
        self.ansC.setText(_fromUtf8(""))
        self.ansC.setObjectName(_fromUtf8("ansC"))
        self.ansB = QtGui.QRadioButton(self.groupBox)
        self.ansB.setGeometry(QtCore.QRect(90, 80, 521, 29))
        self.ansB.setText(_fromUtf8(""))
        self.ansB.setObjectName(_fromUtf8("ansB"))
        self.ansD = QtGui.QRadioButton(self.groupBox)
        self.ansD.setGeometry(QtCore.QRect(90, 180, 521, 29))
        self.ansD.setText(_fromUtf8(""))
        self.ansD.setObjectName(_fromUtf8("ansD"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 30, 31, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 31, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 31, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 31, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.submit = QtGui.QPushButton(self.groupBox)
        self.submit.setGeometry(QtCore.QRect(650, 130, 191, 91))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(23, 12, 91, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(180, 20, 701, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuApp = QtGui.QMenu(self.menubar)
        self.menuApp.setObjectName(_fromUtf8("menuApp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit_questions = QtGui.QAction(MainWindow)
        self.actionEdit_questions.setObjectName(_fromUtf8("actionEdit_questions"))
        self.actionSave_edit = QtGui.QAction(MainWindow)
        self.actionSave_edit.setObjectName(_fromUtf8("actionSave_edit"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNew_Game = QtGui.QAction(MainWindow)
        self.actionNew_Game.setObjectName(_fromUtf8("actionNew_Game"))
        self.menuApp.addAction(self.actionNew_Game)
        self.menuApp.addSeparator()
        self.menuApp.addAction(self.actionExit)
        self.menubar.addAction(self.menuApp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scrollArea, self.ansA)
        MainWindow.setTabOrder(self.ansA, self.ansC)
        MainWindow.setTabOrder(self.ansC, self.ansB)
        MainWindow.setTabOrder(self.ansB, self.ansD)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "--- Code Trivia ---", None))
        self.groupBox.setTitle(_translate("MainWindow", "Answers", None))
        self.label.setText(_translate("MainWindow", "a.", None))
        self.label_2.setText(_translate("MainWindow", "b.", None))
        self.label_3.setText(_translate("MainWindow", "c.", None))
        self.label_4.setText(_translate("MainWindow", "d.", None))
        self.submit.setText(_translate("MainWindow", "Submit Answer", None))
        self.menuApp.setTitle(_translate("MainWindow", "App", None))
        self.actionEdit_questions.setText(_translate("MainWindow", "Edit questions", None))
        self.actionEdit_questions.setStatusTip(_translate("MainWindow", "application Admin only", None))
        self.actionSave_edit.setText(_translate("MainWindow", "Save edit", None))
        self.actionSave_edit.setStatusTip(_translate("MainWindow", "application Admin only", None))
        self.actionSave_edit.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the application", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game", None))

