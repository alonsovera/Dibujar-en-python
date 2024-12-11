class Square():

    @staticmethod
    def bresenham(x1, y1, x2, y2):
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

    @staticmethod
    def draw_square(x1, y1, x2, y2,matrix):
        # Crear una matriz de 20x20 con espacios vacíos
        points = []
        points += Square.bresenham(x1, y1, x2, y1)  # Línea superior
        points += Square.bresenham(x2, y1, x2, y2)  # Línea derecha
        points += Square.bresenham(x1, y2, x2, y2)  # Línea inferior
        points += Square.bresenham(x1, y1, x1, y2)


        # Marcar los puntos de las líneas del cuadrado en la matriz
        for point in points:
            x, y = point
            matrix[x][y] = '* '

        # Imprimir la matriz con el cuadrado dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_square90(x1, y1, x2, y2,matrix):
        # Crear una matriz de 20x20 con espacios vacíos
        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(y1 - (b / 2)) + (a / 2)
        y1nuevo = (x1 - (a / 2)) + (b / 2)
        x2nuevo = -(y2 - (b / 2)) + (a / 2)
        y2nuevo = (x2 - (a / 2)) + (b / 2)

        points = []

        points += Square.bresenham(x1nuevo, y1nuevo, x2nuevo, y1nuevo)  # Línea superior
        points += Square.bresenham(x2nuevo, y1nuevo, x2nuevo, y2nuevo)  # Línea derecha
        points += Square.bresenham(x1nuevo, y2nuevo, x2nuevo, y2nuevo)  # Línea inferior
        points += Square.bresenham(x1nuevo, y1nuevo, x1nuevo, y2nuevo)
        for point in points:
            x, y = point
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el cuadrado dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_squareminus90(x1, y1, x2, y2, matrix):
        # Crear una matriz de 20x20 con espacios vacíos
        a = x1 + x2
        b = y1 + y2
        x1nuevo = (y1 - (b / 2)) + (a / 2)
        y1nuevo = -(x1 - (a / 2)) + (b / 2)
        x2nuevo = (y2 - (b / 2)) + (a / 2)
        y2nuevo = -(x2 - (a / 2)) + (b / 2)

        points = []

        points += Square.bresenham(x1nuevo, y1nuevo, x2nuevo, y1nuevo)  # Línea superior
        points += Square.bresenham(x2nuevo, y1nuevo, x2nuevo, y2nuevo)  # Línea derecha
        points += Square.bresenham(x1nuevo, y2nuevo, x2nuevo, y2nuevo)  # Línea inferior
        points += Square.bresenham(x1nuevo, y1nuevo, x1nuevo, y2nuevo)
        for point in points:
            x, y = point
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el cuadrado dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_square180(x1, y1, x2, y2, matrix):
        # Crear una matriz de 20x20 con espacios vacíos
        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(x1 - (a / 2)) + (a / 2)
        y1nuevo = -(y1 - (b / 2)) + (b / 2)
        x2nuevo = -(x2 - (a / 2)) + (a / 2)
        y2nuevo = -(y2 - (b / 2)) + (b / 2)

        points = []

        points += Square.bresenham(x1nuevo, y1nuevo, x2nuevo, y1nuevo)  # Línea superior
        points += Square.bresenham(x2nuevo, y1nuevo, x2nuevo, y2nuevo)  # Línea derecha
        points += Square.bresenham(x1nuevo, y2nuevo, x2nuevo, y2nuevo)  # Línea inferior
        points += Square.bresenham(x1nuevo, y1nuevo, x1nuevo, y2nuevo)
        for point in points:
            x, y = point
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el cuadrado dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_squareminus180(x1, y1, x2, y2, matrix):
        # Crear una matriz de 20x20 con espacios vacíos
        a = x1 + x2
        b = y1 + y2
        x1nuevo = (x1 - (a / 2)) + (a / 2)
        y1nuevo = (y1 - (b / 2)) + (b / 2)
        x2nuevo = (x2 - (a / 2)) + (a / 2)
        y2nuevo = (y2 - (b / 2)) + (b / 2)

        points = []

        points += Square.bresenham(x1nuevo, y1nuevo, x2nuevo, y1nuevo)  # Línea superior
        points += Square.bresenham(x2nuevo, y1nuevo, x2nuevo, y2nuevo)  # Línea derecha
        points += Square.bresenham(x1nuevo, y2nuevo, x2nuevo, y2nuevo)  # Línea inferior
        points += Square.bresenham(x1nuevo, y1nuevo, x1nuevo, y2nuevo)
        for point in points:
            x, y = point
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el cuadrado dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_square270(x1, y1, x2, y2, matrix):
        # Crear una matriz de 20x20 con espacios vacíos
        a = x1 + x2
        b = y1 + y2
        x1nuevo = (y1 - (b / 2)) + (a / 2)
        y1nuevo = -(x1 - (a / 2)) + (b / 2)
        x2nuevo = (y2 - (b / 2)) + (a / 2)
        y2nuevo = -(x2 - (a / 2)) + (b / 2)

        points = []

        points += Square.bresenham(x1nuevo, y1nuevo, x2nuevo, y1nuevo)  # Línea superior
        points += Square.bresenham(x2nuevo, y1nuevo, x2nuevo, y2nuevo)  # Línea derecha
        points += Square.bresenham(x1nuevo, y2nuevo, x2nuevo, y2nuevo)  # Línea inferior
        points += Square.bresenham(x1nuevo, y1nuevo, x1nuevo, y2nuevo)
        for point in points:
            x, y = point
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el cuadrado dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_squareminus270(x1, y1, x2, y2, matrix):
        # Crear una matriz de 20x20 con espacios vacíos
        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(y1 - (b / 2)) + (a / 2)
        y1nuevo = (x1 - (a / 2)) + (b / 2)
        x2nuevo = -(y2 - (b / 2)) + (a / 2)
        y2nuevo = (x2 - (a / 2)) + (b / 2)

        points = []

        points += Square.bresenham(x1nuevo, y1nuevo, x2nuevo, y1nuevo)  # Línea superior
        points += Square.bresenham(x2nuevo, y1nuevo, x2nuevo, y2nuevo)  # Línea derecha
        points += Square.bresenham(x1nuevo, y2nuevo, x2nuevo, y2nuevo)  # Línea inferior
        points += Square.bresenham(x1nuevo, y1nuevo, x1nuevo, y2nuevo)
        for point in points:
            x, y = point
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el cuadrado dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def resize_square(x1,y1,x2,y2, matrix, n):

        if x1<x2 and y1 < y2:
                x1nuevo = x1 - n
                y1nuevo = y1 - n
                x2nuevo = x2 + n
                y2nuevo = y2 + n
        if x1>x2 and y1>y2:
                x1nuevo = x1 + n
                y1nuevo = y1 + n
                x2nuevo = x2 - n
                y2nuevo = y2 - n



        points = []

        points += Square.bresenham(x1nuevo, y1nuevo, x2nuevo, y1nuevo)  # Línea superior
        points += Square.bresenham(x2nuevo, y1nuevo, x2nuevo, y2nuevo)  # Línea derecha
        points += Square.bresenham(x1nuevo, y2nuevo, x2nuevo, y2nuevo)  # Línea inferior
        points += Square.bresenham(x1nuevo, y1nuevo, x1nuevo, y2nuevo)

        for point in points:
            x, y = point
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el cuadrado dibujado
        for row in matrix:
            print(' '.join(row))




