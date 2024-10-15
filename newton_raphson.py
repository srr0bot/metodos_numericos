import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def metodo_newton_raphson():
    # Función Original
    def funcionNormal(x):
        return x**3 + 2*x**2 + 10*x - 20

    # Primera derivada de la función
    def primeraDeriv(x):
        return 3*x**2 + 4*x + 10

    # Segunda derivada de la función
    def segundaDeriv(x):
        return 6*x + 4

    # Solicitar valores iniciales al usuario
    x0 = float(input("Ingresa el valor de x0 (punto inicial): "))
    error = float(input("Ingresa el valor del error permitido: "))

    # PROCEDIMIENTO
    tramo = abs(2 * error)
    xi = x0
    tabla = []
    iteracion = -1
    while (tramo >= error):
        iteracion += 1
        xnuevo = xi - (funcionNormal(xi) / primeraDeriv(xi))
        tramo = abs(xnuevo - xi)
        gPrimaValor = abs(1 - ((primeraDeriv(xi)**2 - funcionNormal(xi)*segundaDeriv(xi)) / primeraDeriv(xi)**2))
        xi = xnuevo
        tabla.append([iteracion, xi, tramo, gPrimaValor])

    # SALIDA
    print(tabulate(tabla, headers=['Iteración', 'Xi', 'Xi+1 - Xi', 'g(x)´']))
    print("========================================\nLa raíz exacta es: ", xi, "\n========================================\n")

    # GRÁFICA
    a = -2
    b = 5
    n = 50
    xn = np.linspace(a, b, n)
    yn = funcionNormal(xn)
    plt.plot(xn, yn)
    plt.grid(True)
    plt.axhline(0, color="#ff0000")
    plt.axvline(0, color="#ff0000")
    plt.title("Metodo Newton Raphson")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.plot(xi, 0, 'ro')

    if not np.isnan(xi):  # Verificación correcta de NaN
        plt.axvline(xi)
    
    plt.show()

