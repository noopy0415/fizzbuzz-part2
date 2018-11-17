def fizzbuzz_convert(number):
    if number % 15 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"

    if number % 5 == 0: return "Buzz"

    return str(number)


result = fizzbuzz_convert(5)
print(result)
