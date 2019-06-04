# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trivia.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
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

class Ui_MainWindow(QtGui.QMainWindow):
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
        self.scrollArea.setGeometry(QtCore.QRect(100, 70, 691, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 689, 259))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(110, 340, 691, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(40, 30, 117, 29))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(440, 20, 117, 29))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 80, 117, 29))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(440, 80, 117, 29))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 31, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 31, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 31, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(420, 80, 31, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(690, 10, 194, 35))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(23, 12, 91, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 520, 701, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAdmin = QtGui.QMenu(self.menubar)
        self.menuAdmin.setObjectName(_fromUtf8("menuAdmin"))
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
        self.menuAdmin.addAction(self.actionEdit_questions)
        self.menuAdmin.addSeparator()
        self.menuAdmin.addAction(self.actionSave_edit)
        self.menuApp.addAction(self.actionExit)
        self.menubar.addAction(self.menuApp.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scrollArea, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton_3)
        MainWindow.setTabOrder(self.radioButton_3, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.dateTimeEdit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "--- Code Trivia ---", None))
        self.groupBox.setTitle(_translate("MainWindow", "Answers", None))
        self.radioButton.setText(_translate("MainWindow", "RadioButton", None))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton", None))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton", None))
        self.radioButton_4.setText(_translate("MainWindow", "RadioButton", None))
        self.label.setText(_translate("MainWindow", "a.", None))
        self.label_2.setText(_translate("MainWindow", "b.", None))
        self.label_3.setText(_translate("MainWindow", "c.", None))
        self.label_4.setText(_translate("MainWindow", "d.", None))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin", None))
        self.menuApp.setTitle(_translate("MainWindow", "App", None))
        self.actionEdit_questions.setText(_translate("MainWindow", "Edit questions", None))
        self.actionEdit_questions.setStatusTip(_translate("MainWindow", "application Admin only", None))
        self.actionEdit_questions.triggered.connect(self.edit_questions)
        self.actionSave_edit.setText(_translate("MainWindow", "Save edit", None))
        self.actionSave_edit.setStatusTip(_translate("MainWindow", "application Admin only", None))
        self.actionSave_edit.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSave_edit.triggered.connect(self.Save_edit)
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the application", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionExit.triggered.connect(self.close_application)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Exit application',
                                            "Are you sure you want to exit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        # save score to leaderboard

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def edit_questions(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open Editor')
        file = open(name, 'r')
        self.editor()
        with file:
            text = file.read()
            self.textEdit.setText(text)

    def Save_edit(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'save Edit')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()    