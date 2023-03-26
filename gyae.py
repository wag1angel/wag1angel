import tkinter as tk
from typing import List
import random
import time

# starta om spelet
global LBL_poäng
global BTN_återställ

# introduktion
global FRM_användar_INFO
global LBL_användare
global ENT_användarnamn
global BTN_SUBMIT

# välj nivå
global FRM_nivåer
global LBL_nivå
global BTN_nybörjare
global BTN_normal
global BTN_svår

# spelet Layout variables
global FRM_INFO
global LBL_användarnamn
global LBL_POINTS
global LBL_tid
global FRM_spel
global BTN_måltavla


spel_inställningar = {
    'namn': "",
    'Svårighet_nivå': "",
    'nybörjare': {
        'x': 6,
        'y': 3,
        'x_axis_max': 485,
        'y_axis_max': 485
    },
    'normal': {
        'x': 3,
        'y': 1,
        'x_axis_max': 510,
        'y_axis_max': 515
    },
    'svår': {
        'x': 0,
        'y': 0,
        'x_axis_max': 530,
        'y_axis_max': 515
    }
}


def introduction():
    global FRM_användar_INFO
    global LBL_användare
    global ENT_användarnamn
    global BTN_SUBMIT

    FRM_användar_INFO = tk.Frame(master=window, bg='black')
    FRM_användar_INFO.pack(fill=tk.BOTH, expand=True)

    LBL_användare = tk.Label(master=FRM_användar_INFO, text="Välj användarnamn: ", font=("Arial", 20), pady=15, bg='black', fg='magenta2')
    LBL_användare.pack()

    ENT_användarnamn = tk.Entry(master=FRM_användar_INFO, font=("Arial", 12), bg='black', fg='magenta2')
    ENT_användarnamn.pack()

    BTN_SUBMIT = tk.Button(master=FRM_användar_INFO, text="skicka in", command=spel_nivåer, font=("Arial", 12), bg='magenta2', fg='black')
    BTN_SUBMIT.pack()

    LBL_spel_DETAILS = tk.Label(master=FRM_användar_INFO, text="meningen med spelet \n är att klicka på svarta boxen \n så snabbt som möjligt \n innan tiden tar slut.", font=("Arial", 13), bg='black', fg='magenta2')
    LBL_spel_DETAILS.place(width=280, x=140, y=150)


def spel_nivåer():
    """
    funktion för att visa och välja svårighet
    """

    global FRM_nivåer
    global LBL_nivå
    global BTN_nybörjare
    global BTN_normal
    global BTN_svår
    global spel_settings

    spel_inställningar['användarnamn'] = ENT_användarnamn.get()

    FRM_användar_INFO.pack_forget()
    LBL_användare.pack_forget()
    ENT_användarnamn.pack_forget()
    BTN_SUBMIT.pack_forget()

    # make the window frame longer that hold the button together and lower the buttons
    FRM_nivåer = tk.Frame(master=window, height=650, width=550, borderwidth=4, relief=tk.SUNKEN, background='black')
    FRM_nivåer.pack(fill=tk.BOTH)

    LBL_nivå = tk.Label(master=FRM_nivåer, text="välj nivå:", pady=5, font=("Arial", 15), background='black', foreground='magenta2')
    LBL_nivå.pack()

    BTN_nybörjare = tk.Button(
        master=FRM_nivåer, 
        text="nybörjare", 
        height=3, width=15, 
        font=("Arial", 12),
        command=lambda : spel_layout(spel_inställningar['användarnamn'], spel_inställningar['nybörjare']),
        background='black', foreground='magenta2'
        )

    BTN_normal = tk.Button(
        master=FRM_nivåer, 
        text="normal", 
        height=3, width=15,
        font=("Arial", 12),
        command=lambda : spel_layout(spel_inställningar['användarnamn'], spel_inställningar['normal']),
        background='black', foreground='magenta2'
        )

    BTN_svår = tk.Button(
        master=FRM_nivåer, 
        text="svår", 
        height=3, width=15,
        font=("Arial", 12),
        command=lambda : spel_layout(spel_inställningar['användarnamn'], spel_inställningar['svår']),
        background='black', foreground='magenta2'
        )

    BTN_nybörjare.pack(side=tk.TOP, fill=tk.BOTH)
    BTN_normal.pack(side=tk.TOP, fill=tk.BOTH)
    BTN_svår.pack(side=tk.TOP, fill=tk.BOTH)

  
    # center the buttons
    FRM_nivåer.pack_propagate(False)
    FRM_nivåer.grid_rowconfigure(0, weight=1)
    FRM_nivåer.grid_rowconfigure(4, weight=1)
    FRM_nivåer.grid_columnconfigure(0, weight=1)
    FRM_nivåer.grid_columnconfigure(2, weight=1)

    # center the buttons and move them down
    BTN_nybörjare.grid(row=1, column=1, padx=10, pady=40, sticky='nsew')
    BTN_normal.grid(row=2, column=1, padx=10, pady=40, sticky='nsew')
    BTN_svår.grid(row=3, column=1, padx=10, pady=40, sticky='nsew')

    window.configure(background='black')




