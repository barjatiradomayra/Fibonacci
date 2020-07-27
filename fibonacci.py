numero = int(input("introducir numero:"))
a = 0
b = 1
fibonaci = 0

for rango  in range(0,numero):
    a = b
    b = fibonaci
    fibonaci = a +b 
    print(fibonaci)
