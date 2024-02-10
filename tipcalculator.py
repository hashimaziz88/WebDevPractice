print("Welcome to tip calculator")
totalbill = input("what was the total bill? R")
totalpeople = input("how many people split the bill? ")
tip = input("How much tipwould you like to add? 10, 12, 15? ")

totalbillfloat = float(totalbill)
totalpeopleint = int(totalpeople)
tipint = int(tip)

finalbill = (tipint / 100 * totalbillfloat + float(totalbill)) / totalpeopleint

print(finalbill)
