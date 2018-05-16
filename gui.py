from tkinter import *
import time
import threading
import random
from datetime import datetime


class TextChanger(threading.Thread):

	def __init__(self, stringVar):
		self.file = open("testfile.txt", "w")
		super(TextChanger, self).__init__()
		self.text = stringVar

	def run(self):
		possible_texts = ["Raise left hand"] * 12
		possible_texts.extend(["Raise right hand"] * 12)
		random.shuffle(possible_texts)
		self.write_to_file("start")
		time.sleep(2)
		#possible_text_shown_lengths = [4]
		#possible_sleep_lengths = [4]

		for i in range(24):
			message = random.choice(possible_texts)
			self.text.set(message)
			self.write_to_file(message)
			time.sleep(4)
			#time.sleep(random.choice(possible_text_shown_lengths))
			self.text.set("")
			self.write_to_file("end")
			time.sleep(4)
			#time.sleep(random.choice(possible_sleep_lengths))

		self.text.set("session over")
		self.file.close()

	def write_to_file(self, command):
		self.file.write(str(datetime.now()) + "\t" + command + "\n")


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


