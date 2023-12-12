import numpy as np
import matplotlib.pyplot as plt

def ajuste_polinomico_minimos_cuadrados(x, y, grado):
    """
    Método de ajuste polinómico por mínimos cuadrados.

    Parameters:
    - x: Lista de coordenadas x de los puntos conocidos.
    - y: Lista de coordenadas y correspondientes a los puntos conocidos.
    - grado: Grado del polinomio a ajustar.

    Returns:
    - coeficientes: Coeficientes del polinomio ajustado.
    """
    # Construir la matriz de Vandermonde
    A = np.vander(x, grado + 1, increasing=True)

    # Resolver el sistema de ecuaciones normales por mínimos cuadrados
    coeficientes, _, _, _ = np.linalg.lstsq(A, y, rcond=None)

    return coeficientes

def evaluar_polinomio(coeficientes, x):
    """
    Evaluar un polinomio dados sus coeficientes.

    Parameters:
    - coeficientes: Coeficientes del polinomio.
    - x: Valor en el cual evaluar el polinomio.

    Returns:
    - Valor del polinomio en x.
    """
    return np.polyval(coeficientes, x)

# Ejemplo de uso:
# Datos de entrada
x_datos = np.array([1, 2, 3, 4, 5])
y_datos = np.array([2.0, 1.5, 0.5, 0.8, 2.0])

# Grado del polinomio a ajustar
grado_polinomio = 2

# Obtener coeficientes del polinomio ajustado
coeficientes_polinomio = ajuste_polinomico_minimos_cuadrados(x_datos, y_datos, grado_polinomio)

# Evaluar el polinomio en un rango de valores
x_evaluacion = np.linspace(min(x_datos), max(x_datos), 100)
y_evaluacion = evaluar_polinomio(coeficientes_polinomio, x_evaluacion)

# Graficar los datos y el polinomio ajustado
plt.scatter(x_datos, y_datos, label='Datos originales')
plt.plot(x_evaluacion, y_evaluacion, label=f'Ajuste Polinómico (grado {grado_polinomio})', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
