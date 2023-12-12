import numpy as np
import matplotlib.pyplot as plt

def punto_medio(f, y0, t0, tn, h):
    """
    Método del punto medio para resolver ecuaciones diferenciales ordinarias (EDO).

    Parameters:
    - f: Función que define la EDO dy/dt = f(t, y).
    - y0: Condición inicial.
    - t0: Tiempo inicial.
    - tn: Tiempo final.
    - h: Tamaño del paso.

    Returns:
    - t_vals: Lista de tiempos.
    - y_vals: Lista de soluciones y en cada tiempo t.
    """
    t_vals = np.arange(t0, tn + h, h)
    y_vals = [y0]

    for t in t_vals[:-1]:
        y_half = y_vals[-1] + (h / 2) * f(t, y_vals[-1])
        y_next = y_vals[-1] + h * f(t + h/2, y_half)
        y_vals.append(y_next)

    return t_vals, y_vals

# Ejemplo de uso:
def funcion_edo(t, y):
    """
    Define la EDO dy/dt = -y.

    Parameters:
    - t: Tiempo.
    - y: Valor de la función y en el tiempo t.

    Returns:
    - Derivada de y en el tiempo t según la EDO.
    """
    return -y

# Condiciones iniciales y parámetros
y0 = 1.0
t0 = 0.0
tn = 5.0
h = 0.1

# Aplicar el método del punto medio
t_resultado, y_resultado = punto_medio(funcion_edo, y0, t0, tn, h)

# Graficar los resultados
plt.plot(t_resultado, y_resultado, label='Solución numérica')
plt.xlabel('Tiempo (t)')
plt.ylabel('y(t)')
plt.title('Método del Punto Medio para dy/dt = -y')
plt.legend()
plt.show()
