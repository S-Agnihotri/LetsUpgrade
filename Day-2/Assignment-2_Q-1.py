# Delete all occurrence of an element in a list.

userdata = []
length = int(input("How many elements you want to add in userdata: ")) # Taking length of the list from the user

# adding elements in list by the user
for i in range(length):
    userdata.append(input(f"Enter element at location {i+1} :  "))
    i = i + 1

removeElement = input("Which element you want to delete from the userdata:  ")

print(f"Before removing the element ({removeElement})\n",userdata)

# removing element from the list
if removeElement in userdata: # checking the element is available in list or not
    while removeElement in userdata:
        userdata.remove(removeElement)
    print(f"{removeElement} is removed from the userdata.")
else:
    print("Entered element is not available in userdata.")

print(f"After removing the element ({removeElement})\n",userdata)
