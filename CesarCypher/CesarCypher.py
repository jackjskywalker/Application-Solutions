# Import the necessary modules
import tkinter as tk
from tkinter import messagebox

# Function to encrypt a message using the Caesar Cipher method
def encrypt_message(message, shift):
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""
    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Calculate the ASCII offset based on whether the letter is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Calculate the encrypted character by shifting it by the specified amount and wrapping around the alphabet if necessary
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            # Add the encrypted character to the encrypted message
            encrypted_message += encrypted_char
        else:
            # If the character is not a letter, add it to the encrypted message as-is
            encrypted_message += char
    # Return the encrypted message
    return encrypted_message

# Function to decrypt a message using the Caesar Cipher method
def decrypt_message(encrypted_message, shift):
    # Initialize an empty string to store the decrypted message
    decrypted_message = ""
    # Loop through each character in the encrypted message
    for char in encrypted_message:
        # Check if the character is a letter
        if char.isalpha():
            # Calculate the ASCII offset based on whether the letter is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Calculate the decrypted character by shifting it back by the specified amount and wrapping around the alphabet if necessary
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            # Add the decrypted character to the decrypted message
            decrypted_message += decrypted_char
        else:
            # If the character is not a letter, add it to the decrypted message as-is
            decrypted_message += char
    # Return the decrypted message
    return decrypted_message

# Function to be called when the Encrypt button is clicked
def encrypt_button_clicked():
    try:
        # Get the shift value from the shift entry field
        shift = int(shift_entry.get())
        # Get the message from the message entry field
        message = message_entry.get()
        # Encrypt the message using the specified shift value
        encrypted_message = encrypt_message(message, shift)
        # Display the encrypted message in the result text field
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Encrypted message: {encrypted_message}")
    except ValueError:
        # Show an error message if the shift value is invalid
        messagebox.showerror("Error", "Invalid shift value")

# Function to be called when the Decrypt button is clicked
def decrypt_button_clicked():
    try:
        # Get the shift value from the shift entry field
        shift = int(shift_entry.get())
        # Get the message from the message entry field
        message = message_entry.get()
        # Decrypt the message using the specified shift value
        decrypted_message = decrypt_message(message, shift)
        # Display the decrypted message in the result text field
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Decrypted message: {decrypted_message}")
    except ValueError:
        # Show an error message if the shift value is invalid
        messagebox.showerror("Error", "Invalid shift value")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create a label for the message entry field
message_label = tk.Label(root, text="Enter a message:")
message_label.pack()

# Create a frame for the message entry field with a margin on the left and right sides
message_frame = tk.Frame(root)
message_frame.pack(padx=20)

# Create a text entry field for the message
message_entry = tk.Entry(message_frame, width=50, justify=tk.CENTER)
message_entry.pack()

# Create a label for the shift entry field
shift_label = tk.Label(root, text="Enter a shift value (1-25):")
shift_label.pack()

# Create a text entry field for the shift value
shift_entry = tk.Entry(root, width=5, justify=tk.CENTER)
shift_entry.pack()

# Create a button to encrypt the message
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_clicked)
encrypt_button.pack()

# Create a button to decrypt the message
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_button_clicked)
decrypt_button.pack()

# Create a text field to display the result of the encryption or decryption
result_text = tk.Text(root, height=2, width=50)
result_text.pack(pady=10)

# Start the main event loop
root.mainloop()
