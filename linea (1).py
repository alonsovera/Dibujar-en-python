# line
class Line():
    @staticmethod
    def bresenham_line(x1, y1, x2, y2):
        dx = abs(int(x2) - int(x1))
        dy = abs(int(y2) - int(y1))
        steep = dy > dx

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
            dx, dy = dy, dx

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        y = y1
        ystep = 1 if y1 < y2 else -1

        decision = 2 * dy - dx
        points = []

        for x in range(int(x1), int(x2) + 1):
            coord = (x, y) if steep else (y, x)
            points.append(coord)

            if decision > 0:
                y += ystep
                decision -= 2 * dx

            decision += 2 * dy

        return points

    # Espacio de 20x20
    space_size = 20
    @staticmethod
    def draw_line90(x1,y1,x2,y2, pendiente,matrix):

        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(y1 - (b / 2)) + (a / 2)
        y1nuevo = (x1 - (a / 2)) + (b / 2)
        x2nuevo = -(y2 - (b / 2)) + (a / 2)
        y2nuevo = (x2 - (a / 2)) + (b / 2)
        line_points = Line.bresenham_line(x1nuevo, y1nuevo, x2nuevo, y2nuevo)

        # Marcar los puntos de la línea en la matriz
        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[int(y)][int(x)] = '* '
            else:
                matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con la línea dibujada
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_lineminus90(x1, y1, x2, y2, pendiente, matrix):

        a = x1 + x2
        b = y1 + y2
        x1nuevo = (y1 - (b / 2)) + (a / 2)
        y1nuevo = -(x1 - (a / 2)) + (b / 2)
        x2nuevo = (y2 - (b / 2)) + (a / 2)
        y2nuevo = -(x2 - (a / 2)) + (b / 2)
        line_points = Line.bresenham_line(x1nuevo, y1nuevo, x2nuevo, y2nuevo)

        # Marcar los puntos de la línea en la matriz
        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[int(y)][int(x)] = '* '
            else:
                matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con la línea dibujada
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_line180(x1, y1, x2, y2, pendiente, matrix):

        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(x1 - (a / 2)) + (a / 2)
        y1nuevo = -(y1 - (b / 2)) + (b / 2)
        x2nuevo = -(x2 - (a / 2)) + (a / 2)
        y2nuevo = -(y2 - (b / 2)) + (b / 2)
        line_points = Line.bresenham_line(x1nuevo, y1nuevo, x2nuevo, y2nuevo)

        # Marcar los puntos de la línea en la matriz
        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[int(y)][int(x)] = '* '
            else:
                matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con la línea dibujada
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_lineminus180(x1, y1, x2, y2, pendiente, matrix):

        a = x1 + x2
        b = y1 + y2
        x1nuevo = (x1 - (a / 2)) + (a / 2)
        y1nuevo = (y1 - (b / 2)) + (b / 2)
        x2nuevo = (x2 - (a / 2)) + (a / 2)
        y2nuevo = (y2 - (b / 2)) + (b / 2)
        line_points = Line.bresenham_line(x1nuevo, y1nuevo, x2nuevo, y2nuevo)

        # Marcar los puntos de la línea en la matriz
        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[int(y)][int(x)] = '* '
            else:
                matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con la línea dibujada
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_line270(x1, y1, x2, y2, pendiente, matrix):

        a = x1 + x2
        b = y1 + y2
        x1nuevo = (y1 - (b / 2)) + (a / 2)
        y1nuevo = -(x1 - (a / 2)) + (b / 2)
        x2nuevo = (y2 - (b / 2)) + (a / 2)
        y2nuevo = -(x2 - (a / 2)) + (b / 2)
        line_points = Line.bresenham_line(x1nuevo, y1nuevo, x2nuevo, y2nuevo)

        # Marcar los puntos de la línea en la matriz
        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[int(y)][int(x)] = '* '
            else:
                matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con la línea dibujada
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_lineminus270(x1, y1, x2, y2, pendiente, matrix):

        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(y1 - (b / 2)) + (a / 2)
        y1nuevo = (x1 - (a / 2)) + (b / 2)
        x2nuevo = -(y2 - (b / 2)) + (a / 2)
        y2nuevo = (x2 - (a / 2)) + (b / 2)
        line_points = Line.bresenham_line(x1nuevo, y1nuevo, x2nuevo, y2nuevo)

        # Marcar los puntos de la línea en la matriz
        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[int(y)][int(x)] = '* '
            else:
                matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con la línea dibujada
        for row in matrix:
            print(' '.join(row))

    # Coordenadas de la línea

    # Escalar las coordenadas al espacio de 20x20
    @staticmethod
    def draw_line(x1, y1, x2, y2, pendiente, matrix):
        # Obtener los puntos de la línea utilizando el algoritmo de Bresenham
        line_points = Line.bresenham_line(x1, y1, x2, y2)

        # Marcar los puntos de la línea en la matriz
        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[x][y] = '* '
            else:
                matrix[x][y] = '* '

        # Imprimir la matriz con la línea dibujada
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def resize_line(x1,y1,x2,y2, pendiente,matrix, n):
        if y1 == y2:
            if x1 < x2:
                x1nuevo = x1 - n
                y1nuevo = y1
                x2nuevo = x2 + n
                y2nuevo = y2
            elif x1 > x2:
                x1nuevo = x1 + n
                y1nuevo = y1
                x2nuevo = x2 - n
                y2nuevo = y2
        elif x1 == x2:
            if y1 < y2:
                x1nuevo = x1
                y1nuevo = y1 - n
                x2nuevo = x2
                y2nuevo = y2+n
            elif y1 > y2:
                x1nuevo = x1
                y1nuevo = y1 + n
                x2nuevo = x2
                y2nuevo = y2 - n
        elif x1 < x2 and y1 < y2:
                x1nuevo = x1 - n
                y1nuevo = y1 - n
                x2nuevo = x2 + n
                y2nuevo = y2 + n
        elif x1 > x2 and y1 > y2:
                x1nuevo = x1 + n
                y1nuevo = y1 + n
                x2nuevo = x2 - n
                y2nuevo = y2 - n
        elif x1 < x2 and y1 > y2:
                x1nuevo = x1 - n
                y1nuevo = y1 + n
                x2nuevo = x2 + n
                y2nuevo = y2 - n
        elif x1 > x2 and y1 < y2:
                x1nuevo = x1 + n
                y1nuevo = y1 - n
                x2nuevo = x2 - n
                y2nuevo = y2 + n
        line_points = Line.bresenham_line(x1nuevo, y1nuevo, x2nuevo, y2nuevo)

        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[y][x] = '* '
            else:
                matrix[x][y] = '* '

        # Imprimir la matriz con la línea dibujada
        for row in matrix:
            print(' '.join(row))







