alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(en_text, shift_amount):
    cipher_text = ''
    for letter in en_text:
        if letter == ' ':
            new_position = en_text.index(' ')
            cipher_text += en_text[new_position]
        else:

            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > 25:
                new_letter = alphabet[new_position - 26]
                cipher_text += new_letter
            else:
                new_letter = alphabet[new_position]
                cipher_text += new_letter

    print(cipher_text)
