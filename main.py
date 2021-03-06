# passwordManager.py
#
# Python Bootcamp Day 29 - Password Manager
# Usage:
#      Enter requested info in the gui and save your website passwords to a flat
#  file.
#
# Marceia Egler November 28, 2021
import sys
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def pass_manager():
    # ---------------------------- PASSWORD GENERATOR ----------------------- #
    def pass_gen():

        letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

        nr_letters = [
            random.choice(letters) for char in range(random.randint(8, 10))
        ]

        nr_symbols = [
            random.choice(symbols) for sym in range(random.randint(2, 4))
        ]
        nr_numbers = [
            random.choice(numbers) for num in range(random.randint(2, 4))
        ]

        pass_list = nr_letters + nr_numbers + nr_symbols

        random.shuffle(pass_list)
        password = "".join(pass_list)
        password_input.insert(0, password)
        pyperclip.copy(password)

    # ---------------------------- SEARCH FOR PASSWORD ---------------------- #
    def search():
        website = website_input.get().title()
        try:
            with open("passwords.json", "r") as pass_file:
                entry = json.load(pass_file)
                try:
                    if entry[website]:
                        messagebox.showinfo(
                            title=website,
                            message=f"Email: {entry[website]['email']}\n\n"
                            f"Password: {entry[website]['password']}\n\n"
                            "Password has been copied to your clipboard.",
                        )
                        pyperclip.copy(entry[website]["password"])
                except KeyError:
                    messagebox.showwarning(
                        title="Error",
                        message=f"No Data for {website} found.",
                    )
        except FileNotFoundError:
            messagebox.showwarning(
                title="Error", message="You have no saved passwords"
            )

    # ---------------------------- SAVE PASSWORD ---------------------------- #
    def write_to_file(data_to_pass):
        with open("passwords.json", "w") as pass_file:
            json.dump(data_to_pass, pass_file, indent=4)

    def save():

        website = website_input.get().title()
        email = email_input.get()
        password = password_input.get()
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if len(website) < 1 or len(password) < 0:
            messagebox.showwarning(
                title="Missed Fields",
                message="Please double check any missed fields.",
            )
        else:
            try:
                with open("passwords.json", "r") as pass_file:
                    entry = json.load(pass_file)
            except FileNotFoundError:
                write_to_file(new_data)
            else:
                entry.update(new_data)
                write_to_file(entry)
            finally:
                website_input.focus_set()
                website_input.delete(0, "end")
                password_input.delete(0, "end")

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=200, height=200)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0, sticky="w")
    website_input = Entry(width=30)
    website_input.grid(row=1, column=1, columnspan=2, sticky="w")
    website_input.focus_set()
    website_search = Button(text="Search", width=15, command=search)
    website_search.grid(row=1, column=2)

    email_label = Label(text="Email/Username:")
    email_label.grid(row=2, column=0, sticky="w")
    email_input = Entry(width=52)
    email_input.grid(row=2, column=1, columnspan=2, sticky="w")

    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0, sticky="w")
    password_input = Entry(width=30)
    password_input.grid(row=3, column=1, sticky="w")

    gen_pass = Button(text="Generate Password", width=15, command=pass_gen)
    gen_pass.grid(row=3, column=2, sticky="w")
    add_button = Button(text="Add", width=44, command=save)
    add_button.grid(row=4, column=1, columnspan=2, sticky="w")

    window.mainloop()


def main():
    pass_manager()


if __name__ == "__main__":
    sys.exit(main())
