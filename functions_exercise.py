def check_temterature(temp)
    if temp < 70 :
        return "Cold"
    elif temp > 70 and temp < 80:
        return "Warm"
    else:
        return "Hot"


def square_list(numbers):
    for num in numbers:
        return num *num

def countdown(n):
    while n > 0:
        return n
    n -= 1
    
check_temterature(89)

square_list([1,2,3,4,5])

countdown(10)
    

