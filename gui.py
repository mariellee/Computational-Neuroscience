from tkinter import *
import time
import threading
import random
from datetime import datetime, timedelta


class TextChanger(threading.Thread):

	def __init__(self, stringVar):
		dt = datetime.now().strftime("%Y-%m-%dT%H_%M")
		self.file = open("gui_data/" + str(dt) + ".txt", "w")
		super(TextChanger, self).__init__()
		self.text = stringVar

	def run(self):
		possible_texts = ["Raise left hand"] * 12
		possible_texts.extend(["Raise right hand"] * 12)
		random.shuffle(possible_texts)
		timestamp = datetime.now()
		self.write_to_file("start", timestamp)
		timestamp += timedelta(0, 2)
		time.sleep((timestamp - datetime.now()).total_seconds())

		for i in range(24):
			message = random.choice(possible_texts)
			self.text.set(message)
			self.write_to_file(message, timestamp)
			timestamp += timedelta(0, 4)
			time.sleep((timestamp - datetime.now()).total_seconds())

			self.text.set("")
			self.write_to_file("end", timestamp)
			timestamp += timedelta(0, 4)
			time.sleep((timestamp - datetime.now()).total_seconds())

		self.text.set("session over")
		self.file.close()

	def write_to_file(self, command, timestamp):
		self.file.write(str(timestamp) + "\t" + command + "\n")


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


