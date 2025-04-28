def fizzbuzz(number):

    
        if number % 3 == 0 and number % 5 == 0:
            return "fizzbuzz"
        elif number % 3 == 0:
            return "fizz"
        elif number % 5 == 0:
            return "buzz"
        else:
            return "The number is not a multiple of 3 or 5."
    


if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    result = fizzbuzz(user_input)
    print(result)