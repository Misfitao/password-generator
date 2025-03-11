import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(" welcome to the password generator")
nr_letters = int(input("how many letters do you want? "))
nr_symbols = int(input(f"how many symbols do you want "))
nr_numbers = int(input(f"how many numbers do you want? "))

password_list = []
for char in range(0, nr_letters):
  password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
  password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
  password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"your password is: {password}")