def spel_layout(användarnamn: str, difficulty: List):
    """
    funktion för att visa spelets layout
    """

    global FRM_INFO
    global LBL_användarnamn
    global LBL_POINTS
    global LBL_tid
    global FRM_spel
    global BTN_måltavla

    FRM_nivåer.pack_forget()
    LBL_nivå.pack_forget()
    BTN_nybörjare.pack_forget()
    BTN_normal.pack_forget()
    BTN_svår.pack_forget()

    
    FRM_INFO = tk.Frame(master=window, padx=10, pady=10)
    LBL_användarnamn = tk.Label(master=FRM_INFO, text=användarnamn, font=("Arial", 15))
    LBL_POINTS = tk.Label(master=FRM_INFO, text=0, font=("Arial", 15))
    LBL_tid = tk.Label(master=FRM_INFO, text=10, font=("Arial", 15))

    FRM_INFO.pack(fill=tk.BOTH, side=tk.TOP)
    LBL_användarnamn.pack(side=tk.LEFT)
    LBL_POINTS.pack(side=tk.LEFT)
    LBL_tid.pack(side=tk.RIGHT)

    
    FRM_spel = tk.Frame(master=window, height=550, width=550, relief=tk.SUNKEN, borderwidth=4)
    BTN_måltavla = tk.Button(
        master=FRM_spel, 
        height=difficulty['y'], 
        width=difficulty['x'],
        borderwidth=3,
        command=lambda: btn_position(difficulty),
        bg="magenta2"
    )

    FRM_spel.pack()
    BTN_måltavla.place(x=230, y=230)
    
    timer()


def btn_position(spel_nivå):
    x_axis = random.randint(0, spel_nivå['x_axis_max'])
    y_axis = random.randint(0, spel_nivå['y_axis_max'])
    LBL_POINTS['text'] += 1
    BTN_måltavla.place(x=x_axis, y=y_axis)


def timer():
    global LBL_tid
    global BTN_måltavla
    global FRM_spel
    global LBL_POINTS
    global LBL_poäng
    global BTN_återställ

    LBL_tid['text'] -= 1

    if LBL_tid['text'] == 0:
        BTN_måltavla.place_forget()

        LBL_poäng = tk.Label(master=FRM_spel, text=f"Poäng  : {LBL_POINTS['text']}", font=("Arial", 20))
        LBL_poäng.place(x=150, y=170)

        BTN_återställ = tk.Button(master=FRM_spel, text="Försök Igen", command=återställ, width=10)
        BTN_återställ.place(x=230, y=220)
        return 0

    LBL_tid.after(1000, timer)


def återställ():
    global LBL_poäng
    global BTN_återställ
    global FRM_INFO
    global FRM_spel

    LBL_poäng.pack_forget()
    BTN_återställ.pack_forget()
    FRM_INFO.pack_forget()
    FRM_spel.pack_forget()

    spel_nivåer()


window = tk.Tk()
window.title("Mål träning")
window.geometry("560x600")

introduction()

window.mainloop()
