num = int(input("Ingresar un número entero positivo "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "no es número primo")
            break
    else:
        print(num, "es número primo")
else:
    print(num, "no es número primo")

