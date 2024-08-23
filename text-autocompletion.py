import tkinter as tk
from tkinter import simpledialog


words = ["hello", "help", "hi", "house", "how", "happy", "happen", "harmony", "hover", "horizon"]

class AutocompleteText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self.word_list = words
        self.bind("<KeyRelease>", self.on_keyrelease)

    def on_keyrelease(self, event):
     
        self.delete("suggestion", tk.END)

        current_word = self.get("insert linestart", "insert wordend").strip()

        matches = [w for w in self.word_list if w.startswith(current_word)]

        if matches:
            self.insert(tk.END, f" {matches[0]}", ("suggestion",))
            self.tag_configure("suggestion", foreground="gray")

        if event.keysym in ("BackSpace", "Delete"):
            self.delete("suggestion", tk.END)

    def on_tab(self, event):
        self.delete("insert linestart", "insert wordend")
        current_word = self.get("insert linestart", "insert wordend").strip()
        matches = [w for w in self.word_list if w.startswith(current_word)]

        if matches:
            self.insert(tk.END, matches[0])
        return "break"

window = tk.Tk()
window.title("Text Editor with Autocompletion")

text_area = AutocompleteText(window, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10)

text_area.bind("<Tab>", text_area.on_tab)

window.mainloop()
