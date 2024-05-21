from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_main import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_clear.clicked.connect(self.clear_log_win)
        self.pushButton_start.clicked.connect(self.start_usb_trace)
        self.pushButton_stop.clicked.connect(self.stop_usb_trace)

    def clear_log_win(self):
        self.textBrowser.clear()

    def start_usb_trace(self):
        print('start')

    def stop_usb_trace(self):
        print('stop')    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
