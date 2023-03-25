# use of Function inside the another function
def wage(hours, rate):
    return hours * rate
def with_bonus(hours, rate, bonus):
    return wage(hours, rate) + bonus

print(with_bonus(40, 10, 100))