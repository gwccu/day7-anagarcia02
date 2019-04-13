# File name: warmupDay7.py
a = 0
while a <= 100:
    if (a % 5 == 0):
        print(a)
    a += 1

b = 0
for b in range(0, 105, 5):
    print(b)

star = 7
for star in range(7, 0, -2):
    print("*" * star)

number = 4
for number in range(4, 83, 1):
    if (number % 2 == 0):
        print("Blue")
    else:
        print("Green")
