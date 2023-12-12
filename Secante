def funcion_objetivo(x):
    """
    Definición de la función objetivo.

    En estadística y probabilidad, esta función podría representar
    una distribución de probabilidad acumulativa o una función de densidad de probabilidad.
    Ajusta la función según tus necesidades.

    Parameters:
    - x: Valor en el que evaluar la función.

    Returns:
    - Valor de la función en x.
    """
    # Ejemplo: Función cuadrática
    return x**2 - 4

def metodo_secante(x0, x1, tol=1e-6, max_iter=100):
    """
    Método de la Secante para encontrar raíces de una función.

    Parameters:
    - x0, x1: Puntos iniciales.
    - tol: Tolerancia para detener el método (por defecto, 1e-6).
    - max_iter: Número máximo de iteraciones (por defecto, 100).

    Returns:
    - root: Aproximación de la raíz.
    - iterations: Número de iteraciones realizadas.
    """
    iterations = 0

    while iterations < max_iter:
        f_x0 = funcion_objetivo(x0)
        f_x1 = funcion_objetivo(x1)

        if abs(f_x1 - f_x0) < tol:
            break

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        x0 = x1
        x1 = x2

        iterations += 1

    return x1, iterations

# Ejemplo de uso:
punto_inicial_1 = 1.0
punto_inicial_2 = 2.0
raiz_aproximada, num_iteraciones = metodo_secante(punto_inicial_1, punto_inicial_2)

print(f"Aproximación de la raíz: {raiz_aproximada}")
print(f"Número de iteraciones: {num_iteraciones}")
