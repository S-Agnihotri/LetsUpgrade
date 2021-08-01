print("Enter your choice (1 or 2).")
choice = int(input("Press ( 1 ) for celsius to fahrenheit conversion.\nPress ( 2 ) for fahrenheit to celsius conversion."))
celsius = fahrenheit = 0.0

if choice == 1:
    celsius = float(input("Enter the value of celsius : "))
    fahrenheit = (celsius * 9/5) + 32      #(0°C × 9/5) + 32 = 32°F
    print(f"{celsius}°C is equal to {'{:.2f}'.format(fahrenheit)}°F")


elif choice == 2:
    fahrenheit = float(input("Enter the value of fahrenheit : "))
    celsius = (fahrenheit - 32) * 5/9      #(0°F − 32) × 5/9 = -17.78°C
    print(f"{fahrenheit}°F is equal to {'{:.2f}'.format(celsius)}°C")

else:
    print("Invalid Choice.")