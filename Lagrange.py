def polinomio_lagrange(x_vals, y_vals):
    """
    Método de Lagrange para interpolar un polinomio a través de un conjunto de puntos.

    Parameters:
    - x_vals: Lista de coordenadas x de los puntos conocidos.
    - y_vals: Lista de coordenadas y correspondientes a los puntos conocidos.

    Returns:
    - polinomio: Función polinómica interpolante en forma simbólica.
    """
    from sympy import symbols, expand, simplify

    # Definir símbolos
    x = symbols('x')

    # Número de puntos
    n = len(x_vals)

    # Inicializar el polinomio
    polinomio = 0

    for i in range(n):
        termino = y_vals[i]

        for j in range(n):
            if i != j:
                termino *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])

        polinomio += termino

    # Expandir y simplificar el polinomio resultante
    polinomio = expand(polinomio)
    polinomio = simplify(polinomio)

    return polinomio

# Ejemplo de uso:
x_datos = [1, 2, 4]
y_datos = [3, 1, 2]

polinomio_interpolante = polinomio_lagrange(x_datos, y_datos)
print(f"Polinomio interpolante: {polinomio_interpolante}")
