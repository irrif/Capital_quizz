import random
import time
from tkinter import *
from threading import Thread


def main():
    with open("Capitales_Europe.txt", encoding="UTF-8") as txt_file:
        file = txt_file.readlines()

    file = [duo.split(":") for duo in file]
    countries = [duo[0].strip(" ") for duo in file]
    capitals = [duo[1].strip(" ").rstrip("\n") for duo in file]
    dico = {countries[x]: capitals[x] for x in range(len(countries))}
    score = 0
    errors = []


    def choix_pays():
        pays = random.choice(countries)
        countries.remove(pays)
        return pays


    def submit_call(event):
        if event.keysym == "Return" and submit_button["state"] != "disabled":
            submit()


    def afficher():
        pays = random.choice(countries)
        country_var.set(pays)
        countries.remove(pays)


    def submit():
        global score, errors
        if answer_entry.get().lower() == dico.get(country_var.get()).lower():
            while answer_entry.get().lower() == dico.get(country_var.get()).lower():
                print("OK")
                score += 1
                score_var.set(str(str(score)+" / "+str(len(capitals))))
                country_var.set(choix_pays())
                answer_entry.delete(0, END)
        else:
            print("ERROR")
            errors.append(country_var.get())
            country_var.set(choix_pays())
            answer_entry.delete(0, END)

        if len(countries) == 0:
            print("END")
            show_button.config(state="disable")
            submit_button.config(state="disable")


    def show_errors():
        for a in errors:
            print(a, ":", dico[a])


    # def test():
    #     print(submit_button["state"])


    """ Fenêtre """
    window = Tk()
    window.geometry("1080x720")
    window.title("Quizz")

    window.bind("<Return>", submit_call)

    show_frame = Frame(window, bg="grey", borderwidth=2)
    show_frame.pack(anchor=CENTER)

    button_frame = Frame(window, bg="red", borderwidth=2)
    button_frame.pack(anchor=CENTER)

    """ Upper frame """
    region_label = Label(show_frame, text="Europe", font=("Helvetica", 16, "bold"))
    region_label.grid(row=0, column=0)

    country_var = StringVar()
    country_label = Label(show_frame, textvariable=country_var, font=("Helvetica", 12, "bold"))
    country_label.grid(row=1, column=0)

    answer_entry = Entry(show_frame, font=("Helvetica", 12, "bold"))
    answer_entry.grid(row=2, column=0)

    score_var = StringVar()
    score_frame = Label(show_frame, textvariable=score_var, font=("Helvetica", 12, "bold"))
    score_frame.grid(row=0, column=1, rowspan=2)

    """ Lower Frame """
    show_button = Button(button_frame, text="Show", command=afficher)
    show_button.grid(row=0, column=0)

    submit_button = Button(button_frame, text="Submit", command=submit)
    submit_button.grid(row=0, column=1)

    show_errors_button = Button(button_frame, text="Show errors", command=show_errors)
    show_errors_button.grid(row=0, column=2)

    # test_button = Button(button_frame, text="Test", command=test)
    # test_button.grid(row=0, column=3)

    window.mainloop()


if __name__ == '__main__':
    main()
