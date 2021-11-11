def checkio(number):
     if not number % 3 and not number % 5:
          return 'Fizz Buzz'
     elif not number % 3:
          return 'Fizz'
     elif not number % 5:
          return 'Buzz'
     return str(number)

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
