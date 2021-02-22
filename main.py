from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        HEIGHT=450
        WIDTH=700
        
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        
        self.setWindowIcon(QtGui.QIcon('logo.png')) 
        self.setMinimumWidth(WIDTH)
        self.setMinimumHeight(HEIGHT)
        self.showMaximized()

        #navbar
        navbar=QToolBar()
        self.addToolBar(navbar)

        #back btn
        backBtn=QAction('<-Back', self)
        backBtn.triggered.connect(self.browser.back)
        navbar.addAction(backBtn)

        #forward btn
        forwardBtn=QAction('Next->', self)
        forwardBtn.triggered.connect(self.browser.forward)
        navbar.addAction(forwardBtn)

        #Reload btn
        reloadBtn=QAction('Reload', self)
        reloadBtn.triggered.connect(self.browser.reload)
        navbar.addAction(reloadBtn)

        #home btn
        homeBtn=QAction('Home',self)
        homeBtn.triggered.connect(self.navigate_home)
        navbar.addAction(homeBtn)

        #url bar
        self.url_bar=QLineEdit()
        self.url_bar.setPlaceholderText("URL: ")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        #search bar
        self.search_bar=QLineEdit()
        self.search_bar.setPlaceholderText("Search to google ")
        self.search_bar.returnPressed.connect(self.navigate_to_search)
        navbar.addWidget(self.search_bar)


    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    
    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    
    def update_url(self, u):
        self.url_bar.setText(u.toString())
    
    def navigate_to_search(self):
        url=self.search_bar.text()
        self.browser.setUrl(QUrl("https://www.google.com/search?q="+url))


app=QApplication(sys.argv)
QApplication.setApplicationName("Simple Web Browser")
window=MainWindow()

app.exec_()