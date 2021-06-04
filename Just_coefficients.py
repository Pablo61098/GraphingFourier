from sympy import *
import sympy as sp
from sympy.abc import x,n,T
import numpy as np
import matplotlib.pyplot as mpl


def introducir_a_zero():
    while (true):
        try:
            funcion = input("Ingrese una funcion valida para A0: ")
            funcion=sympify(funcion)
            return funcion
        except:
            funcion = input("Ingrese una funcion valida para A0: ")
            funcion = sympify(funcion)
            return funcion

def introducir_an():
    while (true):
        try:
            funcion = input("Ingrese una funcion valida An: ") + "*cos(2*pi*n*x/T)"
            funcion=sympify(funcion)
            return funcion
        except:
            funcion = input("Ingrese una funcion valida An: ")+"*cos(2*pi*n*x/T)"
            funcion = sympify(funcion)
            return funcion

def introducir_bn():
    while (true):
        try:
            funcion = input("Ingrese una funcion valida para Bn: ") + "*sin(2*pi*n*x/T)"
            funcion=sympify(funcion)
            return funcion
        except:
            funcion = input("Ingrese una funcion valida para Bn: ")+"*sin(2*pi*n*x/T)"
            funcion = sympify(funcion)
            return funcion





def menu():
    print("Elija una opcion:\n 1) Serie de Fourier Normal\n 2) Serie de Medio Rango de Fourier\n 3) Serie de Fourier Compleja\n 4) Salir")

def menu_2():
    print("Elija una opcion:\n 1) Introducir funciones\n 2) Introducir coeficientes\n 3) Salir")


def integrar_an(func,limits,periodo):
    func_integrated=lambdify(x,integrate(func*cos(2*np.pi*n*x/float(periodo)),x),"sympy")
    func_integrated=func_integrated(limits[1])-func_integrated(limits[0])
    return func_integrated

def integrar_bn(func,limits,periodo):
    func_integrated=lambdify(x,integrate(func*sin(2*np.pi*n*x/float(periodo)),x),"sympy")
    func_integrated=func_integrated(limits[1])-func_integrated(limits[0])
    return func_integrated

def integrar_a0(func,limits):
    func_integrated=lambdify(x,integrate(func,x),"sympy")
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
    bn = bn * (2 / periodo)
    print("-------------------")
    print(simplify(a_zero) )
    print(simplify(an))
    print(simplify(bn))
    print("-------------------")
    return [sympify(a_zero),sympify(an),sympify(bn)]

def menu_3():
    print("\n1) Continuar con otro indice de iteracion \n 2) Salir\n")


def coeficientes_normales():
    it=int(input("Ingrese el indice de iteracion: "))
    periodo=sympify("1")
    a_zero = introducir_a_zero()
    print("A0: " + str(a_zero))

    a_n = introducir_an()
    print("An: " +str(a_n))
    todo_an = 0
    for i in range(1, it):
        todo_an = todo_an + a_n.subs({n: i, x: x,T:periodo})
    print(todo_an)

    b_n = introducir_bn()
    print("Bn: " + str(b_n))
    todo_bn = 0
    for i in range(1, it):
        todo_bn = todo_bn + b_n.subs({n: i, x: x,T:periodo})
    print(todo_bn)

    todo = a_zero + todo_an + todo_bn
    print(todo)
    todo = lambdify(x, todo)

    x_v = np.arange(-4, 4 * np.pi, 0.1)
    y_v = todo(x_v)

    mpl.xlabel("n: " +str(it),fontsize=20)
    mpl.plot(x_v, y_v)
    mpl.show()

if __name__ == "__main__":
    while(True):
        coeficientes_normales()

''' (7*n*(-1)**n-7)/((pi**2)*(n**2)) '''
''' -(7*(-1)**n)/(pi*n) '''


'''
((7)*(((-1)**n)-1)/((n**2)*(pi**2)))
-(7*(-1)**(n))/(n*pi)
'''

'''
13*7/16
-((4*7*cos(n*pi/4))-(8*7*cos(n*pi/2))+(4*7*cos(3*pi*n/4)))/((n**2)*(pi**2))
(1/((n)*(pi)))*(7-(7*(-1)**n)-(1/n)*((4*7*sin(n*pi/4)/(pi))-((8*7*sin(n*pi/2)/(pi)))+((4*7*sin(3*n*pi/4)/(pi)))))

1/pi
(2/pi)*((-1)**n)/(1-(4*n**2))
(2/pi)*(-(-1)**n)/(1-(4*n**2))

-1/4
-sin((n*pi)/2)/(n*pi)
(1/2)*((6/(n*pi))-(6*cos((n*pi)/2)/(n*pi)))

(4*(pi)**2)/(3)
4*cos(2*n*pi)/(n**3)
(1/pi)*((-4*cos(2*n*pi)*pi**2)/n+(2*cos(2*n*pi)/n**3)-(2/n**3))

2
((cos(2*n*pi)-1)/(2*(n*pi)**2))
-(cos(2*n*pi)/(n*pi))
'''