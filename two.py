print("welcome to the tip calculator")
print("what was the total bill?")
total_bill = float(input("total bill: $"))
print("what percentage tip would you like to give? 10, 12, or 15?")
tip_percentage = int(input("tip percentage: "))
print("how many people to split the bill?")
people = int(input("number of people: "))
print("calculating...")
tip = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + tip
amount_per_person = total_bill_with_tip / people
print(f"total bill: ${total_bill:.2f}")
print(f"tip percentage: {tip_percentage}%")
print(f"total bill with tip: ${total_bill_with_tip:.2f}")
print(f"amount per person: ${amount_per_person:.2f}")

