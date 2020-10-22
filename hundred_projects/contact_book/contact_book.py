# contact book

contacts = dict()


for _ in range(5):
    name = input("Enter a name: ")
    number = input("Enter number: ")
    contacts[name] = number

print(contacts)
