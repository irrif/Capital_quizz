from Europe import *
from tkinter import *

globe = "globe"


def valider():
    values_dict = {"Europe": europe_check.get(),
                   "Asie": asia_check.get(),
                   "Océanie": oceania_check.get(),
                   "Afrique": africa_check.get(),
                   "Amérique": america_check.get(),
                   "Amérique centrale": central_america_check.get()}
    if values_dict["Europe"] == 1:
        europe_main()


window = Tk()
window.title("Jeu Géographie")

text_frame = Frame(window, borderwidth=2)
text_frame.pack(side=TOP)

image_frame = Frame(window)
image_frame.pack()

title_label = Label(text_frame, text="Choix de la région", font=("Helvetica", 16, "bold"), pady=6)
title_label.grid(row=0, column=0, columnspan=6)

europe_check = IntVar()
europe_check_box = Checkbutton(text_frame, text="Europe", font=("Helvetica", 12, "bold"), variable=europe_check)
europe_check_box.grid(row=1, column=0)

asia_check = IntVar()
asia_check_box = Checkbutton(text_frame, text="Asie", font=("Helvetica", 12, "bold"), variable=asia_check)
asia_check_box.grid(row=1, column=1)

oceania_check = IntVar()
oceania_check_box = Checkbutton(text_frame, text="Océanie", font=("Helvetica", 12, "bold"), variable=oceania_check)
oceania_check_box.grid(row=1, column=2)

africa_check = IntVar()
africa_check_box = Checkbutton(text_frame, text="Afrique", font=("Helvetica", 12, "bold"), variable=africa_check)
africa_check_box.grid(row=1, column=3)

america_check = IntVar()
america_check_box = Checkbutton(text_frame, text="Amérique", font=("Helvetica", 12, "bold"), variable=america_check)
america_check_box.grid(row=1, column=4)

central_america_check = IntVar()
central_america_check_box = Checkbutton(text_frame, text="Amérique centreale", font=("Helvetica", 12, "bold"), variable=central_america_check)
central_america_check_box.grid(row=1, column=5)

validate_button = Button(text_frame, text="Valider", font=("Helvetica", 12, "bold"), command=valider)
validate_button.grid(row=2, column=0, rowspan=5, columnspan=6)

image_globe = PhotoImage(file=f"C:/Users/flori/Pictures/Python/{globe}.png")
image_label = Label(image_frame, image=image_globe, borderwidth=2)
image_label.pack()

window.mainloop()
