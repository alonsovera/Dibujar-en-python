class Circle():
    @staticmethod
    def bresenham_circle(center_x, center_y, radius):
        x = 0
        y = radius
        decision = 3 - 2 * radius
        points = []

        while x <= y:
            points.append((x, y))
            points.append((y, x))
            points.append((-x, y))
            points.append((-y, x))
            points.append((-x, -y))
            points.append((-y, -x))
            points.append((x, -y))
            points.append((y, -x))

            if decision < 0:
                decision += 4 * x + 6
            else:
                decision += 4 * (x - y) + 10
                y -= 1
            x += 1

        # Trasladar los puntos al centro del círculo
        points = [(center_x + x, center_y + y) for (x, y) in points]

        return points

    # Espacio de 20x20
    space_size = 20
    @staticmethod
    def draw_circle(centro_x,centro_y,radio, matrix):
        # Obtener los puntos del círculo utilizando el algoritmo de Bresenham
        circle_points = Circle.bresenham_circle(centro_x, centro_y, radio)

        # Marcar los puntos del círculo en la matriz
        for point in circle_points:
            x, y = point
            matrix[y][x] = '* '

        # Imprimir la matriz con el círculo dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def resize_circle(centro_x,centro_y,radio, matrix, n):

        radionuevo = radio + n

        circle_points = Circle.bresenham_circle(centro_x, centro_y, radionuevo)

        # Marcar los puntos del círculo en la matriz
        for point in circle_points:
            x, y = point
            matrix[y][x] = '* '

        # Imprimir la matriz con el círculo dibujado
        for row in matrix:
            print(' '.join(row))
