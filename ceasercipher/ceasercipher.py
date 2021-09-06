from encrypt_for_ceasercipher import encrypt
from decrypt_for_ceasercipher import decrypt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


end_of_game = False
while not end_of_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
        to_continue = input("do you want to try again, say 'yes' or 'no' : ")
        if to_continue == 'yes':
            end_of_game = False
        else:
            end_of_game = True
    elif direction == 'decode':
        decrypt(text, shift)
        to_continue = input("do you want to try again, say 'yes' or 'no' : ")
        if to_continue == 'yes':
            end_of_game = True
        else:
            end_of_game = False
    else:
        print("error")
        to_continue = input("do you want to try again, say 'yes' or 'no' : ")
        if to_continue == 'yes':
            end_of_game = True
        else:
            end_of_game = False


