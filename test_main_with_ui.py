import sys
import fitz
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QLabel, QLineEdit
from PySide6.QtUiTools import QUiLoader
from UIs.ui_simpleUI1_20Jan2023 import Ui_Widget
from ocr_funtions import check_reptition, extractTextFromPdf, saveFileToDst
import getpass


class MainWindow(QtWidgets.QWidget, Ui_Widget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #super(MainWindow, self).__init__()
        self.setWindowTitle("PDF Text Extractor")
        self.BrowseButton.clicked.connect(self.open_files)
        self.filenames = {}
        self.saveDestinations = ""
        self.bucketExtracted = False
        self.CancelButton.clicked.connect(self.cancelProgress)
        self.ExtractTextButton.clicked.connect(self.extractText)
        self.changeSaveLocationButton.clicked.connect(self.changeSaveLocation)
        self.treatedFileId = 0
        self.userDefaultDesktopPath = f"C/Users/{getpass.getuser()}/Desktop" #C:\Users\12\Desktop
    def open_files(self):
        options = QFileDialog.Option()
        options |= QFileDialog.Option().ReadOnly
        files = QFileDialog.getOpenFileNames(self,
                        caption="Select one or more files to open",
                        dir="",
                        filter="PDF Document (*.pdf) ", options = options)
                        
        if files is None or len(files)==0 or len(files[0])==0:
            return None
            
        for i in range(len(files[0][0])-1,-1,-1):
            if files[0][0][i]=='/' or files[0][0][i]=='\\':
                break
        self.saveDestinations = files[0][0][:i]
            
        #print("save destination got: ",self.saveDestination)
        for file in files[0]:
            labelTemp = QtWidgets.QListWidgetItem(file)
            self.listWidget.addItem(labelTemp)
            self.filenames[file] = labelTemp
        self.bucketExtracted = False

    def extractText(self):
        if self.bucketExtracted==False:
            for file in self.filenames.keys():
                if check_reptition(file):
                    doc = fitz.open(file)
                    doc = extractTextFromPdf(file_path=file, page_end = len(doc), show_log = True)
                    saveFileToDst([doc], file[:-4]+'_extracted.pdf')
                    self.listWidget.removeItemWidget(self.filenames[file])
            self.bucketExtracted = True
            self.filenames = {}

    # def save_files_to_destination(self):
    #     for file in self.filenames:
    #          QFileDialog.getSaveFileName(self, caption="Save File To...", dir = file, filter="PDF Document (*.pdf) ")
    def changeSaveLocation(self):
        options = QFileDialog.Option()
        options |= QFileDialog.Option().ReadOnly
        options |=QFileDialog.Option().DontResolveSymlinks
        dir = QFileDialog.getExistingDirectory(self,caption="choose another folder...", dir = self.userDefaultDesktopPath, options = options)
        self.saveDestinations = dir + self.saveDestinations[-12:]

    def cancelProgress(self):
        self.filenames = {}
        self.listWidget.clear()
        self.bucketExtracted = False

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()

    window.show()

    sys.exit(app.exec())

if __name__=="__main__":
      main()