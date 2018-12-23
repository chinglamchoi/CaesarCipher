#Python 3 syntax

def encrypt():
    key = int(input("Please input a key: "))
    msg = input("Please input a message to encrypt in BLOCK LETTERS: ")
    encrypted_message = [encrypt_letter(letter, key) for letter in message]
    print('\n'.join(encrypted_message))
    

def decrypt():
    key = int(input("Please input a key: "))
    msg = input("Please input a message to decrypt in BLOCK LETTERS: ")
    decrypted_message = [decrypt_letter(letter, key) for letter in message]
    print('\n'.join(decrypted_message))
    
    
def encrypt_letter(letter, key):
    ascii_val = ord(letter)
    shifted_ascii_val = ascii_val + key
    shifted_letter =  chr((shifted_ascii_val - 65) % 26 + 65)
    return shifted_letter


def decrypt_letter(letter, key):
    ascii_val = ord(letter)
    unshifted_ascii_val = ascii_val - key
    unshifted_letter = chr((unshifted_ascii_val - 65) % 26 + 65)
    return unshifted_letter
