class Triangle():
    space_size = 20

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

        #for x in range(x1, x2 + 1):
        for x in range(int(x1), int(x2) + 1):
            coord = (x, y) if steep else (y, x)
            points.append(coord)

            if decision > 0:
                y += ystep
                decision -= 2 * dx

            decision += 2 * dy

        return points

    # Espacio de 20x20

    @staticmethod
    def draw_triangle(x1, y1, x2, y2, x3, y3, matrix):
        points = []

        # Obtener los puntos de las líneas del triángulo utilizando el algoritmo de Bresenham
        points += Triangle.bresenham(x1, y1, x2, y2)
        points += Triangle.bresenham(x2, y2, x3, y3)
        points += Triangle.bresenham(x3, y3, x1, y1)

        # Marcar los puntos de las líneas del triángulo en la matriz
        for x, y in points:
            matrix[x][y] = '* '
            # CAMBIAR a matrix[x][y]

        # Imprimir la matriz con el triángulo dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_triangle90(x1, y1, x2, y2, x3, y3, matrix):
        # Intercambiar las coordenadas x e y para girar el triángulo 90 grados
        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(y1 - (b / 2)) + (a / 2)
        y1nuevo = (x1 - (a / 2)) + (b / 2)
        x2nuevo = -(y2 - (b / 2)) + (a / 2)
        y2nuevo = (x2 - (a / 2)) + (b / 2)
        x3nuevo = -(y3 - (b / 2)) + (a / 2)
        y3nuevo = (x3 - (a / 2)) + (b / 2)

        points = []

        # Obtener los puntos de las líneas del triángulo utilizando el algoritmo de Bresenham
        points += Triangle.bresenham(x1nuevo, y1nuevo, x2nuevo, y2nuevo)
        points += Triangle.bresenham(x2nuevo, y2nuevo, x3nuevo, y3nuevo)
        points += Triangle.bresenham(x3nuevo, y3nuevo, x1nuevo, y1nuevo)

        # Marcar los puntos de las líneas del triángulo en la matriz
        for x, y in points:
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el triángulo dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_triangle180(x1, y1, x2, y2, x3, y3, matrix):
        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(x1 - (a / 2)) + (a / 2)
        y1nuevo = -(y1 - (b / 2)) + (b / 2)
        x2nuevo = -(x2 - (a / 2)) + (a / 2)
        y2nuevo = -(y2 - (b / 2)) + (b / 2)
        x3nuevo = -(x3 - (a / 2)) + (a / 2)
        y3nuevo = -(y3 - (b / 2)) + (b / 2)

        points = []

        # Obtener los puntos de las líneas del triángulo utilizando el algoritmo de Bresenham
        points += Triangle.bresenham(x1nuevo, y1nuevo, x2nuevo, y2nuevo)
        points += Triangle.bresenham(x2nuevo, y2nuevo, x3nuevo, y3nuevo)
        points += Triangle.bresenham(x3nuevo, y3nuevo, x1nuevo, y1nuevo)

        # Marcar los puntos de las líneas del triángulo en la matriz
        for x, y in points:
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el triángulo dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_triangle270(x1, y1, x2, y2, x3, y3, matrix):
        a = x1 + x2
        b = y1 + y2
        x1nuevo = (y1 - (b / 2)) + (a / 2)
        y1nuevo = -(x1 - (a / 2)) + (b / 2)
        x2nuevo = (y2 - (b / 2)) + (a / 2)
        y2nuevo = -(x2 - (a / 2)) + (b / 2)
        x3nuevo = (y3 - (b / 2)) + (a / 2)
        y3nuevo = -(x3 - (a / 2)) + (b / 2)

        points = []

        # Obtener los puntos de las líneas del triángulo utilizando el algoritmo de Bresenham
        points += Triangle.bresenham(x1nuevo, y1nuevo, x2nuevo, y2nuevo)
        points += Triangle.bresenham(x2nuevo, y2nuevo, x3nuevo, y3nuevo)
        points += Triangle.bresenham(x3nuevo, y3nuevo, x1nuevo, y1nuevo)

        # Marcar los puntos de las líneas del triángulo en la matriz
        for x, y in points:
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el triángulo dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def resize_triangle(x1, y1, x2, y2, x3, y3, matrix, n):
        if x1 == x3:
            if (x2 > x1) and (y1 < y2):
                x1_new = x1 - n + 1
                y1_new = y1 - n
                x2_new = x2 + n + 1
                y2_new = y2 + n
                x3_new = x3 - n + 1
                y3_new = y3 + n
            elif (x2 < x1) and (y1 < y2):
                x1_new = x1 + n -1
                y1_new = y1 - n
                x2_new = x2 - n - 1
                y2_new = y2 + n
                x3_new = x3 + n -1
                y3_new = y3 + n

        elif x2 == x3:
            #YA ESTÁ
            if (x1 < x2) and (y1 < y2):
                x1_new = x1 - n
                y1_new = y1 - n + 1
                x2_new = x2 + n
                y2_new = y2 + n + 1
                x3_new = x3 + n
                y3_new = y3 - n + 1
            #YA ESTÁ
            elif (x2 < x1) and (y1 < y2):
                x1_new = x1 + n
                y1_new = y1 - n + 1
                x2_new = x2 - n
                y2_new = y2 + n + 1
                x3_new = x3 - n
                y3_new = y3 - n + 1


        elif x1 == x2:
            if (y1> y2):
                x1_new = x1 + 1
                y1_new = y1 - n
                x2_new = x2 + 1
                y2_new = y2 + n
                x3_new = x3 - n + 1
                y3_new = y3
            elif y2> y1:
                x1_new = x1 - 1
                y1_new = y1 - n
                x2_new = x2 - 1
                y2_new = y2 + n
                x3_new = x3 + n - 1
                y3_new = y3

        points = []

        # Obtener los puntos de las líneas del triángulo utilizando el algoritmo de Bresenham
        points += Triangle.bresenham(x1_new, y1_new, x2_new, y2_new)
        points += Triangle.bresenham(x2_new, y2_new, x3_new, y3_new)
        points += Triangle.bresenham(x3_new, y3_new, x1_new, y1_new)

        # Marcar los puntos de las líneas del triángulo en la matriz
        for x, y in points:
            matrix[x][y] = '* '
            # CAMBIAR a matrix[x][y]

        # Imprimir la matriz con el triángulo dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_triangleminus90(x1, y1, x2, y2, x3, y3, matrix):
        # Intercambiar las coordenadas x e y para girar el triángulo -90 grados
        a = x1 + x2
        b = y1 + y2
        x1nuevo = (y1 - (b / 2)) + (a / 2)
        y1nuevo = -(x1 - (a / 2)) + (b / 2)
        x2nuevo = (y2 - (b / 2)) + (a / 2)
        y2nuevo = -(x2 - (a / 2)) + (b / 2)
        x3nuevo = (y3 - (b / 2)) + (a / 2)
        y3nuevo = -(x3 - (a / 2)) + (b / 2)

        points = []

        # Obtener los puntos de las líneas del triángulo utilizando el algoritmo de Bresenham
        points += Triangle.bresenham(x1nuevo, y1nuevo, x2nuevo, y2nuevo)
        points += Triangle.bresenham(x2nuevo, y2nuevo, x3nuevo, y3nuevo)
        points += Triangle.bresenham(x3nuevo, y3nuevo, x1nuevo, y1nuevo)

        # Marcar los puntos de las líneas del triángulo en la matriz
        for x, y in points:
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el triángulo dibujado
        for row in matrix:
            print(' '.join(row))

    @staticmethod
    def draw_triangleminus180(x1, y1, x2, y2, x3, y3, matrix):
        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(x1 - (a / 2)) + (a / 2)
        y1nuevo = -(y1 - (b / 2)) + (b / 2)
        x2nuevo = -(x2 - (a / 2)) + (a / 2)
        y2nuevo = -(y2 - (b / 2)) + (b / 2)
        x3nuevo = -(x3 - (a / 2)) + (a / 2)
        y3nuevo = -(y3 - (b / 2)) + (b / 2)

        points = []

        # Obtener los puntos de las líneas del triángulo utilizando el algoritmo de Bresenham
        points += Triangle.bresenham(x1nuevo, y1nuevo, x2nuevo, y2nuevo)
        points += Triangle.bresenham(x2nuevo, y2nuevo, x3nuevo, y3nuevo)
        points += Triangle.bresenham(x3nuevo, y3nuevo, x1nuevo, y1nuevo)

        # Marcar los puntos de las líneas del triángulo en la matriz
        for x, y in points:
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el triángulo dibujado
        for row in matrix:
            print(' '.join(row))
    @staticmethod
    def draw_triangleminus270(x1, y1, x2, y2, x3, y3, matrix):
        a = x1 + x2
        b = y1 + y2
        x1nuevo = -(y1 - (b / 2)) + (a / 2)
        y1nuevo = (x1 - (a / 2)) + (b / 2)
        x2nuevo = -(y2 - (b / 2)) + (a / 2)
        y2nuevo = (x2 - (a / 2)) + (b / 2)
        x3nuevo = -(y3 - (b / 2)) + (a / 2)
        y3nuevo = (x3 - (a / 2)) + (b / 2)

        points = []

        # Obtener los puntos de las líneas del triángulo utilizando el algoritmo de Bresenham
        points += Triangle.bresenham(x1nuevo, y1nuevo, x2nuevo, y2nuevo)
        points += Triangle.bresenham(x2nuevo, y2nuevo, x3nuevo, y3nuevo)
        points += Triangle.bresenham(x3nuevo, y3nuevo, x1nuevo, y1nuevo)

        # Marcar los puntos de las líneas del triángulo en la matriz
        for x, y in points:
            matrix[int(x)][int(y)] = '* '

        # Imprimir la matriz con el triángulo dibujado
        for row in matrix:
            print(' '.join(row))
