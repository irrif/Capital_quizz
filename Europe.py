from tkinter import *
import random

with open("Capitales_Europe.txt", encoding="UTF-8") as txt_file:
    file = txt_file.readlines()

file = [duo.split(":") for duo in file]
countries = [duo[0].strip(" ") for duo in file]
capitals = [duo[1].strip(" ").rstrip("\n") for duo in file]
dico = {countries[x]: capitals[x] for x in range(len(countries))}
score = 0
errors = []
false = "False"
right = "Ok"


def europe_main():


    def afficher():
        pays = random.choice(countries)
        country_var.set(pays)


    def submit_call(event):
        if event.keysym == "Return" and len(countries) != 0:
            submit()


    def submit():  # sourcery skip: extract-duplicate-method
        global score, errors
        pays = country_var.get()
        if answer_entry.get().lower() == dico.get(country_var.get()).lower():
            while answer_entry.get().lower() == dico.get(country_var.get()).lower():
                score += 1
                score_var.set(str(str(score)+" / "+str(len(capitals))))
                answer_list.set(answer_list.get()+"\n"+country_var.get() + " : " + right)
                countries.remove(pays) #
                answer_entry.delete(0, END)
                if len(countries) != 0:
                    afficher()
                else:
                    answer_list.set(answer_list.get() + "\n" + "--- END ---")
        else:
            errors.append(country_var.get())
            answer_list.set(answer_list.get()+"\n"+country_var.get() + " : " + false)
            countries.remove(pays) #
            answer_entry.delete(0, END)
            if len(countries) != 0:
                afficher()
            else:
                answer_list.set(answer_list.get() + "\n" + "--- END ---")


    window_europe = Tk()
    window_europe.title("Europe")
    window_europe.bind("<Return>", submit_call)

    main_frame = Frame(window_europe)
    main_frame.pack()

    region_label = Label(main_frame, text="Europe", font=("Helvetica", 20, "bold"), fg="black")
    region_label.grid(row=0, column=0, pady=6)

    country_var = StringVar()
    country_label = Label(main_frame, textvariable=country_var, font=("Helvetica", 12, "bold"), width=20, height=2)
    country_label.grid(row=1, column=0)

    answer_entry = Entry(main_frame, font=("Helvetica", 12, "bold"))
    answer_entry.grid(row=2, column=0)

    score_var = IntVar(value="0 / 50")
    score_var_label = Label(main_frame, textvariable=score_var, font=("Helvetica", 12, "bold"))
    score_var_label.grid(row=3, column=0)

    answer_list = StringVar()
    answer_list_label = Label(main_frame, textvariable=answer_list, font=("Helvetica", 12, "bold"))
    answer_list_label.grid(row=0, column=1, rowspan=5)

    afficher()
    window_europe.mainloop()
