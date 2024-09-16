from cmath import phase
from tkinter import *
import time
import random as r

from trio import current_time


class FastTyping(Tk):
    def __init__(self):
        super().__init__()
        self.title("Speed type")
        self.minsize(width=500, height=300)
        self.configure(bg="#F56E14")
        self.phrases = [
            "Junior developers write clean code.",
            "Junior programmers learn new languages.",
            "Debugging skills improvewith practice."
            "Code reviews enhance coding skills."
        ]
        self.start_time = None

        # Intro label
        self.start_label = Label(self, text="Speed checker", font=("Arial", 24, "bold"), bg="#F56E14", fg="#F5D995")
        self.start_label.pack(pady=10)
        self.start_word = Label(self, text="fd", font=("Arial", 20, "bold"), bg="#F56E14", fg="black")
        self.start_word.pack(pady=25)
        # Typing Entry
        self.entry = Entry(width=30, font=("Arial", 16))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)
        # Result label
        self.result_label = Label(self, text="dfg", font=("Arial", 20, "bold"), bg="#F56E14", fg="black")
        self.result_label.pack(pady=15)

        self.mainloop()

    def getNewPhrase(self):
        self.current_word = r.choice(self.phrases)
        self.start_word.config(text=self.current_word)
        # self.entry.delete()
        self.start_time = time.time()

    def check_word(self):
        typed_phrase = self.entry.get().strip()
        if typed_phrase == self.current_word:
            elapsed_time = time.time() - self.start_time
            typing_speed = int(len(self.current_word) / (elapsed_time/60))
            self.result_label.config(text=f"Your speed is {typing_speed} per minute", fg="black")
        else:
            self.result_label.config(text=f"Input and given phrase don't match", fg="black")