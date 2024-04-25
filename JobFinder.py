from new_func import new_func


return new_func()
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number to check if it's prime: "))

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

else:
    print(number, "is not a prime number.")
number = int(input("Enter a number to check if it's prime: "))

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

else:
    print(number, "is not a prime number.")