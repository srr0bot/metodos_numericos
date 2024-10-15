import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def metodo_secante():
    # Función Original
    def fdx(x):
        return x*3 + 2(x**2) + 10*x - 20

    # Solicitar valores iniciales al usuario
    xiMenos = float(input("Ingresa el valor de Xi-1: "))
    xi = float(input("Ingresa el valor de Xi: "))
    error = float(input("Ingresa el valor de error permitido: "))

    # PROCEDIMIENTO
    tramo = 1
    tabla = []
    iteracion = -1
    while (error < tramo):
        iteracion += 1
        xnuevo = xi - (fdx(xi) * (xi - xiMenos)) / (fdx(xi) - fdx(xiMenos))
        tramo = abs(xnuevo - xi)
        xiMenos = xi
        xi = xnuevo
        tabla.append([iteracion, xi, tramo])

    # SALIDA
    print(tabulate(tabla, headers=['Iteración', 'Xi', 'Xi+1 - Xi']))
    print("========================================\nLa raíz exacta es: ", xnuevo, "\n========================================\n")

    # GRÁFICA
    a = -2
    b = 5
    n = 50
    xn = np.linspace(a, b, n)
    yn = fdx(xn)
    plt.plot(xn, yn)
    plt.grid(True)
    plt.axhline(0, color="#ff0000")
    plt.axvline(0, color="#ff0000")
    plt.title("Metodo Secante")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.plot(xi, 0, 'ro')

    if (xnuevo != np.nan):
        plt.axvline(xi)
    plt.show()