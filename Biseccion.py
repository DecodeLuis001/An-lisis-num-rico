def funcion_objetivo(x):
    """
    Definición de la función objetivo.

    En este ejemplo, usaremos una función simple.
    Puedes cambiar esta función según tus necesidades.
    """
    return x**2 - 4

def metodo_biseccion(a, b, tol=1e-6, max_iter=100):
    """
    Método de la Bisección para encontrar la raíz de una función.

    Parámetros:
    - a, b: Intervalo [a, b] donde se busca la raíz.
    - tol: Tolerancia para detener el método (por defecto, 1e-6).
    - max_iter: Número máximo de iteraciones (por defecto, 100).

    Retorna:
    - root: Aproximación de la raíz.
    - iterations: Número de iteraciones realizadas.
    """
    if funcion_objetivo(a) * funcion_objetivo(b) > 0:
        raise ValueError("La función no cambia de signo en el intervalo dado.")

    root = None
    iterations = 0

    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2
        if funcion_objetivo(c) == 0:
            root = c
            break
        elif funcion_objetivo(c) * funcion_objetivo(a) < 0:
            b = c
        else:
            a = c
        iterations += 1

    if root is None:
        root = (a + b) / 2

    return root, iterations

# Ejemplo de uso:
intervalo_a = 0
intervalo_b = 3
raiz_aproximada, num_iteraciones = metodo_biseccion(intervalo_a, intervalo_b)

print(f"Aproximación de la raíz: {raiz_aproximada}")
print(f"Número de iteraciones: {num_iteraciones}")
