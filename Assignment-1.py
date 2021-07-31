# Take input for a list and sort it in descending order.

print("Enter the numbers in list.")
print("To finish capturing press Enter")
list1 = [int(i)for  i in input().split()]
list1.sort()
list1.reverse()
print(list1)