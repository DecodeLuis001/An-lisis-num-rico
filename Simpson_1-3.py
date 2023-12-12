import numpy as np
import matplotlib.pyplot as plt

def metodo_simpson_un_tercio(f, a, b, n):
    """
    Método de Simpson con regla de 1/3 para aproximar la integral definida de una función.

    Parameters:
    - f: Función a integrar.
    - a: Límite inferior de integración.
    - b: Límite superior de integración.
    - n: Número de subintervalos (debe ser par).

    Returns:
    - Aproximación de la integral definida.
    """
    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par para el método de Simpson con regla de 1/3.")

    h = (b - a) / n
    x_vals = np.linspace(a, b, n+1)
    y_vals = f(x_vals)
    
    integral_aproximada = (h / 3) * (y_vals[0] + 4 * np.sum(y_vals[1:-1:2]) + 2 * np.sum(y_vals[2:-2:2]) + y_vals[-1])
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

# Número de subintervalos (debe ser par)
n = 4

# Aplicar el método de Simpson con regla de 1/3
resultado_integral = metodo_simpson_un_tercio(funcion_a_integrar, a, b, n)

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
plt.title('Método de Simpson con Regla de 1/3 para la Integración Numérica')
plt.show()
