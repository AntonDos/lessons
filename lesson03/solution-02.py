deposit = 2130
time = 5
interest = 10
bonus = 120

for i in range(time):
    deposit = deposit + (deposit / interest) + bonus

print(deposit)
