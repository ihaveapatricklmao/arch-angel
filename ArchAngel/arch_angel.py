import json
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

print("starting browser...")

bookmark_file = 'bookmark.json'

application = QApplication(sys.argv)
app_icon = QSystemTrayIcon(QIcon('fatratbeinggrabbed.png'), parent=application)
app_icon.show()

#browser icons

class WebBrowser(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(WebBrowser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("ArchAngel")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        #url
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(40)

        #tab
        self.tab_btn = QPushButton("+")
        self.tab_btn.setMinimumHeight(40)

        #go
        self.go_btn = QPushButton("Enter")
        self.go_btn.setMinimumHeight(40)

       #reload
        self.reload_btn = QPushButton("Reload")
        self.reload_btn.setMinimumHeight(40)

        #back
        self.back_btn = QPushButton("<-")
        self.back_btn.setMinimumHeight(40)

        #forward
        self.forward_btn = QPushButton("->")
        self.forward_btn.setMinimumHeight(40)

        #bookmark
        self.bookmark_btn = QPushButton("[ ]")
        self.bookmark_btn.setMinimumHeight(40)

        self.home_btn = QPushButton("Home")
        self.home_btn.setMinimumHeight(40)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.tab_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.bookmark_btn)
        self.horizontal.addWidget(self.home_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)
        self.home_btn.clicked.connect(self.home_tp)
        ##self.tab_btn.clicked.connect(self.browser.addTab)
        ##self.bookmark_btn.clicked.connect(self.browser.bookmark)


        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://search.brave.com/"))

        self.window.setLayout(self.layout)
        self.window.show()
    def home_tp(self):
        self.browser.setUrl(QUrl("https://search.brave.com/"))
        
    def navigate(self, url):
        if  not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = WebBrowser()
app.exec_()
