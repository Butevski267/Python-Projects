from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
#import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open('passwords.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message = 'No data file found.')
    else:
        if website in data:
            read_email = data[website]['email']
            read_password = data[website]['password']
            messagebox.showinfo(title=website, message = f"email:{read_email}\npassword:{read_password}")
        else:
            messagebox.showinfo(title='Error', message = 'You haven\'t saved a password for that website')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.delete(0,"end")
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_press():
    website = website_entry.get()
    email = email_entry.get()
    passv = password_entry.get()
    new_data = {
        website:{
            'email': email,
            'password': passv
        }
    }
    text = f'{website} | {email} | {passv}'

    if website == '' or passv == '':
        error = messagebox.showerror("Error", "Enter all your fields!")
    else:
        is_ok = messagebox.askokcancel(title=website, message = f"These are the details entered: \nEmail: {email}\nPassword: {passv}\n Is it okay to save?")


    if is_ok:
        try:
            with open('passwords.json', 'r') as f:
                #Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open('passwords.json','w') as f:
                json.dump(new_data, f, indent = 4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open('passwords.json', 'w') as f:
                #Saving updated data
                json.dump(data, f, indent = 4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=40,pady=40,bg='white')
window.title('Password Manager')



canvas = Canvas(width=200, height=200, highlightthickness=0,bg='white')
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = lock_image)
canvas.grid(row=0,column=1,columnspan=2 )

# Labels
website_label = Label(text='Website:',bg='white')
website_label.grid(row=1,column=0)

email_label = Label(text='Email/Username:',bg='white')
email_label.grid(row=2,column=0)

password_label = Label(text='Password:',bg='white')
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=31)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=54)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'b.butevski@hotmail.com')

password_entry = Entry(width=31)
password_entry.grid(row=3,column=1)

#Buttons
add_button = Button(text='Add',width=46,command = on_press)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text='Search',width=18, command = search_password)
search_button.grid(row=1,column=2)
generate_button = Button(text='Generate Password',width=18, command = generate_password)
generate_button.grid(row=3,column=2)







window.mainloop()