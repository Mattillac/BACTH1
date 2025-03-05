#prog 1
a = input("enter num 1: ")
b = input("enter num 2: ")
if a > b:
    print("num 1 is bigger")
elif a < b:
    print("num 2 is bigger")

#prog 2
a = input("enter num 1: ")
b = input("enter num 2: ")
if a == b:
    print("both are the same")
elif a < b or b < a:
    print("num 1 and 2 aren't the same")

#prog 3
a = int(input("enter num 1: "))
b = int(input("enter num 2: "))
r = a+b
print(r)

#prog 4
a = int(input("enter num 1: "))
b = int(input("enter num 2: "))
r = a*b
print(r)

#prog 5
a = float(input("enter num 1: "))
b = float(input("enter num 2: "))
r = a/b
print(r)

#prog 6
a = float(input("enter num 1: "))
b = float(input("enter num 2: "))
r = a**b
print(r)

#prog 7
a = 0
for i in range(10):
    b = int(input(f" Enter num {i+1}: "))
    a += b
print(a)

#prog 8
a = 0
for i in range(10):
    b = int(input(f" enter num {i+1}: "))
    if b % 2 != 0:
        a += 1
print(f"Odd numbers: {a}")

#pro 9
for a in range(1, 101):
    if a % 2 == 0:
     print(a)

#prog 10
for a in range(1, 101):
    if a % 10 != 0:
     print(a)
