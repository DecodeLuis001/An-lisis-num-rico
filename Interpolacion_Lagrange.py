def interpolacion_lagrange(x_interp, x_datos, y_datos):
    """
    Método de interpolación de Lagrange para encontrar el valor interpolado en un punto específico.

    Parameters:
    - x_interp: Punto en el cual se desea interpolar.
    - x_datos: Lista de coordenadas x de los puntos conocidos.
    - y_datos: Lista de coordenadas y correspondientes a los puntos conocidos.

    Returns:
    - y_interp: Valor interpolado en el punto x_interp.
    """
    n = len(x_datos)
    y_interp = 0

    for i in range(n):
        termino = y_datos[i]

        for j in range(n):
            if i != j:
                termino *= (x_interp - x_datos[j]) / (x_datos[i] - x_datos[j])

        y_interp += termino

    return y_interp

# Ejemplo de uso:
x_datos = [1, 2, 4]
y_datos = [3, 1, 2]

# Punto en el cual se desea interpolar
x_interp = 3

# Aplicar el método de interpolación de Lagrange
y_interp = interpolacion_lagrange(x_interp, x_datos, y_datos)

print(f"Valor interpolado en x={x_interp}: {y_interp}")
