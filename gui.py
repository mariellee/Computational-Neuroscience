from tkinter import *
import time
import threading
import random


class TextChanger(threading.Thread):

	def __init__(self, stringVar):
		super(TextChanger, self).__init__()
		self.text = stringVar

	def run(self):
		time.sleep(2)
		possible_texts = ["Raise left hand", "Raise right hand"]
		possible_text_shown_lengths = [2, 2.5, 3, 3.5, 4]
		possible_sleep_lengths = [1, 2, 3, 4, 5]

		while 1:
			self.text.set(random.choice(possible_texts))
			time.sleep(random.choice(possible_text_shown_lengths))
			self.text.set("")
			time.sleep(random.choice(possible_sleep_lengths))

# GUI
root = Tk()
root.title("Introduction to computational neuroscience")
root.geometry("1200x800")


stringVar = StringVar()

text = Label(root, textvariable=stringVar)
text.place(x=300, y=200)
text.config(font=("Ariel", 70))

textChanger = TextChanger(stringVar)
textChanger.start()

root.mainloop()


