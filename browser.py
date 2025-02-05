
# importing required libraries 
from os import path
from PyQt5 import QtCore, QtWidgets, QtWebEngineCore, QtWebEngineWidgets
from PyQt5.QtCore import * 

from PyQt5.QtWidgets import * 

from PyQt5.QtGui import * 


from PyQt5.QtWebEngineWidgets import * 

from PyQt5.QtPrintSupport import * 
from threading import Thread
import os 
import time
import sys
import requests
import urllib
from urllib import request
from adblockparser import AdblockRules

with open("easylist.txt") as f:
    raw_rules = f.readlines()
    rules = AdblockRules(raw_rules)
# main window 
global pot
class GeeksforGeeks(QWidget):
 
    def __init__(self):
        super().__init__()
        self.resize(250,60)
 
        # calling a defined method to initialize UI
        # creating progress bar
        self.progressBar = QProgressBar(self)
 
        # setting its size
        self.progressBar.setGeometry(25, 45, 210, 30)
        self.button = QPushButton('Start download', self)
 
        # assigning position to button
        self.button.move(50, 100)
 
        # assigning activity to push button
        self.button.clicked.connect(self.Download)
        # creating push button to start download
        self.setGeometry(310, 310, 280, 170)
        self.setWindowTitle("download")
 
        # assigning activity to push butt
 
        # setting window geometry
        
 
        # setting window action
        
 
        
 
    # when push button is pressed, this method is called
    def Handle_Progress(self, blocknum, blocksize, totalsize):
 
        ## calculate the progress
        readed_data = blocknum * blocksize
 
        if totalsize > 0:
            download_percentage = int(round(readed_data * 100 / totalsize))
            self.progressBar.setValue(download_percentage)
            print('Whatsup')
            QApplication.processEvents()
            print('what is down')
 
    # method to download any file using urllib
    def Download(self):
        global pot
        # specify the url of the file which is to be downloaded
        
        down_url = pot # specify download url here
        q = pot.split('/')
        exte = []
        # specify save location where the file is to be saved
        basepath = os.getcwd().replace('\\','/')
        path_arr = basepath.split("/")
        path_arr2 = path_arr[0,2]
        save_loc = path_arr2.join("/")+"/Downloads/" + q[-1].split('?')[0]
         
        # Downloading using urllib
        urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)
        print('zip line')
 
