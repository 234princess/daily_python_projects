print ("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?\nN"))

tip_level = int(input("What tip percentage will you like to give? 10, 12 or 15?\n"))
tip = (tip_level / 100) + 1

no_people = int(input("How many people are splitting the bill?\n"))

final_tip = (total_bill * tip) / 5
rounded_tip = round(final_tip, 2)

print(f"Each person is to pay N{rounded_tip}")