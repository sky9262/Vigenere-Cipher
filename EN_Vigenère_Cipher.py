import time
import colorama
import argparse
import sys
import random


def vigenere_encrypt(plaintext, key):
    counter = 0
    encoded_text = ""
    for char in plaintext:
        vig_key_val = 0
        if char.islower():
            vig_key = key[counter]
            if vig_key.islower():
                vig_key_val = ord(vig_key) - ord("a")
            elif vig_key.isupper():
                vig_key_val = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("a") + vig_key_val) %26) +ord("a"))
            counter += 1

        elif char.isupper():
            vig_key = key[counter]
            if vig_key.islower():
                vig_key_val = ord(vig_key) - ord("a")
            elif vig_key.isupper():
                vig_key_val = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("A") + vig_key_val) %26) +ord("A"))
            counter += 1

        if counter == len(key):
            counter = 0

        if not char.isalpha():
            vig_char = char


        encoded_text += vig_char

    return encoded_text

def vigenere_decrypt(encodedtext, key):
    counter = 0
    decoded_text = ""
    for char in encodedtext:
        vig_key_val = 0
        if char.islower():
            vig_key = key[counter]
            if vig_key.islower():
                vig_key_val = ord(vig_key) - ord("a")
            elif vig_key.isupper():
                vig_key_val = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("a") - vig_key_val) %26) +ord("a"))
            counter += 1

        elif char.isupper():
            vig_key = key[counter]
            if vig_key.islower():
                vig_key_val = ord(vig_key) - ord("a")
            elif vig_key.isupper():
                vig_key_val = ord(vig_key) - ord("A")

            vig_char = chr(((ord(char) - ord("A") - vig_key_val) %26) +ord("A"))
            counter += 1

        if counter == len(key):
            counter = 0

        if not char.isalpha():
            vig_char = char


        decoded_text += vig_char

    return decoded_text

def gen_ran_char(char):
    if 'a' <= char <= 'z':
        return chr(random.randint(ord('a'), ord('z')))
    elif 'A' <= char <= 'Z':
        return chr(random.randint(ord('A'), ord('Z')))
    else:
        return char
    pass

def Decrypt_Animation(from_, to_):
    for i in range(len(to_)):
        chars = list(from_)  # Convert to a list for character replacement
        if ('a' <= chars[i] <= 'z') or ('A' <= chars[i] <= 'Z'):
            for _ in range(10):
                chars[i] = gen_ran_char(chars[i])  # Random character
                # Prepare the line to print
                line = colorama.Fore.GREEN + "".join(chars[:i]) + colorama.Fore.RESET + colorama.Fore.BLUE + chars[i] + colorama.Fore.RESET + colorama.Fore.RED + "".join(chars[i+1:]) + colorama.Fore.RESET

                print("\rDecrypted Text: " + line, end='', flush=True)  # Use carriage return instead of clearing the screen
                time.sleep(0.1)
            chars[i] = to_[i]  # Replace with the original character

        print("\rDecrypted Text: " + colorama.Fore.GREEN + to_ + colorama.Fore.RESET, end='', flush=True)  # Use carriage return instead of clearing the screen
        time.sleep(0.1)
        from_ = "".join(chars)

def Encrypt_Animation(from_, to_):
    for i in range(len(to_)):
        chars = list(from_)  # Convert to a list for character replacement
        if ('a' <= chars[i] <= 'z') or ('A' <= chars[i] <= 'Z'):
            for _ in range(10):
                chars[i] = gen_ran_char(chars[i])  # Random character
                # Prepare the line to print
                line = colorama.Fore.RED + "".join(chars[:i]) + colorama.Fore.RESET + colorama.Fore.BLUE + chars[i] + colorama.Fore.RESET + colorama.Fore.GREEN + "".join(chars[i+1:]) + colorama.Fore.RESET

                print("\rDecrypted Text: " + line, end='', flush=True)  # Use carriage return instead of clearing the screen
                time.sleep(0.1)
            chars[i] = to_[i]  # Replace with the original character

        print("\rDecrypted Text: " + colorama.Fore.RED + to_ + colorama.Fore.RESET, end='', flush=True)  # Use carriage return instead of clearing the screen
        time.sleep(0.1)
        from_ = "".join(chars)

