import tkinter as tk
import pyautogui
import keyboard
import socket

root = tk.Tk()
PORT = 33333
HOST = '127.0.0.1' 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST,PORT))


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
	root.after(50, root_loop)
	root.mainloop()

#{"id":"gaze_data", "x":243.104736539389, "y": 535.199351737433, "timestamp":1541217256708}qqqqq