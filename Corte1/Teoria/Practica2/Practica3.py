while True:
    a = input("por favor ingrese un valor: ")
    print(a)

    parimpar = int(a)%2
    print(parimpar)
    if(parimpar== 0):
        print("el número es par")
    else:
        print("el número es impar")
    hacer = input("para repetir digite 3: ")
    if hacer != "3":
        break