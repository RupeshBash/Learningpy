def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def main():
    number = int(input("Enter a number: "))
    result = check(number)
    