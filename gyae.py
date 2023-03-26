import tkinter as tk
from typing import List
import random
import time

# starta om spelet
global LBL_poang
global BTN_aterstall

# introduktion
global FRM_anvandar_INFO
global LBL_anvandare
global ENT_anvandarnamn
global BTN_SUBMIT

# välj nivå
global FRM_nivaer
global LBL_niva
global BTN_nybarjare
global BTN_normal
global BTN_svar

# spelet Layout variables
global FRM_INFO
global LBL_anvandarnamn
global LBL_POINTS
global LBL_tid
global FRM_spel
global BTN_maltavla


spel_installningar = {
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
    global FRM_anvandar_INFO
    global LBL_anvandare
    global ENT_anvandarnamn
    global BTN_SUBMIT

    FRM_anvandar_INFO = tk.Frame(master=window, bg='black')
    FRM_anvandar_INFO.pack(fill=tk.BOTH, expand=True)

    # Lägg till titel
    LBL_title = tk.Label(master=FRM_anvandar_INFO, text="Aim Trainer", font=("Arial", 30, "bold"), pady=20, bg='black', fg='magenta2')
    LBL_title.pack()

    # Centered text
    FRM_center = tk.Frame(master=FRM_anvandar_INFO, bg='black')
    FRM_center.pack(fill=tk.BOTH, expand=True)

    LBL_anvandare = tk.Label(master=FRM_center, text="Välj användarnamn: ", font=("Arial", 20), pady=10, bg='black', fg='magenta2')
    LBL_anvandare.pack()

    ENT_anvandarnamn = tk.Entry(master=FRM_center, font=("Arial", 12), bg='black', fg='magenta2')
    ENT_anvandarnamn.pack()

    BTN_SUBMIT = tk.Button(master=FRM_center, text="skicka in", command=spel_nivaer, font=("Arial", 12), bg='magenta2', fg='black')
    BTN_SUBMIT.pack()

    LBL_spel_DETAILS = tk.Label(master=FRM_center, text="meningen med spelet \n är att klicka på svarta boxen \n så snabbt som möjligt \n innan tiden tar slut.", font=("Arial", 13), bg='black', fg='magenta2')
    LBL_spel_DETAILS.pack(pady=50)




def spel_nivaer():
    """
    funktion för att visa och välja svårighet
    """

    global FRM_nivaer
    global LBL_niva
    global BTN_nyborjare
    global BTN_normal
    global BTN_svar
    global spel_settings

    spel_installningar['användarnamn'] = ENT_anvandarnamn.get()

    FRM_anvandar_INFO.pack_forget()
    LBL_anvandare.pack_forget()
    ENT_anvandarnamn.pack_forget()
    BTN_SUBMIT.pack_forget()

    # knapparnas storlek, färg och bakrund färg
    FRM_nivaer = tk.Frame(master=window, height=650, width=550, borderwidth=4, relief=tk.SUNKEN, background='black')
    FRM_nivaer.pack(fill=tk.BOTH)

    LBL_niva = tk.Label(master=FRM_nivaer, text="välj nivå:", pady=5, font=("Arial", 15), background='black', foreground='magenta2')
    LBL_niva.pack()

    BTN_nyborjare = tk.Button(
        master=FRM_nivaer, 
        text="nybörjare", 
        height=3, width=15, 
        font=("Arial", 12),
        command=lambda : spel_layout(spel_installningar['användarnamn'], spel_installningar['nybörjare']),
        background='black', foreground='magenta2'
        )

    BTN_normal = tk.Button(
        master=FRM_nivaer, 
        text="normal", 
        height=3, width=15,
        font=("Arial", 12),
        command=lambda : spel_layout(spel_installningar['användarnamn'], spel_installningar['normal']),
        background='black', foreground='magenta2'
        )

    BTN_svar = tk.Button(
        master=FRM_nivaer, 
        text="svår", 
        height=3, width=15,
        font=("Arial", 12),
        command=lambda : spel_layout(spel_installningar['användarnamn'], spel_installningar['svår']),
        background='black', foreground='magenta2'
        )

    BTN_nyborjare.pack(side=tk.TOP, fill=tk.BOTH)
    BTN_normal.pack(side=tk.TOP, fill=tk.BOTH)
    BTN_svar.pack(side=tk.TOP, fill=tk.BOTH)

  
    # centrera knapparna
    FRM_nivaer.pack_propagate(False)
    FRM_nivaer.grid_rowconfigure(0, weight=1)
    FRM_nivaer.grid_rowconfigure(4, weight=1)
    FRM_nivaer.grid_columnconfigure(0, weight=1)
    FRM_nivaer.grid_columnconfigure(2, weight=1)

    # centrera knapparna och flyttar på dem
    BTN_nyborjare.grid(row=1, column=1, padx=10, pady=40, sticky='nsew')
    BTN_normal.grid(row=2, column=1, padx=10, pady=40, sticky='nsew')
    BTN_svar.grid(row=3, column=1, padx=10, pady=40, sticky='nsew')

    window.configure(background='black')




def spel_layout(anvandarnamn: str, difficulty: List):
    """
    funktion för att visa spelets layout
    """

    global FRM_INFO
    global LBL_anvandarnamn
    global LBL_POINTS
    global LBL_tid
    global FRM_spel
    global BTN_maltavla

    FRM_nivaer.pack_forget()
    LBL_niva.pack_forget()
    BTN_nyborjare.pack_forget()
    BTN_normal.pack_forget()
    BTN_svar.pack_forget()

    
    FRM_INFO = tk.Frame(master=window, padx=10, pady=10, bg='black')
    LBL_anvandarnamn = tk.Label(master=FRM_INFO, text=anvandarnamn, font=("Arial", 15), fg='magenta2', bg='black')
    LBL_POINTS = tk.Label(master=FRM_INFO, text=0, font=("Arial", 15), fg='magenta2', bg='black')
    LBL_tid = tk.Label(master=FRM_INFO, text=10, font=("Arial", 15), fg='magenta2', bg='black')

    FRM_INFO.pack(fill=tk.BOTH, side=tk.TOP)
    LBL_anvandarnamn.pack(side=tk.LEFT)
    LBL_POINTS.pack(side=tk.LEFT)
    LBL_tid.pack(side=tk.RIGHT)

    
    FRM_spel = tk.Frame(master=window, height=550, width=550, relief=tk.SUNKEN, borderwidth=4, bg='black')
    BTN_maltavla = tk.Button(
        master=FRM_spel, 
        height=difficulty['y'], 
        width=difficulty['x'],
        borderwidth=3,
        command=lambda: btn_position(difficulty),
        bg="magenta2",
        fg='black'
    )

    FRM_spel.pack()
    BTN_maltavla.place(x=230, y=230)
    
    timer()

    


def btn_position(spel_niva):
    x_axis = random.randint(0, spel_niva['x_axis_max'])
    y_axis = random.randint(0, spel_niva['y_axis_max'])
    LBL_POINTS['text'] += 1
    BTN_maltavla.place(x=x_axis, y=y_axis)

    



def timer():
    global LBL_tid
    global BTN_maltavla
    global FRM_spel
    global LBL_POINTS
    global LBL_poang
    global BTN_aterstall

    LBL_tid['text'] -= 1

    if LBL_tid['text'] == 0:
        BTN_maltavla.place_forget()

        LBL_poang = tk.Label(master=FRM_spel, text=f"Poäng  : {LBL_POINTS['text']}", font=("Arial", 20), bg="black", fg="#EE82EE")
        LBL_poang.place(x=150, y=170)

        BTN_aterstall = tk.Button(master=FRM_spel, text="Försök Igen", command=aterstall, width=10, bg="black", fg="#EE82EE")
        BTN_aterstall.place(x=230, y=220)
        return 0

    LBL_tid.after(1000, timer)


def aterstall():
    global LBL_poang
    global BTN_aterstall
    global FRM_INFO
    global FRM_spel
    

    LBL_poang.pack_forget()
    BTN_aterstall.pack_forget()
    FRM_INFO.pack_forget()
    FRM_spel.pack_forget()

    spel_nivaer()
    


window = tk.Tk()
window.title("Mål träning")
window.geometry("560x600")
window.configure(bg="black")

introduction()

window.mainloop()
