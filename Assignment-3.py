gift_presented_to = [2, 1, 5, 3, 4]
gift_received_from =[2, 1, 4, 5, 3]

for i in range(len(gift_received_from)):
    print(f"Person P{i+1} has received gift from person P{gift_received_from[i]}")