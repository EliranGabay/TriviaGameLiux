#!/usr/bin/python3
import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 900, 600)
        self.setWindowTitle("--- Code Trivia ---")
        self.setWindowIcon(QtGui.QIcon('brainstorm.png'))
        extractAction = QtGui.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Exit the application")
        extractAction.triggered.connect(self.close_application)

        EditQuestions = QtGui.QAction("&Edit Questions", self)
        EditQuestions.setStatusTip("application Admin only")
        EditQuestions.triggered.connect(self.edit_questions)

        SaveEdit = QtGui.QAction("&Save Edit", self)
        SaveEdit.setShortcut("Ctrl+S")
        SaveEdit.setStatusTip("application Admin only")
        SaveEdit.triggered.connect(self.Save_edit)

        self.statusBar()

        mainMenu = self.menuBar()
        AppMenu = mainMenu.addMenu('&App')
        AppMenu.addAction(extractAction)

        AdminMenu = mainMenu.addMenu('&Admin')
        AdminMenu.addAction(EditQuestions)
        AdminMenu.addAction(SaveEdit)

        self.home()

    def home(self):
        self.show()

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


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
# <div>Icons made by <a href="https://www.flaticon.com/authors/popcorns-arts" title="Icon Pond">Icon Pond</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
