# Function to encrypt a message using the Caesar Cipher method
def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Function to decrypt a message using the Caesar Cipher method
def decrypt_message(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

# Main program logic
def main():
    while True:
        print("Caesar Cypher Program")
        print("1 - Encrypt a message")
        print("2 - Decrypt a message")
        print("0 - Exit the program")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            message = input("Enter the message you want to encrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift value must be between 1 and 25.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            encrypted_message = encrypt_message(message, shift)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == "2":
            message = input("Enter the message you want to decrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift value must be between 1 and 25.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            decrypted_message = decrypt_message(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        else:
            print("Invalid choice. Please enter 0, 1, or 2.")

# Run the main function
if __name__ == "__main__":
    main()
