# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import urllib.request
from PyQt5.QtWidgets import *
import sys
 
class GeeksforGeeks(QWidget):
 
    def __init__(self):
        super(GeeksforGeeks, self).__init__()
        self.resize(400,300)
 
        # calling a defined method to initialize UI
        # creating progress bar
        self.progressBar = QProgressBar(self)
 
        # setting its size
        self.progressBar.setGeometry(25, 45, 210, 30)
 
        # creating push button to start download
 
        # assigning activity to push button
        self.Download
 
        # setting window geometry
        self.setGeometry(310, 310, 280, 170)
 
        # setting window action
        self.setWindowTitle("GeeksforGeeks")
 
        
 
    # when push button is pressed, this method is called
    def Handle_Progress(self, blocknum, blocksize, totalsize):
 
        ## calculate the progress
        readed_data = blocknum * blocksize
 
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()
 
    # method to download any file using urllib
    def Download(self):
 
        # specify the url of the file which is to be downloaded
        down_url = '' # specify download url here
 
        # specify save location where the file is to be saved
        save_loc = 'C:\Desktop\GeeksforGeeks.png'
 
        # Downloading using urllib
        urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)
 
 
# main method to call our app
if __name__ == '__main__':
 
    # create app
    App = QApplication(sys.argv)
 
    # create the instance of our window
    window = GeeksforGeeks()
 
    # start the app
    sys.exit(App.exec())