birthdays = {'Alice':'Apr 1', 'Bob':'May 5', 'Juan':'Aug 13'}

while True:
    print('Enter a name: ')
    name=input()
    if name == '':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the birthday for {name}')
    else:
        print(f'I do not have birthday information for {name}')
        print(f'When is the birthday?')
        bday=input()
        birthdays[name]=bday
        print('Birthday database updated!')