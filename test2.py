saving_rate1 = int(input("Person 1: How much per month? "))
saving_rate2 = int(input("Person 2: How much per month? "))
yearly_rate = float(input("What is the interest rate of your acct? "))

monthly_rate = (yearly_rate / 12)

print(f"Your monthly rate is: {monthly_rate}%...")
saving_time = int(input("How long do you intend to save for (in months)? "))

calculated_savings = (saving_rate1 + saving_rate2) * saving_time
to_string = str(calculated_savings)

print(f"In {saving_time} months, you should save ${to_string}")
