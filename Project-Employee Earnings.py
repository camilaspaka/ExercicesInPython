name = input("Please enter the employee´s name: ").strip().title()
hourly_wage = input("Whats is their hourly wage? ")
hours_worked = input("How many hours have they worked this week? ")

earnings = float(hourly_wage) * float(hours_worked)

print(f"{name} earned ${earnings} this week.")