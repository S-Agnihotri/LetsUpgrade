# Check whether a string is a pangram.

alphabet = "abcdefghijklmnopqrstuvwxyz"
sentence = input("Please enter your sentence below:\n")

pangram = True

for char in alphabet:
    if char not in sentence.lower():
        pangram = False
    

        
if pangram:
    print("Entered sentence is a pangram.")
else:
    print("Entered sentence is not a pangram.")
