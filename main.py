from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ["#", "@", "%", "$","&", "*", "^", ">","?", "<", "|"]

    random_len = random.randint(2, 6)

    
    # Short way: List Comprehension:
    list_password = [random.choice(letters) for _ in range(random_len + 3)]
    list_password += [str(random.choice(numbers)) for _ in range(random_len - 1)]
    list_password += [random.choice(symbols) for _ in range(random_len - 2)]
    
    # Long way: Loops
    # for _ in range(0, random_len + 2):
    #     random_letter = random.choice(letters)
    #     list_password += random_letter
        
    # for _ in range(0, random_len):
    #     random_number = random.choice(numbers)
    #     list_password += str(random_number)
        
    # for _ in range(0, random_len - 2):
    #     list_password += random.choice(symbols)
        
        
    random.shuffle(list_password)

    password = "".join(list_password)
    
    # for item in list_password:
    #     password += item
        
    password_entry.insert(END, string = password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web_data = web_entry.get().title()
    email_data = email_entry.get()
    password_data = password_entry.get()
    
    new_data = {
        web_data: {
            "email": email_data,
            "password": password_data
        }
    
    }
    
        
    if len(web_data) <= 0 or len(password_data) <= 0:
        messagebox.showerror(title = "Opps!", message = "There are some empty fields")
        
        
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                
                
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent = 4)
                
        # when there is no data in the file this kind of error will occur:
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent = 4)

        else:
            
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent = 4)
 
            
    web_entry.delete(0, END)
    password_entry.delete(0, END)
    

# ---------------------------- SEARCH DATA ------------------------------- #

def search():
    website = web_entry.get().title()
    
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(website.title(), f"Email: {data[website]['email']}\n"
                                f"Password: {data[website]["password"]}")
            
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!!")
        
    except KeyError, json.decoder.JSONDecodeError:
        messagebox.showerror("Error", "Site not found!!")
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)


canvas = Canvas(width = 160, height = 160)
logo = PhotoImage(file = "logo.png")
canvas.create_image(80, 80, image = logo)
canvas.grid(column = 1, row = 0)


website_label = Label(text ="Website:")
website_label.grid(column = 0, row = 1)


web_entry = Entry(width = 30)
web_entry.grid(column = 1, row = 1)
web_entry.focus()


search_button = Button(text = "search", width = 15, command = search)
search_button.grid(column = 2, row = 1)


emial_label = Label(text = "Email/Username:", padx= 20)
emial_label.grid(column=0, row = 2)


email_entry = Entry(width = 49)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(END, string = "afghanzerak508@gmail.com")


password_label = Label(text = "Password:")
password_label.grid(column =0, row = 3)


password_entry = Entry(width = 30)
password_entry.config(highlightthickness = 0)
password_entry.grid(column = 1, row = 3)


generate_password_button = Button(text = "Generate Password", command = generate_password)
generate_password_button.grid(column = 2, row = 3)



add_button = Button(text = "Add", width = 41, command = save_data)
add_button.grid(column = 1, row = 4, columnspan = 2)












window.mainloop()