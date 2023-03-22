"""
for number in range(1,10,2):
    print(number*'.')
"""

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")