def noArgs():
    # Define the menu
    menu = """
    1. Encrypt a Message:
    2. Decrypt a Message:
    3. Insert a Key:
    """

    # Initialize colorama
    colorama.init()
    # Add color to the menu options
    print(colorama.Fore.YELLOW + menu + colorama.Fore.RESET)

    # Get the user's choice
    choice = input("\nEnter your choice: ")
    key = ""
    # Perform the operations
    if choice == "1":
        plaintext = input("\nEnter the text message: ")
        if key != "":
            encrypted_text = vigenere_encrypt(plaintext, key)
            Encrypt_Animation(plaintext, encrypted_text)
            # print("\nEncrypted Text: " + colorama.Fore.BLUE + encrypted_text + colorama.Fore.RESET)
            print("\nKey: " + colorama.Fore.RED + key + colorama.Fore.RESET + "\n*Please remember the key!!!")

        else:
            key = input("Enter the key: ")
            encrypted_text = vigenere_encrypt(plaintext, key)
            Encrypt_Animation(plaintext, encrypted_text)
            # print("\nEncrypted Text: " + colorama.Fore.BLUE + encrypted_text + colorama.Fore.RESET)
            print("\nKey: " + colorama.Fore.RED + key + colorama.Fore.RESET + "\n*Please remember the key!!!")
    elif choice == "2":
        encrypted_text = input("\nEnter the encrypted message: ")
        if key != "":
            decrypted_text = vigenere_decrypt(encrypted_text, key)
            Decrypt_Animation(encrypted_text, decrypted_text)
            print("\nKey: " + colorama.Fore.RED + key + colorama.Fore.RESET + "\n\n")

        else:
            key = input("Enter the key: ")
            decrypted_text = vigenere_decrypt(encrypted_text, key)
            Decrypt_Animation(encrypted_text, decrypted_text)
            print("\nKey: " + colorama.Fore.RED + key + colorama.Fore.RESET + "\n\n")
    elif choice == "3":
        key = input("\nEnter the key: ")
    else:
        print("\nInvalid choice...!")

    # Ask the user if they want to continue
    while input("\nContinue? (yes/no): ") == "yes":
        print(colorama.Fore.YELLOW + menu + colorama.Fore.RESET)

        # Get the user's choice
        choice = input("\nEnter your choice: ")
        key = ""
        # Perform the operations
        if choice == "1":
            plaintext = input("\nEnter the text message: ")
            if key != "":
                encrypted_text = vigenere_encrypt(plaintext, key)
                # print("\nEncrypted Text: " + colorama.Fore.BLUE + encrypted_text + colorama.Fore.RESET)
                Encrypt_Animation(plaintext, encrypted_text)
                print("\nKey: " + colorama.Fore.RED + key + colorama.Fore.RESET + "\n*Please remember the key!!!")

            else:
                key = input("Enter the key: ")
                encrypted_text = vigenere_encrypt(plaintext, key)
                # print("\nEncrypted Text: " + colorama.Fore.BLUE + encrypted_text + colorama.Fore.RESET)
                Encrypt_Animation(plaintext, encrypted_text)
                print("\nKey: " + colorama.Fore.RED + key + colorama.Fore.RESET + "\n*Please remember the key!!!")
        elif choice == "2":
            encrypted_text = input("\nEnter the encrypted message: ")
            if key != "":
                decrypted_text = vigenere_decrypt(encrypted_text, key)
                Decrypt_Animation(encrypted_text, decrypted_text)
                print("\nKey: " + colorama.Fore.RED + key + colorama.Fore.RESET + "\n")

            else:
                key = input("Enter the key: ")
                decrypted_text = vigenere_decrypt(encrypted_text, key)
                Decrypt_Animation(encrypted_text, decrypted_text)
                print("\nKey: " + colorama.Fore.RED + key + colorama.Fore.RESET + "\n")

        elif choice == "3":
            key = input("\nEnter the key: ")
        else:
            print("\nInvalid choice...!")


def main():

    if len(sys.argv) == 1:
        noArgs()
        return

    # Create an argument parser
    parser = argparse.ArgumentParser(description="Text Encryption and Decryption")

    # Define the operation (encryption or decryption)
    parser.add_argument("-o", "--operation", required=True, choices=["encrypt", "decrypt"], help="Operation: encrypt or decrypt")

    # Define the key argument
    parser.add_argument("-k", "--key", required=True, help="Encryption key/decryption key")

    # Define the text argument
    parser.add_argument("-t", "--text", required=True, help="Text to encrypt or decrypt")

    # Parse the command-line arguments
    args = parser.parse_args()

    if args.operation == "encrypt":
        encrypted_text = vigenere_encrypt(args.text, args.key)
        # Crypt_Animation(args.text, encrypted_text)
        # print("\nKey: " + colorama.Fore.RED + args.key + colorama.Fore.RESET + "\n*Remember the key!!!")
        print(encrypted_text)
    elif args.operation == "decrypt":
        decrypted_text = vigenere_decrypt(args.text, args.key)
        # Crypt_Animation(args.text, decrypted_text)
        # print("\nKey: " + colorama.Fore.RED + args.key + colorama.Fore.RESET + "\n*Remember the key!!!")
        print(decrypted_text)

if __name__ == "__main__":
    main()



colorama.deinit()
