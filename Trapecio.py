import numpy as np
import matplotlib.pyplot as plt

def metodo_trapecio(f, a, b, n):
    """
    Método del trapecio para aproximar la integral definida de una función.

    Parameters:
    - f: Función a integrar.
    - a: Límite inferior de integración.
    - b: Límite superior de integración.
    - n: Número de subintervalos.

    Returns:
    - Aproximación de la integral definida.
    """
    h = (b - a) / n
    x_vals = np.linspace(a, b, n+1)
    y_vals = f(x_vals)
    
    integral_aproximada = h * (np.sum(y_vals) - 0.5 * (y_vals[0] + y_vals[-1]))
    return integral_aproximada

# Ejemplo de uso:
def funcion_a_integrar(x):
    """
    Función de ejemplo a integrar.

    Parameters:
    - x: Variable de la función.

    Returns:
    - Valor de la función en x.
    """
    return x**2

# Límites de integración
a = 0
b = 2

# Número de subintervalos
n = 4

# Aplicar el método del trapecio
resultado_integral = metodo_trapecio(funcion_a_integrar, a, b, n)

# Mostrar resultados
print(f"Aproximación de la integral definida: {resultado_integral}")

# Graficar la función y el área bajo la curva
x_vals = np.linspace(a, b, 100)
y_vals = funcion_a_integrar(x_vals)

plt.plot(x_vals, y_vals, label='Función a integrar')
plt.fill_between(x_vals, y_vals, color='skyblue', alpha=0.4, label='Área bajo la curva')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Método del Trapecio para la Integración Numérica')
plt.show()
