import tkinter as tk
from tkinter import font

class RoundedButton(tk.Canvas):
    def __init__(self, parent, border_radius, padding, color, text="", command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, relief="flat", highlightthickness=0, bg=parent["bg"])
        self.command = command
        font_size = 16
        self.font = font.Font(size=font_size, family='Helvetica', weight="bold")
        self.text = text
        self.id = None
        height = font_size + (2 * padding)
        width = self.font.measure(text) + (4 * padding)
        width = width if width >= 80 else 80
        if border_radius > 0.5 * width:
            print("Error: border_radius is greater than width.")
            return None
        if border_radius > 0.5 * height:
            print("Error: border_radius is greater than height.")
            return None
        rad = 2 * border_radius
        def shape():
            self.create_arc((0, rad, rad, 0), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width - rad, 0, width, rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width, height - rad, width - rad, height), start=270, extent=90, fill=color, outline=color)
            self.create_arc((0, height - rad, rad, height), start=180, extent=90, fill=color, outline=color)
            self.id = self.create_text(width/2, height/2, text=self.text, font=self.font, fill="white")
            self.bind("<ButtonRelease-1>", lambda event: self.command())
            return self
        shape()
        self.config(width=width, height=height)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Rounded Button Example")
    root.configure(bg="white")

    def button_click():
        print("Button clicked!")

    rounded_button = RoundedButton(root, border_radius=10, padding=10, color="#04AA6D", text="Click Me", command=button_click)
    rounded_button.pack(pady=20)

    root.mainloop()
