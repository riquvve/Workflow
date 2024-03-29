import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.app"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg = "gray")
        label.pack()

canvas = tk.Canvas(root, height=500, width=500, bg='#e6ffe6')
canvas.pack()

frame =tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="black", bg="#e6ffe6", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="black", bg="#e6ffe6")
runApps.pack()

root.mainloop()