x = int(input("first value:"))
y = int(input("second value:"))



def sum(x, y):
    return x+y

def substract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    try:
        return x / y

    except ZeroDivisionError:
        print("You can't divide by zero!")

    


def main():
    print(sum(x, y))
    print(substract(x, y))
    print(multiply(x, y))
    print(divide(x, y))

main()