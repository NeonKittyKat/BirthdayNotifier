import os
import tkinter as tk
from screeninfo import get_monitors
from pathlib import Path

# Get folder where this script is located
base_dir = Path(__file__).parent

# Build path to birthday/data.txt relative to script
dataPath = base_dir / "Data.txt"

print(dataPath)

root = tk.Tk()
entry_var = tk.StringVar()
entry_var2 = tk.StringVar()
m=get_monitors()[0]
scrWidth = int(m.width / 4)
scrHeight = int(m.height / 3)
DataTable = {}

def setBirthday():
    query1 = entry_var.get().strip().lower()  # name
    query2 = entry_var2.get().strip()         # birthday

    if not query1 or not query2:
        print("Name or birthday is empty")
        return
    
    with open(dataPath, 'r') as f:
        for line in f:
            name = line.split(':', 1)[0].strip().lower()  # extract name part, lowercase
            if name == query1:
                print("name exists already")
                return

    # Append to the text file (creates it if it doesn't exist)
    with open(dataPath, 'a') as f:
        f.write(f"{query1}:{query2}\n")

    print(f"Saved: {query1} -> {query2}")
def showBirthdays():
    os.chmod(dataPath, 0o644)
    os.system(f'notepad "{dataPath}"')
button1 = tk.Button(
    root,
    text="Set Name and Birthday",
    bg="#181818",     # Background color
    fg="#FFFFFF",       # Text color
    activebackground="#252525",  # Hover/click background
    activeforeground="#FFFFFF",     # Hover/click text
    command=setBirthday,
    width=30
)
button2 = tk.Button(
    root,
    text="Show all birthdays",
    bg="#181818",     # Background color
    fg="#FFFFFF",       # Text color
    activebackground="#252525",  # Hover/click background
    activeforeground="#FFFFFF",     # Hover/click text
    command=showBirthdays,
    width=30
)
entry1 = tk.Entry(
    root,
    width=40,
    textvariable=entry_var
)
entry2 = tk.Entry(
    root,
    width=40,
    textvariable=entry_var2
)
def enable_Window(event=None):
    root.title("BirthDay Notification")
    root.geometry(rf"{scrWidth}x{scrHeight}")
    root.configure(bg="#000000")

    label = tk.Label(root, text="Birthday Notifier", bg="#000000", fg="#FFFFFF")
    #grids
    label.grid(row=0, column=4, columnspan=1, sticky="n")
    button1.grid(row=3, column=0, rowspan=1, columnspan=2, sticky="w")
    button2.grid(row=5 , column=0, rowspan=1, columnspan=2, sticky="w")
    entry1.grid(row=2, column=5, columnspan=2)
    entry2.grid(row=4, column=5, columnspan=2)
def updateAll(event=None):
    for c in range(13):
        root.grid_columnconfigure(c, weight=1)
    for r in range(13):
        root.grid_rowconfigure(r, weight=1)

root.bind("<Configure>", updateAll)
enable_Window()

root.mainloop()
