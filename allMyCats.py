catNames=[]

while True:
    print(f"Enter the name of cat {len(catNames)+1} (or enter nothing to stop): ")
    name=input()
    if name == "":
        break
    catNames.append(name)

print("The names of the cats are: ")
for name in catNames:
    print(f" {name}")
print("Thanks for entering the names of your cats!")

# This code collects names of cats from the user until they choose to stop.
# It stores the names in a list and then prints them out.
# The user can enter as many names as they like, and the program will display all the names entered.
# The program will terminate when the user inputs an empty string.
