def spam():
    global eggs 
    eggs = 'spam' #this is a global variable

def bacon():
    eggs = bacon #this is a local variable

def ham():
    print(eggs) #this will print the global variable

eggs = 42 #this is a global variable
spam()
print(eggs)

