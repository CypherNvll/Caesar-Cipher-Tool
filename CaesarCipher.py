#    libs
import os 
import shutil
import random

#    variables
randomchars = 'LyQ|eFsl$gp=k7-}_U[ET?W,#"6bRj!V+4f5H0arS\'ti/`>D.&P2mxYo:q1NzGnBw)%h {J*Cvcu^X;I3~Z9d8]KO(MA<@\n\r'

#    functions
def cipher(file, shift):
    if os.path.isfile(file):
        with open(file, 'r') as f:
            text = f.read()
        encrypted = ''
        for char in text:
            if char in randomchars:
                new_index = (randomchars.index(char) + shift) % len(randomchars)
                encrypted += randomchars[new_index]
            else:
                encrypted += char
        with open(file, 'w') as f:
            f.write(encrypted)
        print(f"File '{file}' has been encrypted successfully.")
    elif os.path.isdir(file):
        for root, dirs, files in os.walk(file):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath, 'r') as f:
                    text = f.read()
                encrypted = ''
                for char in text:
                    if char in randomchars:
                        new_index = (randomchars.index(char) + shift) % len(randomchars)
                        encrypted += randomchars[new_index]
                    else:
                        encrypted += char
                with open(filepath, 'w') as f:
                    f.write(encrypted)
        print(f"Folder '{file}' has been encrypted successfully.")

def decipher(file, shift):
    if os.path.isfile(file):
        with open(file, 'r') as f:
            text = f.read()
        decrypted = ''
        for char in text:
            if char in randomchars:
                new_index = (randomchars.index(char) - shift) % len(randomchars)
                decrypted += randomchars[new_index]
            else:
                decrypted += char
        with open(file, 'w') as f:
            f.write(decrypted)
        print(f"File '{file}' has been decrypted successfully.")
    elif os.path.isdir(file):
        for root, dirs, files in os.walk(file):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath, 'r') as f:
                    text = f.read()
                decrypted = ''
                for char in text:
                    if char in randomchars:
                        new_index = (randomchars.index(char) - shift) % len(randomchars)
                        decrypted += randomchars[new_index]
                    else:
                        decrypted += char
                with open(filepath, 'w') as f:
                    f.write(decrypted)
        print(f"Folder '{file}' has been decrypted successfully.")

def str_cipher(text, shift):
    encrypted = ''
    for char in text:
        if char == '\n':  # Preserve line breaks
            encrypted += '\n'
        elif char == '\r':  # Preserve carriage returns
            encrypted += '\r'
        elif char in randomchars:
            new_index = (randomchars.index(char) + shift) % len(randomchars)
            encrypted += randomchars[new_index]
        else:
            encrypted += char
    return encrypted

def str_decipher(text, shift):
    decrypted = ''
    for char in text:
        if char == '\n':  # Preserve line breaks
            decrypted += '\n'
        elif char == '\r':  # Preserve carriage returns
            decrypted += '\r'
        elif char in randomchars:
            new_index = (randomchars.index(char) - shift) % len(randomchars)
            decrypted += randomchars[new_index]
        else:
            decrypted += char
    return decrypted

def main():
    print(f'\n{'='*10} Caesar Cipher Tool {'='*10}')
    print('1. Encrypt a file or folder')
    print('2. Decrypt a file or folder')
    print('3. Encrypt or decrypt a string')
    print('4. Exit')
    match input('Enter your choice: '):
        case '1':
            file = input('Enter the file or folder path to encrypt: ')
            shift = int(input('Enter the shift value (default: 5): ') or 5)
            cipher(file, shift)
        case '2':
            file = input('Enter the file or folder path to decrypt: ')
            shift = int(input('Enter the shift value, must be the same as the encryption shift (default: 5): ') or 5)
            decipher(file, shift)
        case '3':
            text = input('Enter the text to encrypt or decrypt: ')
            shift = int(input('Enter the shift value (default: 5): ') or 5)
            print(cipher(text, shift))
        case '4':
            exit()
        case _:
            print('Invalid choice')
            main()

if __name__ == '__main__':
    main()