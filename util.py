import tkinter

def alert_suspicious(line1, line2):
    FONT = "Calibri"
    FONT_SIZE = 13

    root = tkinter.Tk()
    root.geometry("300x200")
    root.title("Suspicious Activity")
    line1_label = tkinter.Label(root, text=line1, font=(FONT, FONT_SIZE))
    line1_label.place(x=60, y=60)
    line2_label = tkinter.Label(root, text=line2, font=(FONT, FONT_SIZE))
    line2_label.place(x=60, y=100)
    root.mainloop()

