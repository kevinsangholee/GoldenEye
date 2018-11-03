import tkinter as tk
import pyautogui
import keyboard
import socket
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import *


root = tk.Tk()
PORT = 33333
HOST = '127.0.0.1' 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST,PORT))


class MyNotification(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        # < Styles >
        self.background_style_css = "background-color: rgba(22, 160, 133, 100); border-radius: 4px;"
        self.close_button_style_css = """
                                        QPushButton{
                                                    background-color: none;
                                                    color: white; border-radius: 6px;
                                                    font-size: 18px;
                                                    }
                                    """
        # </ Styles >

        # < Global Settings >
        self.setFixedSize(510, 210)
        self.move(400, 30)
        # </ Global Settings >

        # < Main Style >
        self.main_back = QLabel(self)
        self.main_back.resize(500, 200)
        self.main_back.setStyleSheet(self.background_style_css)
        # </ Main Style >

        # < Text Label >
        self.text_label = QLabel(self)
        self.text_label.move(10, 5)
        self.text_label.resize(300, 100)
        self.text_label.setText("Hi YUVI, How are You ? :)")
        # < Text Label >

        # < Header Style >
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # This Line Set Your Window Always on To
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        # </ Header Style >

    def terminal_ask(self):

        while True:

            print("If you want to close this window, type stop: ")

            get_input = input()

            if get_input.lstrip().rstrip().lower() == "stop":
                self.close_window()

            else:
                print("Invalid Syntax, Try it again.")

            QApplication.processEvents()

    def close_window(self):

        self.close()
        sys.exit()


def move_mouse():
	pyautogui.moveTo(100, 150)

def root_loop():
	data, addr = sock.recvfrom(1024)
	data = data.decode("utf-8")
	split = data.split('"x":')
	split2 = split[1].split(', "y": ')
	x = float(split2[0])
	split3 = split2[1].split(', "timestamp":')
	y = float(split3[0])
	timestamp = int(split3[1].split('}')[0]);
	print(x,y,timestamp)
	if keyboard.is_pressed('q'):
		print("clicking on " + str(x) + " "+ str(y))
		pyautogui.click(x,y)
	root.after(100, root_loop)

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		w = tk.Label(self, text="HACKATHON BABy")
		w.pack();
		button = tk.Button(self, text="Move mouse", fg="red", command=move_mouse)
		button.pack()


if __name__ == "__main__":
	
	MainApplication(root).pack(side="top", fill="both", expand=True)
	MainWindow = MyNotification()
	MainWindow.show()
	MainWindow.terminal_ask()
	root.after(50, root_loop)
	root.mainloop()

#{"id":"gaze_data", "x":243.104736539389, "y": 535.199351737433, "timestamp":1541217256708}qqqqq