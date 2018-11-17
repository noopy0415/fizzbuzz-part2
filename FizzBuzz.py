number = 1
# for number in 1 to 100:
while number < 100:
    number += 1
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        continue
    if number % 3 == 0:
        print("Fizz")
        continue
    if number % 5 == 0:
        print("Buzz")
        continue
    print(str(number))

print()
