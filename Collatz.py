def collatz(num):
    if num <= 0:
        return 1
    elif(num % 2 == 0):
        return num // 2
    else:
        return 3 * num + 1

num_str = input("enter a number")
num = int(num_str)

while num != 1:
    print(str(num))
    num = collatz(num)
print(str(num))