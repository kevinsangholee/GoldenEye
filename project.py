import tkinter as tk
import pyautogui
import keyboard

def move_mouse():
	pyautogui.moveTo(100, 150)

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		w = tk.Label(self, text="HEllo tkinter!")
		w.pack();
		button = tk.Button(self, text="Move mouse", fg="red", command=move_mouse)
		button.pack()

if __name__ == "__main__":
	root = tk.Tk()
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.mainloop()
	while True:
		try:
			if keyboard.is_pressed('q'):
				print("Keypressed");
				break
			else:
				pass
		except:
			break;
			
