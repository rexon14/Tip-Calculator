print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
ptip = float(input("What percentage tip would you like to give? "))
nump = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round(bill*(1 + ptip/100)/nump,2)}")
