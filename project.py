import tkinter as tk
import pyautogui
import keyboard

root = tk.Tk()

def move_mouse():
	pyautogui.moveTo(100, 150)

def root_loop():
	if keyboard.is_pressed('q'):
		print("Keypressed")
	root.after(50, root_loop)

class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		w = tk.Label(self, text="HEllo tkinter!")
		w.pack();
		button = tk.Button(self, text="Move mouse", fg="red", command=move_mouse)
		button.pack()



if __name__ == "__main__":
	MainApplication(root).pack(side="top", fill="both", expand=True)
	root.after(50, root_loop)
	root.mainloop()
	while True:
		print("HELO");

			
