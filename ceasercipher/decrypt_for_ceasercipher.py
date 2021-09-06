alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def decrypt(de_text, shift_no):
    cipher_text = ''
    for letters in de_text:
        if letters == " ":
            new_position = de_text.index(' ')
            cipher_text += de_text[new_position]
        else:
            position = alphabet.index(letters)
            new_position = position - shift_no
            cipher_text += alphabet[new_position]

    print(cipher_text)
