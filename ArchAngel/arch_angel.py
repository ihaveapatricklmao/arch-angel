import json
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

print("starting browser...")


class WebBrowser(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(WebBrowser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("ArchAngel")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(40)

        self.tab_btn = QPushButton("+")
        self.tab_btn.setMinimumHeight(40)

        self.go_btn = QPushButton("Enter")
        self.go_btn.setMinimumHeight(40)

        self.back_btn = QPushButton("<-")
        self.back_btn.setMinimumHeight(40)

        self.forward_btn = QPushButton("->")
        self.forward_btn.setMinimumHeight(40)

        self.bookmark_btn = QPushButton("[ ]")
        self.bookmark_btn.setMinimumHeight(40)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.tab_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.bookmark_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        ##self.tab_btn.clicked.connect(self.browser.addTab)
        ##self.bookmark_btn.clicked.connect(self.browser.bookmark)


        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://search.brave.com/"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if  not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = WebBrowser()
app.exec_()
