import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_label.config(text="Invalid length")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=generated_password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