class WebEngineUrlRequestInterceptor(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if rules.should_block(url):
            print("block::::::::::::::::::::::", url)
            info.block(True)

class MainWindow(QMainWindow): 


    # constructor 

    def __init__(self, *args, **kwargs): 

        super(MainWindow, self).__init__(*args, **kwargs) 

  

        # creating a tab widget 

        self.tabs = QTabWidget() 
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QIcon('images/Xbrowser.png'))

  

        # making document mode true

        self.tabs.setDocumentMode(True) 

  

        # adding action when double clicked 

        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick) 

  

        # adding action when tab is changed 

        self.tabs.currentChanged.connect(self.current_tab_changed) 

        # making tabs closeable 

        self.tabs.setTabsClosable(True) 

  

        # adding action when tab close is requested 

        self.tabs.tabCloseRequested.connect(self.close_current_tab) 

  

        # making tabs as central widget 

        self.setCentralWidget(self.tabs) 

  

        # creating a status bar 

        self.status = QStatusBar() 

  

        # setting status bar to the main window 

        self.setStatusBar(self.status) 
        

  

        # creating a tool bar for navigation 

        navtb = QToolBar("Navigation") 

  

        # adding tool bar tot he main window 

        self.addToolBar(navtb)# setting status tip 
        back_btn = QAction("Back", self)
        back_btn.setIcon(QIcon('images/left-arrow.png'))

        back_btn.setStatusTip("Back to previous page") 
        self.basepath = os.getcwd().replace('\\','/')

  

        # adding action to back button 

        # making current tab to go back 

        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back()) 

  

        # adding this to the navigation tool bar 

        navtb.addAction(back_btn)

  

        # similarly adding next button 

        next_btn = QAction("Forward", self)
        next_btn.setIcon(QIcon('images/right-arrow.png'))

        next_btn.setStatusTip("Forward to next page") 

        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward()) 

        navtb.addAction(next_btn) 

  

        # similarly adding reload button 

        reload_btn = QAction("Reload", self)
        reload_btn.setIcon(QIcon('images/reload.png'))
        reload_btn.property('border-radius:2px;')

        reload_btn.setStatusTip("Reload page") 

        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload()) 

        navtb.addAction(reload_btn) 

  

        # creating home action 

        home_btn = QAction("Home", self)
        home_btn.setIcon(QIcon('images/home.png'))

        home_btn.setStatusTip("Go home") 

  

        # adding action to home button 

        home_btn.triggered.connect(self.navigate_home) 

        navtb.addAction(home_btn) 

  

        # adding a separator 

        navtb.addSeparator() 

  

        # creating a line edit widget for URL 

        self.urlbar = QLineEdit() 
        self.urlbar.setStyleSheet("border: 2px solid red;color: blue;border-radius: 5px;background-color:black;font-size:12px;height:22px;font:Helvetica;")

  

        # adding action to line edit when return key is pressed 

        self.urlbar.returnPressed.connect(self.navigate_to_url) 

  

        # adding line edit to tool bar 

        navtb.addWidget(self.urlbar) 

  

        # similarly adding stop action
        stop_btn = QAction("Go", self)
        stop_btn.setIcon(QIcon('images/search.png'))

        stop_btn.setStatusTip("Visit url") 

        stop_btn.triggered.connect(self.Visit) 

        navtb.addAction(stop_btn) 
        colorButton = QPushButton()
        colorButton.setIcon(QIcon('images/menu.png'))
        navtb.addWidget(colorButton)
        self.sub =GeeksforGeeks

        # creating back action 

        menu = QMenu()
        menu.addAction("SETTINGS").triggered.connect(self.red)
        menu.addAction("PAGE SOURCE").triggered.connect(self.blue)
        colorButton.setMenu(menu)

        # creating first tab 

        self.add_new_tab(QUrl(self.basepath+"/search.html"), 'New Tab') 

  

        # showing all the components

  

        # setting window title
        

        self.setWindowTitle("X Browser")
    def cookie_filter(self,req):
           print(
            f"firstPartyUrl: {req.firstPartyUrl.toString()}, origin: {req.origin.toString()}, thirdParty? {req.thirdParty}"
        )
           return False
        
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if rules.should_block(url):
            print("block::::::::::::::::::::::", url)
            info.block(True)

    @QtCore.pyqtSlot("QWebEngineFullScreenRequest")
    def FullscreenRequest(self, request):
        request.accept()
        if request.toggleOn():
            self.browser.setParent(None)
            self.browser.showFullScreen()
        else:
            self.setCentralWidget(self.browser)
            self.browser.showNormal()


    # method for adding new tab 
    def red(self):
            path = self.tabs.currentWidget().url().toString().replace('file:///','')
            print(path)
            file = open(path)
            cont = file.read()
            print(cont)
    def blue(self):
            if path.exists(self.tabs.currentWidget().url().toString().replace('file:///','')):
                cell = self.tabs.currentWidget().url().toString().replace('file:///','')
                print(cell)
                file = open(cell)
                cont = file.read()
            else:
                response = request.urlopen(self.tabs.currentWidget().url().toString())
                # set the correct charset below
                cont = response.read().decode('utf-8')
            with open('editor.html','w',encoding='utf-8') as file:
             file.write('''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link href="https://fonts.googleapis.com/css?family=Germania+One|Raleway|Montserrat" rel="stylesheet">
<link rel="stylesheet" href="editor.css">
</head>
<body>
<div class="setting">
<button class="tablink" onclick="openPage('editor', this, '#0f97f9')" id="defaultOpen">Editor</button>
<button class="tablink" onclick="openPage('output', this, '#0f97f9')" id="run">Output</button>  
<span id="option">&#8942;</span>
</div>
<div class="main">
<div class="options">
    <p>Font size</p> 
<div class="slidecontainer">
  <input type="range" min="1" max="30" value="10" class="slider" id="slider">
  <r></r>
</div>

<p>Themes</p>
<br>
<button id="t1" class="btn"></button><button id="t2" class="btn"></button><button id="t3" class="btn"></button>
<br>
<p>Font style</p>

<br>
<button id="fontd">default</button>
<button id="font1">font</button>
<button id="font2">font</button>



</div>

<!--textarea-->
<div id="editor" class="tabcontent">
  <textarea id="code">
      
'''+cont+'''
      
      
  </textarea>
 
</div>

<!--output iframe-->
<div id="output" class="tabcontent">
<iframe id="result"></iframe>
</div>


</div>
 <script src="editor.js"></script>  
</body>
</html> 
''')         
            file.close()
            qurl = self.tabs.currentWidget().url()
            ori=qurl.toString()
            self.tabs.currentWidget().setUrl(QUrl(self.basepath+'/editor.html'))
            



    def _downloadRequested(self,item):
        global pot
        print(item.url().toString()) # QWebEngineDownloadItem
        pot = item.url().toString()
        self.w =GeeksforGeeks()
        self.w.show()

       
        print('downloading to', item.path())


    def add_new_tab(self, qurl = None, label ="Blank"): 

  

        # if url is blank
        print('add_new')
       

        if qurl is None: 

            # creating a google url 

            qurl = QUrl(self.basepath+"/search.html")
           
        elif qurl.toString() == self.basepath+'/search.html':

            pass
        elif path.exists(qurl.toString().replace('file:///','')):
            print('local2')
        else:
            try:
                print(qurl.toString())
                requests.get("http://www.google.com")
            except:
                print(4)
                qurl = QUrl(self.basepath+'/error.html')

            

        

  

        # setting url to browser
        browser = QWebEngineView() 
        browser.setUrl(qurl)

         

  

        # setting tab index 

        i = self.tabs.addTab(browser, label) 

        self.tabs.setCurrentIndex(i) 

  

        # adding action to the browser when url is changed 

        # update the url 

        browser.urlChanged.connect(lambda qurl, browser = browser: 

                                   self.update_urlbar(qurl, browser)) 

  

        # adding action to the browser when loading is finished 

        # set the tab title 

        browser.loadFinished.connect(lambda _, i = i, browser = browser: 

                                     self.tabs.setTabText(i, browser.page().title())) 
        self.tabs.currentWidget().urlChanged.connect(self.internet) 
        self.tabs.currentWidget().page().profile().downloadRequested.connect(self._downloadRequested)
        interceptor = WebEngineUrlRequestInterceptor()
        QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()
        

  

    # when double clicked is pressed on tabs 

    def tab_open_doubleclick(self, i): 

  

        # checking index i.e 

        # No tab under the click 

        if i == -1: 

            # creating a new tab 

            self.add_new_tab() 

  

    # wen tab is changed 

    def current_tab_changed(self, i): 

  

        # get the curl
        print('tab_changed')

        qurl = self.tabs.currentWidget().url()
        print(qurl.toString())

  

        # update the url 

        self.update_urlbar(qurl, self.tabs.currentWidget()) 

  

        # update the title 

        self.update_title(self.tabs.currentWidget())
        if qurl.toString() != self.basepath+'/search.html' and qurl.toString() != 'file:///'+self.basepath+'/search.html' and not path.exists(qurl.toString().replace('file:///','')):
          try:
            print('not locale')
            requests.get("http://www.google.com")
          except:
            print(3)
            self.tabs.currentWidget().setUrl(QUrl(self.basepath+'/error.html'))
            

    # when tab is closed 

    def close_current_tab(self, i): 

  

        # if there is only one tab 

        if self.tabs.count() < 2: 

            # do nothing 

            return

  

        # else remove the tab 

        self.tabs.removeTab(i) 

  

    # method for updating the title 
    def internet(self):
         try:
            urllib.request.urlopen('https://www.google.com', timeout=1)
         except (urllib.error.URLError):
              if self.tabs.currentWidget().url().toString()==self.basepath+'/search.html':
                pass
              elif self.tabs.currentWidget().url().toString()=='file:///'+self.basepath+'/search.html':
                pass
              elif self.tabs.currentWidget().url().toString()=='file:///'+self.basepath+'/error.html':
                pass
              elif path.exists(self.tabs.currentWidget().url().toString().replace('file:///','')):
                print('local')
              else:
                print(2,self.tabs.currentWidget().url().toString())
                self.tabs.currentWidget().setUrl(QUrl(self.basepath+'/error.html'))
               
         except:
            pass


    def update_title(self, browser): 

  

        # if signal is not from the current tab 

        if browser != self.tabs.currentWidget(): 

            # do nothing 

            return

  

        # get the page title 

        title = self.tabs.currentWidget().page().title() 

  

        # set the window title 

        self.setWindowTitle("% s - X Browser" % title) 

  

    # action to go to home 

    def navigate_home(self): 

  
        try:
          # go to google 
          
          self.tabs.currentWidget().setUrl(QUrl("http://www.duckduckgo.com"))
          requests.get("http://www.google.com")
        except:
            self.tabs.currentWidget().setUrl(QUrl(self.basepath+'/error.html'))
            
            
  

    # method for navigate to url 

    def navigate_to_url(self): 

  

        # get the line edit text
        print('navigate_to_url')

        # convert it to QUrl object 

        q = QUrl(self.urlbar.text()) 

  

        # if scheme is blank 

        if q.scheme() == "": 

            # set scheme 

            q.setScheme("http") 

  

        # set the url
        try:

          self.tabs.currentWidget().setUrl(q)
          requests.get("http://www.google.com")
        except:
            print(1)
            self.tabs.currentWidget().setUrl(QUrl(self.basepath+'/error.html'))
            

    def Visit(self):
        self.add_new_tab(QUrl(self.urlbar.text()))

    # method to update the url 

    def update_urlbar(self, q, browser = None): 

  

        # If this signal is not from the current tab, ignore 

        if browser != self.tabs.currentWidget(): 

  

            return

        if q.toString() == 'file:///'+self.basepath+'/search.html':
            self.urlbar.setText('')

        elif q.toString() == 'file:///'+self.basepath+'/error.html':
            self.urlbar.setText('')
        # set text to the url bar
        elif q.toString() == self.basepath+'/error.html':
            self.urlbar.setText('')
        elif q == self.basepath+'/error.html':
            self.urlbar.setText('')
        elif q =='file:///'+self.basepath+'/search.html':
            self.urlbar.setText('')
        elif q.toString() ==self.basepath+'/search.html':
            self.urlbar.setText('')
        elif q =='file:///'+self.basepath+'/editor.html':
            self.urlbar.setText('')
        elif q.toString() ==self.basepath+'/editor.html':
            self.urlbar.setText('')
        elif  path.exists(self.tabs.currentWidget().url().toString().replace('file:///','')):
            self.urlbar.setText('')

        else :
          

          self.urlbar.setText(q.toString()) 

  

          # set cursor position 

          self.urlbar.setCursorPosition(0) 


# creating a PyQt5 application
class WorkerThread(QObject):
    signalExample = pyqtSignal(str)
 
    def __init__(self):
        super().__init__()
 
    @pyqtSlot()
    def run(self):
        while True:
            # Long running task ...
            self.signalExample.emit("leet")
            time.sleep(1)


            

app = QApplication(sys.argv) 

  
# setting name to the application 

app.setApplicationName("X browser") 

  
# creating MainWindow object 

window = MainWindow()
window.show()
# loop 
app.exec_()
