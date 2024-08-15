def check_temperature(temp):  # Fixed the typo in the function name
    if temp < 70:
        return "Cold"
    elif temp >= 70 and temp < 80:
        return "Warm"
    else:
        return "Hot"


def square_list(numbers):
    square_numbers = []
    for num in numbers:
        square_numbers.append(num * num)
    return square_numbers


def countdown(n):
    while n > 0:
        print(n)
        n -= 1


# Testing the functions
print(check_temperature(89))  # Outputs: Hot

print(square_list([1, 2, 3, 4, 5]))  # Outputs: [1, 4, 9, 16, 25]

countdown(10)  # Outputs: 10 9 8 7 6 5 4 3 2 1