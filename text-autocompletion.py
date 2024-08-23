import tkinter as tk
from tkinter import simpledialog

# Danh sách từ mẫu để tự động hoàn thành
words = ["hello", "help", "hi", "house", "how", "happy", "happen", "harmony", "hover", "horizon"]

class AutocompleteText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self.word_list = words
        self.bind("<KeyRelease>", self.on_keyrelease)

    def on_keyrelease(self, event):
        # Xóa các gợi ý trước đó
        self.delete("suggestion", tk.END)

        # Lấy từ hiện tại
        current_word = self.get("insert linestart", "insert wordend").strip()

        # Tìm kiếm các từ bắt đầu bằng từ hiện tại
        matches = [w for w in self.word_list if w.startswith(current_word)]

        if matches:
            self.insert(tk.END, f" {matches[0]}", ("suggestion",))
            self.tag_configure("suggestion", foreground="gray")

        # Xóa gợi ý nếu phím xoá được nhấn
        if event.keysym in ("BackSpace", "Delete"):
            self.delete("suggestion", tk.END)

    def on_tab(self, event):
        self.delete("insert linestart", "insert wordend")
        current_word = self.get("insert linestart", "insert wordend").strip()
        matches = [w for w in self.word_list if w.startswith(current_word)]

        if matches:
            self.insert(tk.END, matches[0])
        return "break"

# Tạo cửa sổ Tkinter
window = tk.Tk()
window.title("Text Editor with Autocompletion")

# Tạo ô văn bản với tính năng tự động hoàn thành
text_area = AutocompleteText(window, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10)

# Gắn sự kiện Tab để hoàn thành từ
text_area.bind("<Tab>", text_area.on_tab)

# Chạy vòng lặp chính của cửa sổ Tkinter
window.mainloop()
