import triangulo
import cuadrado
import linea
import circulo
class borrar():

    @staticmethod
    def del_circle(centro_x,centro_y,radio, matrix):
        circle_points = circulo.Circle.bresenham_circle(centro_x, centro_y, radio)
        for point in circle_points:
            x, y = point
            matrix[y][x] = '  '
        #for row in matrix:
        #    print(' '.join(row))

    @staticmethod
    def del_square(x1, y1, x2, y2,matrix):
        points = []
        points += cuadrado.Square.bresenham(x1, y1, x2, y1)
        points += cuadrado.Square.bresenham(x2, y1, x2, y2)
        points += cuadrado.Square.bresenham(x1, y2, x2, y2)
        points += cuadrado.Square.bresenham(x1, y1, x1, y2)
        for point in points:
            x, y = point
            matrix[x][y] = '  '
        #for row in matrix:
        #    print(' '.join(row))

    @staticmethod
    def del_line(x1,y1,x2,y2,pendiente, matrix):
        line_points = linea.Line.bresenham_line(x1, y1, x2, y2)
        for point in line_points:
            x, y = point
            if pendiente == 1:
                matrix[y][x] = '  '
            else:
                matrix[x][y] = '  '
        #for row in matrix:
        #    print(' '.join(row))

    @staticmethod
    def del_triangle(x1,y1,x2,y2,x3,y3,matrix):
        points = []

        points += triangulo.Triangle.bresenham(x1, y1, x2, y2)
        points += triangulo.Triangle.bresenham(x2, y2, x3, y3)
        points += triangulo.Triangle.bresenham(x3, y3, x1, y1)

        for x, y in points:
            matrix[int(x)][int(y)] = '  '

        #for row in matrix:
        #    print(' '.join(row))

