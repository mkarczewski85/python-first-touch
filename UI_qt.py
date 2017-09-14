# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:04:49 2017

@author: Maciej
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, pyqtSlot  



class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip('<b>Wcinij przycisk!</b>')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Okienko z przyciskiem')
        self.statusBar()
    
        btn = QPushButton('Przycisk', self)
        btn.clicked.connect(self.buttonClicked)
        btn.setToolTip('<b>Wcisnij mnie!</b>')
        btn.resize(btn.sizeHint())
        btn.move(80, 80)
        
        textbox = QLineEdit(self)
        textbox.move(20, 20)
        textbox.resize(200,30)
        textbox.setText('Test')
        self.show()
    
    def buttonClicked(self):
        
        self.statusBar().showMessage('Wcisnales mnie!')
        QMessageBox.information(self, 'Info', 'To jest informacja', QMessageBox.Ok)
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Pytanie',
            "Czy jestes pewien?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept(QCoreApplication.instance().quit)
        else:
            event.ignore()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())