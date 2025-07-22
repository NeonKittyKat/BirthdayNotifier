import datetime
from pathlib import Path
import tkinter as tk
import tkinter.font as tkFont

TodaysDate = datetime.date.today()
base_dir = Path(__file__).parent
dataPath = base_dir / "Data.txt"
root = tk.Tk()
BirthdayMessage = ""
Font = tkFont.Font(family="Helvetica", size=12)

def enable_Window(event=None):
    root.title("BirthDay Notification")
    root.geometry("300x200")
    root.configure(bg="#000000")

    label = tk.Label(root, text="Birthday Notifier", bg="#000000", fg="#FFFFFF")
    Message = tk.Message(root, text=BirthdayMessage, bg="#000000", fg="#FFFFFF", width=400, font=Font)
    #grids
    label.grid(row=0, column=4, columnspan=1, sticky="n")
    Message.grid(row=9, column=0, columnspan=10, sticky="w",)
def updateAll(event=None):
    for c in range(20):
        root.grid_columnconfigure(c, weight=1)
    for r in range(20):
        root.grid_rowconfigure(r, weight=1)


with open(dataPath, 'r') as file:
    for line in file:
        if line.__contains__( str(TodaysDate.month)):
            if line.__contains__(str(TodaysDate.day)):
                name = line.split(":", 1)[0]
                bornYear = line.split(":", 1)[1].split("/", 2)[2]
                newAge = (TodaysDate.year) - int(bornYear)
                BirthdayMessage = f"Its {name}'s Birthday today YAHHHHHHH \nThey are {newAge} years old"
                root.bind("<Configure>", updateAll)
                enable_Window()
                root.mainloop()
