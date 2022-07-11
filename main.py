from random import choice, shuffle, randint
from tkinter import messagebox
import tkinter
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.delete(0, tkinter.END)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ----------------------------  WEBSITE SEARCH ------------------------------- #

def search():
    website = website_input.get()
    try:
        with open('./Pass_Gen/data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message=f'No data file found.')
    else:
        if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists.')

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title='Oops!', message='Please don\'t leave any fields empty!')
    else:
        try:
            with open('./Pass_Gen/data.json', mode='r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('./Pass_Gen/data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('./Pass_Gen/data.json', mode='w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
FONT = 'Courier'

window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title('Password Generator')

canvas = tkinter.Canvas(height=200, width=200, highlightthickness=0)
pass_img = tkinter.PhotoImage(file='./Pass_Gen/logo.png')
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# WEBSITE
website_txt = tkinter.Label(text='Website:')
website_txt.grid(column=0, row=1)
website_input = tkinter.Entry(width=23)
website_input.grid(column=1, row=1)
website_input.focus()
# EMAIL
email_txt = tkinter.Label(text='Email/Username:')
email_txt.grid(column=0, row=2)
email_input = tkinter.Entry(width=38)
email_input.insert(0, 'vyva@mail.vy')
email_input.grid(column=1, row=2, columnspan=2)
# PASSWORD
password_txt = tkinter.Label(text='Password:')
password_txt.grid(column=0, row=3)
password_input = tkinter.Entry(width=23)
password_input.grid(column=1, row=3, )
# GEN BUTTON
gen_button = tkinter.Button(text='Generate',font=(FONT, 10, 'normal'), width=10, command=pass_generator)
gen_button.grid(column=2, row=3)
# ADD BUTTON
add_button = tkinter.Button(text='Add', highlightthickness=0, width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)
# SEARCH BUTTON
search_button = tkinter.Button(text='Search', highlightthickness=0, width=10, command=search)
search_button.grid(column=2, row=1)

window.mainloop()