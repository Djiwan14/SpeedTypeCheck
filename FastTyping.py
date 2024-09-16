from tkinter import *
import time
import random as r

class FastTyping(Tk):
    def __init__(self):
        super().__init__()
        self.title("Speed type")
        self.minsize(width=500, height=300)
        self.configure(bg="red")
        self.phrases = [
            "Junior developers write clean code.",
            "Junior programmers learn new languages.",
            "Debugging skills improvewith practice."
            "Code reviews enhance coding skills."
        ]
        self.start_time = None

        self.word_label = Label(text="Speed checker", font=("Arial", 24, "bold"))
        self.word_label.pack(pady=15)

        self.mainloop()