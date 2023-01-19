#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")

bill = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, 15? ")
num_to_split_bill = input("How many people to split the bill? ")

bill_to_float = float(bill)
tip_percentage_to_int = int(tip_percentage)
num_to_split_bill_int = int(num_to_split_bill)

tip = bill_to_float * (tip_percentage_to_int / 100)
total_bill = bill_to_float + tip

split_per_person = total_bill / num_to_split_bill_int
to_split = "{:.2f}".format(split_per_person)
message = f"Each person should pay: ${to_split}"

print(message)