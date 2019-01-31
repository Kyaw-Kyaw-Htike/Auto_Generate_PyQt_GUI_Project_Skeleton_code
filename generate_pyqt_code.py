# Copyright (C) 2019 Kyaw Kyaw Htike @ Ali Abdul Ghafur. All rights reserved.
import sys
import glob
import os
import subprocess
from ui_MainWin import Ui_MainWin
from PyQt5 import QtCore, QtGui, QtWidgets

def qt_browse_directory(parent_widget=None, text_display="Select Directory"):
    return str(QtWidgets.QFileDialog.getExistingDirectory(parent_widget, text_display))
def qt_browse_single_file(parent_widget=None, text_display='Open file', ini_directory='c:\\', str_filter='Image files (*.jpg *.gif)'):
    return QtWidgets.QFileDialog.getOpenFileName(parent_widget, text_display, ini_directory, str_filter)[0]
def qt_browse_multiple_files(parent_widget=None, text_display='Open files', ini_directory='c:\\', str_filter='Image files (*.jpg *.gif)'):
    return QtWidgets.QFileDialog.getOpenFileNames(parent_widget, text_display, ini_directory, str_filter)[0]

class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWin()
        self.ui.setupUi(self)
        self.ui.lineEdit_pathToBat.setText(r"D:\Anaconda3\envs\deep_learning\Library\bin\pyuic5.bat")
    def browse_directory_to_process(self):
        self.dir_process = qt_browse_directory(self)
        self.ui.lineEdit_pathToDirectoryToProcess.setText(self.dir_process)
    def browse_path_to_bat(self):
        self.fpath_bat = qt_browse_single_file(self, str_filter="Select pyuic5.bat file (*.bat)")
        self.ui.lineEdit_pathToBat.setText(self.fpath_bat)
    def gen_code(self):
        self.dir_process = self.ui.lineEdit_pathToDirectoryToProcess.text()
        self.fpath_bat = self.ui.lineEdit_pathToBat.text()
        fpaths_ui_files = glob.glob(os.path.join(self.dir_process, '*.ui'))
        str_display = []
        str_display.append(f'''
There are {len(fpaths_ui_files)} ui file(s) found created by Qt Designer.

Generated code

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

def qt_browse_directory(parent_widget=None, text_display="Select Directory"):
    return str(QtWidgets.QFileDialog.getExistingDirectory(parent_widget, text_display))
def qt_browse_single_file(parent_widget=None, text_display='Open file', ini_directory='c:\\', str_filter='Image files (*.jpg *.gif)'):
    return QtWidgets.QFileDialog.getOpenFileName(parent_widget, text_display, ini_directory, str_filter)[0]
def qt_browse_multiple_files(parent_widget=None, text_display='Open files', ini_directory='c:\\', str_filter='Image files (*.jpg *.gif)'):
    return QtWidgets.QFileDialog.getOpenFileNames(parent_widget, text_display, ini_directory, str_filter)[0]

        ''')

        for fpath_ui_file in fpaths_ui_files:
            fname_cur = os.path.basename(fpath_ui_file)
            name_cur = os.path.splitext(fname_cur)[0]
            subprocess.call([self.fpath_bat, fname_cur, '-o', 'ui_'+name_cur+'.py'], cwd=self.dir_process, shell=False)
            str_display.append(f'''
#######################################
# For {fname_cur} file:
#######################################
            
from ui_{name_cur} import Ui_{name_cur}

class {name_cur}(QtWidgets.QMainWindow): # or class {name_cur}(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_{name_cur}()
        self.ui.setupUi(self)
        
    def example_method_or_callback(self):
        pass     
            ''')

        str_display.append(f'''
#######################################
# Main application start
#######################################

app = QtWidgets.QApplication(sys.argv)
qwin = initialize_one_of_the_ui_clases_above()
qwin.show()
sys.exit(app.exec_())
        ''')

        self.ui.textEdit_output.setText('\n'.join(str_display))

app = QtWidgets.QApplication(sys.argv)
qwin = MainWin()
qwin.show()
sys.exit(app.exec_())