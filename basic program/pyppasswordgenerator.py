import random
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '*', '#', '$', '%', '(', ')', '&', '+']
print("Welcome to Py-Password Generator")
letters_pass = int(input('How many letters would you like in your password?\n'))
symbols_pass = int(input("How many symbols would you like?\n"))
num_pass = int(input("How many numbers would you like?\n"))

password = ""   # to add different string letters and symbols later
for letters in range(1, letters_pass+1):
    password += random.choice(alphabet_list)

for num in range(1, num_pass+1):
    password += random.choice(num_list)

for sym in range(1, symbols_pass+1):
    password += random.choice(symbols_list)

# random.shuffle(list(password))
print(password)
final_password = ""
for finalpass in random.sample(password, len(password)):
    final_password += finalpass
print("you final password is :", final_password)

