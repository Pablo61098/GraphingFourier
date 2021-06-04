from sympy import *
from sympy.abc import x,n,T
import numpy as np
import matplotlib.pyplot as mpl
import time
import math

def introducir_a_zero(coeficiente_zero):
    while (true):
        try:
            funcion = coeficiente_zero
            funcion=sympify(funcion)
            return funcion
        except:
            funcion = input("Ingrese una funcion valida para A0: ")
            funcion = sympify(funcion)
            return funcion

def introducir_an(coeficiente_an):
    while (true):
        try:
            funcion = coeficiente_an*cos(2*pi*n*x/T)
            funcion=sympify(funcion)
            return funcion
        except:
            funcion = input("Ingrese una funcion valida An: ")+"*cos(2*pi*n*x/T)"
            funcion = sympify(funcion)
            return funcion

def introducir_bn(coeficiente_bn):
    while (true):
        try:
            funcion = coeficiente_bn*sin(2*pi*n*x/T)
            funcion=sympify(funcion)
            return funcion
        except:
            funcion = input("Ingrese una funcion valida para Bn: ")+"*sin(2*pi*n*x/T)"
            funcion = sympify(funcion)
            return funcion



def serie_normal(coeficientes,periodo,it):
    periodo=float(periodo)
    a_zero = introducir_a_zero(coeficientes[0])
    print("A0: " + str(a_zero))

    a_n = introducir_an(coeficientes[1])
    print("An: " + str(a_n))
    todo_an = 0
    for i in range(1, it):
        todo_an = todo_an + a_n.subs({n: i, x: x,T:periodo})
    print(todo_an)

    b_n = introducir_bn(coeficientes[2])
    print("Bn: " + str(b_n))
    todo_bn = 0
    for i in range(1, it):
        todo_bn = todo_bn + b_n.subs({n: i, x: x,T:periodo})
    print(todo_bn)

    todo = a_zero + todo_an + todo_bn
    print(todo)
    todo = lambdify(x, todo,["numpy"])

    x_v = np.arange(-4, 4 * np.pi, 0.1)
    y_v = todo(x_v)

    mpl.plot(x_v, y_v)
    mpl.xlabel("n="+str(it), fontsize=20)
    mpl.show()



'''
((7)-7*(-1)**n)/(n*pi)
(1/pi)*((((7)-7*(-1)**n)/(1+n*1))+(((7)-7*(-1)**n)/(1-n*1)))

((7)*(((-1)**n)-1)/((n**2)*(pi**2)))
-(7*(-1)**(n))/(n*pi)
'''
def menu():
    print("Elija una opcion:\n 1) Serie de Fourier Normal\n 2) Serie de Medio Rango de Fourier\n 3) Serie de Fourier Compleja\n 4) Salir")

def menu_2():
    print("Elija una opcion:\n 1) Introducir funciones\n 2) Introducir coeficientes\n 3) Salir")


def integrar_an(func,limits,periodo):
    func_integrated=lambdify(x,integrate(func*cos(2*np.pi*n*x/float(periodo)),x),["sympy","numpy"])
    func_integrated=func_integrated(limits[1])-func_integrated(limits[0])
    return func_integrated

def integrar_bn(func,limits,periodo):
    func_integrated=lambdify(x,integrate(func*sin(2*np.pi*n*x/float(periodo)),x),["sympy","numpy"])
    func_integrated=func_integrated(limits[1])-func_integrated(limits[0])
    return func_integrated

def integrar_a0(func,limits):
    func_integrated=lambdify(x,integrate(func,x),["sympy","numpy"])
    func_integrated=func_integrated(limits[1])-func_integrated(limits[0])
    return func_integrated


def conseguir_coeficientes(dict,periodo):
    a_zero=0
    an=0
    bn=0
    for func in dict:
        print("heeelloooooo")
        a_zero=a_zero+integrar_a0(sympify(func),dict[func])
        an=an+integrar_an(sympify(func),dict[func],periodo)
        bn=bn+integrar_bn(sympify(func),dict[func],periodo)
    a_zero = a_zero*(1/(periodo))
    an = an*(2/periodo)
    bn = bn*(2 / periodo)

    return [sympify(a_zero),sympify(an),sympify(bn)]

def menu_3():
    print("\n 1) Continuar con otro indice de iteracion \n 2) Salir\n")


if __name__ == "__main__":

    menu()
    opcion=input("Escoja una opcion: ")

    while(opcion!="4"):
        if(opcion == "1"):
            menu_2()
            opcion_2=input("Elija una opcion: ")

            while(opcion_2!="3"):
                if(opcion_2=="1"):
                    num_funciones=int(input("Cuantas funciones componen la serie: "))
                    periodo=sympify(input("Ingresa el perido: "))
                    left_start=0-float(periodo)/2
                    funciones={}
                    for i in range(num_funciones):
                        if(i!=num_funciones-1):
                            funcion=input("Ingrese la funcione que empieza en " + str(left_start)+" --> ")

                            right_end=float(sympify(input("Ingrese el fin de la funcion " + funcion+ " --> ")))
                            funciones[sympify(funcion)]=[left_start,right_end]
                            left_start=right_end
                        else:
                            funcion = input("Ingrese la funcione que empieza en " + str(left_start) + " y termina en: "+ str(float(periodo)/2)+" --> ")

                            right_end=float(periodo)/2
                            funciones[sympify(funcion)] = [left_start, right_end]

                    start_time=time.time()
                    coeficientes=conseguir_coeficientes(funciones,periodo)
                    print("\n -- Tiempo de ejecucion 1111111111: %s segundos -- " % (time.time() - start_time))


                    it=int(input("Ingrese el indice n de iteracion: "))
                    start_time = time.time()
                    serie_normal(coeficientes,periodo,it)
                    print("\n -- Tiempo de ejecucion 22222222: %s segundos -- " % (time.time() - start_time))
                    menu_3()
                    opcion_3=input("Elija una opcion: ")


                    while(opcion_3!=2):
                        start_time = time.time()
                        it = int(input("Ingrese el indice n de iteracion: "))
                        serie_normal(coeficientes, periodo, it)
                        print("\n -- Tiempo de ejecucion 22222222: %s segundos -- " % (time.time() - start_time))
                        menu_3()
                        opcion_3 = input("Elija una opcion: ")

                if (opcion_2 == "2"):
                    pass
        '''                    
        if (opcion == "2"):

        if (opcion == "3"):
        '''

        menu()
        opcion = input("Escoja una opcion: ")







