from tkinter.filedialog import*
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()
    
def openFile():
    file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)
    
def clearFile():
    entry.delete(1.0, END)
canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("NOTEPAD")
canvas.config(bg = "white")
top = Frame(canvas)
top.pack(padx = 10, pady = 5)

b1 = Button(canvas, text="open", bg = "white", command = openFile)
b1.pack(in_ = top, side=LEFT)

b2 = Button(canvas, text="save", bg = "white", command = saveFile)
b2.pack(in_ = top, side=LEFT)

b3 = Button(canvas, text="clear", bg = "white", command = clearFile)
b3.pack(in_ = top, side=LEFT)

b4 = Button(canvas, text="exit", bg = "white", command = exit)
b4.pack(in_ = top, side=LEFT)

entry = Text(canvas,wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

canvas.mainloop()
