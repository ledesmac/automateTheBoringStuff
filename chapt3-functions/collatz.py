import sys
def collatz(num:int) -> int:
    if num == 1:
        return 1
    
    if num % 2 == 0:
        num = num // 2
        print(num)
        collatz(num)
    else:
        collatz((3 * num + 1))


print("Please Enter an integer: ")
try:
    number = int(input())
except Exception as e:
    print("That is not an integer")

result = collatz(number)
sys.exit()


