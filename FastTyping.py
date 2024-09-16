from tkinter import *
import time
import random as r

from dominate.tags import button


class FastTyping(Tk):
    def __init__(self):
        super().__init__()
        self.current_word = None
        self.title("Speed type")
        self.minsize(width=600, height=300)
        self.configure(bg="#F56E14")
        self.phrases = [
            "Junior developers",
            "Write clean code",
            "Junior programmers",
            "Learn new languages",
            "Debugging skills",
            "Code reviews",
            "Coding skills",
            "I love Python",
            "I love Java"
        ]
        self.start_time = None

        # Intro label
        self.start_label = Label(self, text="Speed checker", font=("Arial", 24, "bold"), bg="#F56E14", fg="#F5D995")
        self.start_label.pack(pady=10)
        self.start_word = Label(self, text="", font=("Arial", 20, "bold"), bg="#F56E14", fg="black")
        self.start_word.pack(pady=25)
        # Typing Entry
        self.entry = Entry(width=35,font=("Arial", 16))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)
        # Result label
        self.result_label = Label(self, text="", font=("Arial", 20, "bold"), bg="#F56E14", fg="black")
        self.result_label.pack(pady=15)
        # Reset button
        self.button = Button(text="Reset", command=self.getNewPhrase, activebackground="#B6E053", activeforeground="#000000")
        self.button.pack(pady=10)
        self.getNewPhrase()

    def getNewPhrase(self):
        self.current_word = r.choice(self.phrases)
        self.start_word.config(text=self.current_word)
        self.entry.delete(0, END)
        self.start_time = time.time()

    def check_word(self, event):
        typed_phrase = self.entry.get().strip()
        if typed_phrase == self.current_word.lower():
            elapsed_time = time.time() - self.start_time
            typing_speed = int(len(self.current_word) / (elapsed_time/60))
            self.result_label.config(text=f"Your speed is {typing_speed} per minute", fg="black")
        else:
            self.result_label.config(text=f"Input and given phrase don't match", fg="black")

        self.after(1500, self.getNewPhrase())

if __name__ == "__main__":
    app = FastTyping()
    app.mainloop()