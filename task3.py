import tkinter as tk
import random
import string

def generate_password():
    try:
        password_length = int(entry_length.get())
        if password_length <= 0:
            password_label.config(text="Please enter a positive number.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        password_label.config(text=f"Generated Password: {generated_password}")
    except ValueError:
        password_label.config(text="Invalid input. Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input field for password length
label_length = tk.Label(root, text="Enter password length:")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

# Create button to generate the password
btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack()

# Create label to display the generated password
password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

root.mainloop()
