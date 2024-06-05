import tkinter as tk
import tkinter.font as tkFont

def button_command():
    label["text"] = "Юрій"

if __name__ == "__main__":
    root = tk.Tk()

    root.title("Say My Name")
    # setting window size
    width = 300
    height = 100
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    button = tk.Button(root)
    button["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    button["font"] = ft
    button["fg"] = "#000000"
    button["justify"] = "center"
    button["text"] = "Say My Name"
    button.place(x=10, y=50, width=280, height=30)
    button["command"] = button_command

    label = tk.Label(root)
    ft = tkFont.Font(family='Times', size=10)
    label["font"] = ft
    label["fg"] = "#333333"
    label["justify"] = "center"
    label["text"] = ""
    label.place(x=25, y=10, width=258, height=30)

    root.mainloop()
