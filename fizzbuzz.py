stevilo = int(input("Select a number between 1 and 100:"))
x = 1

if stevilo >= 1 and stevilo <= 100:
    while x <= stevilo:
        ostanek_1 = x % 3
        ostanek_2 = x % 5
        if x % 3 == 0 and x % 5 == 0:
            print('fizzbuzz')
        elif ostanek_1 == 0:
            print ("fizz")
        elif ostanek_2 == 0:
            print("buzz")
        else:
            print(x)
        x += 1
