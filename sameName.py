def spam():
    global eggs
    eggs='spam'

eggs='global'
spam()
print(eggs) 

# This code defines a function spam that modifies a global variable eggs.
# The initial value of eggs is 'global', but after calling spam(), it becomes 'spam'.
# This will print 'spam' since the global variable eggs is modified in the spam function.