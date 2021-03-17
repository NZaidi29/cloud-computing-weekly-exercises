#program to create and print a list of strings
S = input("Please type words separated by spaces: ")
result = S.split()
print(result)

#program to remove and add list elements
operation = input("Please type either add or remove: ")

if operation == "remove":
    i = int(input("Please type the position of the item you wish to remove: "))
    #I am assuming user counts from 1
    result.pop(i-1)
    print(result)
elif operation == "add":
    i = input("Please type the item you wish to add to the list: ") 
    result.append(i)
    print(result)
else:
    print("Invalid inputs")