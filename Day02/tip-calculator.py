print("Welcome to Tip Calculator!")
total_bill = float(input("What was your total bill?\n$"))
tip = int(input("What percentage of tip would you like to give? 10, 12, or 15?\n%"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
with_tip = total_bill * tip_as_percent
bill = total_bill + with_tip
bill_per_person = round(bill / people, 2)

print(f"Each person should pay: ${bill_per_person}")