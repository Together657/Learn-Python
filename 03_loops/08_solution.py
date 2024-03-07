number = 29

is_prime = True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
else: # number == 1
    is_prime = False

print("Is {} a prime number? {}".format(number, "Yes" if is_prime else "No"))

