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

    # ---------------------------- SAVE PASSWORD ---------------------------- #
    def save():
        with open("passwords.txt", "a") as pass_file:
            website = website_input.get()
            email = email_input.get()
            password = password_input.get()

            if len(website) < 1 or len(password) < 0:
                messagebox.showwarning(
                    title="Missed Fields",
                    message="Please double check any missed fields.",
                )
            else:
                is_ok = messagebox.askokcancel(
                    title=website,
                    message=f"These are the details entered:\nEmail: {email}\n"
                    f"Password: {password}\nIs it ok to save?",
                )

                if is_ok:
                    pass_file.write(f"{website} | {email} | {password}\n")
                    website_input.delete(0, "end")
                    password_input.delete(0, "end")
                    website_input.focus_set()

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
    website_input = Entry(width=52)
    website_input.grid(row=1, column=1, columnspan=2, sticky="w")
    website_input.focus_set()

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
