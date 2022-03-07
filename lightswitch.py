import yaml, os.path
import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

switch = True
window.config(bg="black")

def logWrite(text):
    #bruh
    if not os.path.exists("actions.log"):
        with open("actions.log", "a") as file:
            file.write(text)
            file.close()
    else:
        with open("actions.log", "a") as file:
            file.write(text)
            file.close()



def toggleSwitch():
    global button
    global window
    global switch
    if switch:
        logWrite("light is on\n")
        window.config(bg="yellow")
        button.config(text="Switch light off")
        switch = False
    else:
        logWrite("light is off\n")
        window.config(bg="black")
        button.config(text="Switch light on")
        switch = True

button.config(text="Switch light on", command=toggleSwitch)


# schijf hier tussen je code
window.mainloop()