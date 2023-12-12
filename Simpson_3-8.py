import numpy as np
import matplotlib.pyplot as plt

def metodo_simpson_tres_octavos(f, a, b, n):
    """
    Método de Simpson con regla de 3/8 para aproximar la integral definida de una función.

    Parameters:
    - f: Función a integrar.
    - a: Límite inferior de integración.
    - b: Límite superior de integración.
    - n: Número de subintervalos (debe ser múltiplo de 3).

    Returns:
    - Aproximación de la integral definida.
    """
    if n % 3 != 0:
        raise ValueError("El número de subintervalos debe ser múltiplo de 3 para el método de Simpson con regla de 3/8.")

    h = (b - a) / n
    x_vals = np.linspace(a, b, n+1)
    y_vals = f(x_vals)
    
    suma_parcial_1 = np.sum(y_vals[1:-1:3])
    suma_parcial_2 = np.sum(y_vals[2:-1:3])
    suma_parcial_3 = np.sum(y_vals[3:-1:3])
    
    integral_aproximada = (3 * h / 8) * (y_vals[0] + 3 * suma_parcial_1 + 3 * suma_parcial_2 + 2 * suma_parcial_3 + y_vals[-1])
    
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

# Número de subintervalos (debe ser múltiplo de 3)
n = 6

# Aplicar el método de Simpson con regla de 3/8
resultado_integral = metodo_simpson_tres_octavos(funcion_a_integrar, a, b, n)

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
plt.title('Método de Simpson con Regla de 3/8 para la Integración Numérica')
plt.show()
