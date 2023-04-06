import random

with open("Capitales_Europe.txt", encoding="UTF-8") as txt_file:
    file = txt_file.readlines()

file = [duo.split(":") for duo in file]
countries = [duo[0].strip(" ") for duo in file]
capitals = [duo[1].strip(" ").rstrip("\n") for duo in file]
dico = {countries[x]: capitals[x] for x in range(len(countries))}


def submit_call(event):
    if event.keysym == "Return":
        submit()


def afficher(country_var):
    country_var.set(random.choice(countries))


def start():
    afficher(country_var)
    timer = 0
    while True:
        timer += 1
        timer_var.set(timer)
        print(timer)
        time.sleep(1)


def submit(answer_entry):
    if answer_entry.get().lower() == dico.get(country.get()).lower():
        print("Bravo")
        country.set(random.choice(countries))
        answer_entry.delete(0, END)
        if answer_entry.get().lower() == dico.get(country.get()).lower():
            while answer_entry.get().lower() == dico.get(country.get()).lower():
                country.set(random.choice(countries))
                answer_entry.delete(0, END)
    else:
        print("No")