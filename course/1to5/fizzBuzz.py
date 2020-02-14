def fizz_buzz(input):
    if(input % 3 == 0 and input % 5 == 0):
        return "FIZZBUZZ"
    elif(input % 3 == 0):
        return "FIZZ"
    elif(input % 5 == 0):
        return "FUZZ"
    else:
        return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(2))
