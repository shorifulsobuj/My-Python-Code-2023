fName = input("Enter your First Name: ").lower()
sName = input("Enter your Second Name: ").lower()

name = fName.title() + " " + sName.title()

print(f'Your name is: {name}')
changeName = input('Which name you want to change: ').lower()
newName = input('Enter replaced name: ').lower()

finalName = name.replace(changeName.title(), newName.title())
print(f'Your name is: {finalName}')
