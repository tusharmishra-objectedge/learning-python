x = int(input())
if x > 0:
    print(f"{x} is positive")
    if x % 2:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
else:
    print(f"{x} is negative")
