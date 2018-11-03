import tkinter as tk
import pyautogui
import keyboard
import socket
import sys

root = tk.Tk()
PORT = 33333
HOST = '127.0.0.1' 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST,PORT))
currX = 0
currY = 0
pressed = False
previousTime = 0
previousCoord = (1,1)
savedCoords = []

def root_loop():
	global currX
	global currY
	global previousTime
	global previousCoord
	data, addr = sock.recvfrom(1024)
	data = data.decode("utf-8")
	split = data.split('"x":')
	split2 = split[1].split(', "y": ')
	currX = float(split2[0])
	split3 = split2[1].split(', "timestamp":')
	currY = float(split3[0])
	timestamp = int(split3[1].split('}')[0]);
	if len(savedCoords) < 3:
		savedCoords.append([currX,currY])
	else:
		savedCoords[0] = savedCoords[1]
		savedCoords[1] = savedCoords[2]
		savedCoords[2] = (currX,currY)
	pause = timestamp - previousTime
	if(pause > 300 and pause < 500):
		pyautogui.click(savedCoords[0][0], savedCoords[0][1])
	previousTime = timestamp
	root.after(10, root_loop)


class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		w = tk.Label(self, text="HACKATHON BABY")
		w.pack();

def moveToCurrent(info):
	global pressed
	if not pressed:
		pressed = True
		pyautogui.moveTo(currX, currY)

def click(info):
	global pressed
	pyautogui.click()
	pressed = False

if __name__ == "__main__":
	
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.after(50, root_loop)
	keyboard.on_press_key('alt', moveToCurrent);
	keyboard.on_release_key('alt', click);
	root.mainloop()