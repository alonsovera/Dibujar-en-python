import circulo
import triangulo
import cuadrado
import linea
import borrar
figuras = [ ]
figuras1 = [ ]

F1 = ["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "11", "12", "13", "14", "15", "16", "17", "18",
      "19", "20", "  "]
F2 = [" 1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
      "  ", "  ", " 1"]
F3 = [" 2", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
      "  ", "  ", " 2"]
F4 = [" 3", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
      "  ", "  ", " 3"]
F5 = [" 4", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
      "  ", "  ", " 4"]
F6 = [" 5", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
      "  ", "  ", " 5"]
F7 = [" 6", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
      "  ", "  ", " 6"]
F8 = [" 7", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
      "  ", "  ", " 7"]
F9 = [" 8", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
      "  ", "  ", " 8"]
F10 = [" 9", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", " 9"]
F11 = ["10", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "10"]
F12 = ["11", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "11"]
F13 = ["12", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "12"]
F14 = ["13", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "13"]
F15 = ["14", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "14"]
F16 = ["15", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "15"]
F17 = ["16", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "16"]
F18 = ["17", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "17"]
F19 = ["18", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "18"]
F20 = ["19", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "19"]
F21 = ["20", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
       "  ", "  ", "20"]
F22 = ["  ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "11", "12", "13", "14", "15", "16", "17", "18",
       "19", "20", "  "]

matriz = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10,
                  F11, F12, F13, F14, F15, F16, F17, F18, F19, F20,
                  F21, F22]





first = input()
if first == "init":
    print("Welcome to the gimp xyz")
    for row in matriz:
        print(' '.join(row))

while True:
    decision1 = input("$ Operations Show, Add, Delete, Rotate or Resize \n")

    if decision1 == "DELETE":
        decision3 = int(input("Tag: ")) #Tag
        decision2 = decision3 - 1 #Elemento en la lista de Python
        if len(figuras) > 0:
            if decision2 < 0 or decision2 > len(figuras):
                print("El número de figura es inválido")
                continue

            if figuras[decision2][1] == 'Círculo':
                print("CIRCULO")
                for i in range(len(figuras1)):
                    if figuras1[i][0] == str(decision3):
                        borrar.borrar.del_circle(figuras1[i][1],figuras1[i][2], figuras1[i][3], matriz)
                        figuras.pop(decision3-1)
                        figuras1.pop(decision3-1)
                        break
                else:
                    print("No hay nada que mostrar")

            elif figuras[decision2][1] == 'Cuadrado':
                print("CUADRADO")
                for i in range(len(figuras1)):
                    if figuras1[i][0] == str(decision3):
                        borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                        figuras.pop(decision3-1)
                        figuras1.pop(decision3-1)
                        break
                else:
                    print("No hay nada que mostrar")

            elif figuras[decision2][1] == 'Línea':
                print("LINEA")
                for i in range(len(figuras1)):
                    if figuras1[i][0] == str(decision3):
                        borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], figuras1[i][5], matriz)
                        figuras.pop(decision3-1)
                        figuras1.pop(decision3 - 1)

                        break
                else:
                    print("No hay nada que mostrar")


            elif figuras[decision2][1] == 'Triángulo':

                print("TRIANGULO")

                if decision3 >= 1 and decision3 <= len(figuras1):

                    for i in range(len(figuras1)):

                        if figuras1[i][0] == str(decision3):
                            borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                       figuras1[i][5], figuras1[i][6], matriz)

                            figuras.pop(decision3 - 1)

                            figuras1.pop(decision3 - 1)

                            break

                else:

                    print("El valor de decision3 está fuera del rango válido.")

            for i in range(len(figuras)):
                if i >= decision2:
                    figuras[i][0] = str(int(figuras[i][0]) - 1)
                    figuras1[i][0] = str(int(figuras1[i][0])-1)
            for i in range(len(figuras)):
                if figuras[i][1] == "Cuadrado":
                    borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4], matriz)
                    cuadrado.Square.draw_square(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4], matriz)
                elif figuras[i][1] == "Círculo":
                    borrar.borrar.del_circle(figuras1[i][1], figuras1[i][2], figuras1[i][3], matriz)
                    circulo.Circle.draw_circle(figuras1[i][1], figuras1[i][2], figuras1[i][3], matriz)
                elif figuras[i][1] == 'Línea':
                    borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                           figuras1[i][5], matriz)
                    linea.Line.draw_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                         figuras1[i][5], matriz)
                elif figuras[i][1] == "Triángulo":
                    borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                               figuras1[i][5], figuras1[i][6], matriz)
                    triangulo.Triangle.draw_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                     figuras1[i][5], figuras1[i][6], matriz)




        else:
            print("No hay figuras para eliminar")


    elif decision1 == "ADD"  :
        if len(figuras) >= 5:
            print("YA HAY 5 FIGURAS.")
            continue
        decision2 = input()
        decision3 = decision2.upper()
        print(decision3)
        if decision3 == 'CIRCULO':
            centrox = int(input("Centro x: "))
            centroy = int(input("Centro y: "))
            radio = int(input("Radio: "))
            if centrox < 1 or centrox > 20 or centroy < 1 or centroy > 20 or radio < 1 or radio > 11:
                print("Invalid operation")
                continue
            circulo.Circle.draw_circle(centrox, centroy, radio, matriz)
            figuras1.append([str(len(figuras1)+1), centrox, centroy, radio])
            #print(figuras1)
            figuras.append([str(len(figuras) + 1),"Círculo", centrox, centroy, radio])
        elif decision3 == 'TRIANGULO':
            x1 = int(input("x1 :"))
            y1 = int(input("y1: "))
            x2 = int(input("x2: "))
            y2 = int(input("y2: "))
            x3 = int(input("x3: "))
            y3 = int(input("y3: "))
            if any(coordenada < 1 or coordenada > 20 for coordenada in [x1, y1, x2, y2, x3, y3]):
                print("Invalid operation")
                continue
            triangulo.Triangle.draw_triangle(x1, y1, x2, y2, x3, y3, matriz)
            figuras1.append([str(len(figuras1)+1),x1,y1,x2,y2,x3,y3])
            #figuras.append(
             #   [str(len(figuras) + 1), "Triángulo", f"Coordenadas: ({x1}, {y1}), ({x2}, {y2}), ({x3}, {y3})"])
            figuras.append([str(len(figuras) + 1), "Triángulo", x1, y1, x2, y2, x3, y3])
        elif decision3 == 'CUADRADO':
            x1 = int(input("x1: "))
            y1 = int(input("y1: "))
            x2 = int(input("x2: "))
            y2 = int(input("y2: "))
            if any(coordenada < 1 or coordenada > 20 for coordenada in [x1, y1, x2, y2]):
                print("Invalid operation")
                continue
            #figrascuadrado.append([str(len(figuras)+1), x1 , y1 , x2 , y2])
            #print(figrascuadrado)
            figuras1.append([str(len(figuras1)+1),x1,y1,x2,y2])
            cuadrado.Square.draw_square(x1, y1, x2, y2, matriz)
            #figuras.append([str(len(figuras) + 1), "Cuadrado", f"Coordenadas: ({x1}, {y1}), ({x2}, {y2})"])
            figuras.append([str(len(figuras) + 1), "Cuadrado", x1, y1, x2, y2])

        elif decision3 == 'LINEA':
            x1 = int(input("x1: "))
            y1 = int(input("y1: "))
            x2 = int(input("x2: "))
            y2 = int(input("y2: "))
            if any(coordenada < 1 or coordenada > 20 for coordenada in [x1, y1, x2, y2]):
                print("Invalid operation")
                continue
            if x1 != x2:
                pendiente1 = (y2 - y1) / (x2 - x1)
            else:
                pendiente1 = float('inf')  # Valor especial para líneas verticales
            #figuraslinea.append([str(len(figuras)+1), x1, y1, x2, y2, pendiente1])
            linea.Line.draw_line(x1, y1, x2, y2, pendiente1, matriz)
            figuras1.append([str(len(figuras1)+1),x1,y1,x2,y2,pendiente1])
            #figuras.append([str(len(figuras) + 1), "Línea", f"Coordenadas: ({x1}, {y1}), ({x2}, {y2})"])
            figuras.append([str(len(figuras) + 1), "Línea", x1, y1, x2, y2])
        else:
            print("INCORRECTO. TIPO DE FIGURA NO ENCONTRADA")

    elif decision1 == "SHOW":
        print("Número  | Tipo        | Datos")
        for figura in figuras:
            print("{:<8}| {:<10} | {:<20}".format(figura[0], figura[1], figura[2]))

        print(figuras)
        print(figuras1)
        
        for row in matriz:
            print(' '.join(row))


    elif decision1 == "RESIZE":
        n = int(input())
        decision8 = int(input())
        decision9 = decision8 - 1
        if len(figuras) > 0:
            if decision9 < 0 or decision9 > len(figuras):
                print("El número de figura es inválido")
                continue
            figuras[decision9][1]
            if figuras[decision9][1] == 'Línea':
                print("LINEA")
                if 1 <= decision8 <= len(figuras1):
                    for i in range(len(figuras1)):
                        if figuras1[i][0] == str(decision8):
                            borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            linea.Line.resize_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz, n)

                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            if y1 == y2:
                                if x1 < x2:
                                    figuras1[i][1] = x1 - n
                                    figuras1[i][2] = y1
                                    figuras1[i][3] = x2 + n
                                    y2 = figuras1[i][4] = y2
                                elif x1 > x2:
                                    figuras1[i][1] = x1 + n
                                    figuras1[i][2] = y1
                                    figuras1[i][3] = x2 - n
                                    y2 = figuras1[i][4] = y2
                            elif x1 == x2:
                                if y1 < y2:
                                    figuras1[i][1] = x1
                                    figuras1[i][2] = y1 - n
                                    figuras1[i][3] = x2
                                    y2 = figuras1[i][4] = y2 + n
                                elif y1 > y2:
                                    figuras1[i][1] = x1
                                    figuras1[i][2] = y1 + n
                                    figuras1[i][3] = x2
                                    y2 = figuras1[i][4] = y2 - n
                            elif x1 < x2 and y1 < y2:
                                figuras1[i][1] = x1 - n
                                figuras1[i][2] = y1 - n
                                figuras1[i][3] = x2 + n
                                y2 = figuras1[i][4] = y2 + n
                            elif x1 > x2 and y1 > y2:
                                figuras1[i][1] = x1 + n
                                figuras1[i][2] = y1 + n
                                figuras1[i][3] = x2 - n
                                y2 = figuras1[i][4] = y2 - n
                            elif x1 < x2 and y1 > y2:
                                figuras1[i][1] = x1 - n
                                figuras1[i][2] = y1 + n
                                figuras1[i][3] = x2 + n
                                y2 = figuras1[i][4] = y2 - n
                            elif x1 > x2 and y1 < y2:
                                figuras1[i][1] = x1 + n
                                figuras1[i][2] = y1 - n
                                figuras1[i][3] = x2 - n
                                y2 = figuras1[i][4] = y2 + n


            if figuras[decision9][1] == 'Cuadrado':
                print("CUADRADO")
                if 1 <= decision8 <= len(figuras1):
                    for i in range(len(figuras1)):
                        if figuras1[i][0] == str(decision8):
                            borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            cuadrado.Square.resize_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz, n)

                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            """
                            limite1 = x1 - n
                            limite2 = y1 - n
                            limite3 = x2 + n
                            limite4 = y2 + n

                            if limite1 < 0 or limite2 < 0 or limite3 > 20 or limite4 > I20 :
                                print("Invalid operation.")
                                break
                            """

                            if x1 < x2 and y1 < y2:
                                    figuras1[i][1] = x1 - n
                                    figuras1[i][2] = y1 - n
                                    figuras1[i][3] = x2 + n
                                    figuras1[i][4] = y2 + n
                            if x1 > x2 and y1 > y2:
                                    figuras1[i][1] = x1 + n
                                    figuras1[i][2] = y1 + n
                                    figuras1[i][3] = x2 - n
                                    figuras1[i][4] = y2 - n
            if figuras[decision9][1] == 'Círculo':
                print("CIRCULO")
                if 1 <= decision8 <= len(figuras1):
                    for i in range(len(figuras1)):
                        if figuras1[i][0] == str(decision8):
                            r = figuras1[i][3] # r
                            x = figuras1[i][1] # x
                            y = figuras1[i][2] # y
                            j = x - r
                            k = j - n
                            l = x + r
                            m = l + n
                            o = y - r
                            p = o - n
                            q = y + r
                            s = q + n


                            #k = k + figuras1[i][3]
                            """print(j)
                            print(k)"""
                            if k < 1 or m > 20 or p <=0 or s > 20 :
                                print("Invalid operation.")
                                break



                            borrar.borrar.del_circle(figuras1[i][1], figuras1[i][2], figuras1[i][3], matriz)
                            circulo.Circle.resize_circle(figuras1[i][1], figuras1[i][2], figuras1[i][3], matriz,n)

                            figuras1[i][3] = figuras1[i][3] + n

            if figuras[decision9][1] == 'Triángulo':
                print("TRIANGULO")
                if 1 <= decision8 <= len(figuras1):
                    for i in range(len(figuras1)):
                        if figuras1[i][0] == str(decision8):

                            borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                       figuras1[i][5], figuras1[i][6], matriz)
                            triangulo.Triangle.resize_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3],
                                                               figuras1[i][4],figuras1[i][5], figuras1[i][6], matriz, n)

                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]




                            if x1 == x3:
                                if (x2 > x1) and (y1 < y2):
                                    figuras1[i][1] = x1 - n + 1
                                    figuras1[i][2] = y1 - n
                                    figuras1[i][3] = x2 + n + 1
                                    figuras1[i][4] = y2 + n
                                    figuras1[i][5] = x3 - n + 1
                                    figuras1[i][6] = y3 + n
                                elif (x2 < x1) and (y1 < y2):
                                    figuras1[i][1] = x1 + n - 1
                                    figuras1[i][2] = y1 - n
                                    figuras1[i][3] = x2 - n - 1
                                    figuras1[i][4] = y2 + n
                                    figuras1[i][5] = x3 + n - 1
                                    figuras1[i][6] = y3 + n

                            elif x2 == x3:
                                # YA ESTÁ
                                if (x1 < x2) and (y1 < y2):
                                    figuras1[i][1] = x1 - n
                                    figuras1[i][2] = y1 - n + 1
                                    figuras1[i][3] = x2 + n
                                    figuras1[i][4] = y2 + n + 1
                                    figuras1[i][5] = x3 + n
                                    figuras1[i][6] = y3 - n + 1
                                # YA ESTÁ
                                elif (x2 < x1) and (y1 < y2):
                                    figuras1[i][1] = x1 + n
                                    figuras1[i][2] = y1 - n + 1
                                    figuras1[i][3] = x2 - n
                                    figuras1[i][4] = y2 + n + 1
                                    figuras1[i][5] = x3 - n
                                    figuras1[i][6] = y3 - n + 1


                            elif x1 == x2:
                                if (y1 > y2):
                                    figuras1[i][1] = x1 + 1
                                    figuras1[i][2] = y1 - n
                                    figuras1[i][3] = x2 + 1
                                    figuras1[i][4] = y2 + n
                                    figuras1[i][5] = x3 - n + 1
                                    figuras1[i][6] = y3
                                elif y2 > y1:
                                    figuras1[i][1] = x1 - 1
                                    figuras1[i][2] = y1 - n
                                    figuras1[i][3] = x2 - 1
                                    figuras1[i][4] = y2 + n
                                    figuras1[i][5] = x3 + n - 1
                                    figuras1[i][6] = y3

                            break
            else:
                print("No hay nada para mostrar")
        else:
            print("No hay figuras disponibles")

    elif decision1 == 'ROTATE':
        decision4 = int(input())
        decision5 = decision4 - 1
        decision6 = input()
        if len(figuras) > 0:
            if decision5 < 0 or decision5 > len(figuras):
                print("El número de figura es inválido")
                continue

            if figuras[decision5][1] == 'Círculo':
                print("CIRCULO")

                continue

            elif figuras[decision5][1] == 'Cuadrado':
                print("CUADRADO")
                if 1 <= decision4 <= len(figuras1):

                    for i in range(len(figuras1)):

                        if decision6 == '90' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int(-(y1 - (b / 2)) + (a / 2))
                            k = int((x1 - (a / 2)) + (b / 2))
                            l = int(-(y2 - (b / 2)) + (a / 2))
                            m = int((x2 - (a / 2)) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or \
                                    l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break


                            borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            cuadrado.Square.draw_square90(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)



                            figuras1[i][1] = j

                            figuras1[i][2] = k

                            figuras1[i][3] = l

                            figuras1[i][4] = m


                            # figuras.pop(decision3 - 1)
                            # figuras1.pop(decision3 - 1)

                            break
                        elif decision6 == '-90' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int((y1 - (b / 2)) + (a / 2))
                            k = int(-(x1 - (a / 2)) + (b / 2))
                            l = int((y2 - (b / 2)) + (a / 2))
                            m = int(-(x2 - (a / 2)) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or \
                                    l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            cuadrado.Square.draw_squareminus90(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            figuras1[i][1] = j

                            figuras1[i][2] = k

                            figuras1[i][3] = l

                            figuras1[i][4] = m

                            break

                        elif decision6 == '180' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int(-(x1 - (a / 2)) + (a / 2))
                            k = int(-(y1 - (b / 2)) + (b / 2))
                            l = int(-(x2 - (a / 2)) + (a / 2))
                            m = int(-(y2 - (b / 2)) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or \
                                    l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            cuadrado.Square.draw_square180(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            figuras1[i][1] = j

                            figuras1[i][2] = k

                            figuras1[i][3] = l

                            figuras1[i][4] = m

                            break
                        elif decision6 == '-180' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int((x1 - (a / 2)) + (a / 2))
                            k = int((y1 - (b / 2)) + (b / 2))
                            l = int((x2 - (a / 2)) + (a / 2))
                            m = int((y2 - (b / 2)) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or \
                                    l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            cuadrado.Square.draw_squareminus180(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            figuras1[i][1] = j

                            figuras1[i][2] = k

                            figuras1[i][3] = l

                            figuras1[i][4] = m

                            break
                        elif decision6 == '270' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]
                            b = figuras1[i][2] + figuras1[i][4]
                            j = int((y1 - (b / 2)) + (a / 2))
                            k = int(-(x1 - (a / 2)) + (b / 2))
                            l = int((y2 - (b / 2)) + (a / 2))
                            m = int(-(x2 - (a / 2)) + (b / 2))
                            if j < 1 or j > 20 or k < 1 or k > 20 or \
                                    l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break

                            borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            cuadrado.Square.draw_square270(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)

                            figuras1[i][1] = j

                            figuras1[i][2] = k

                            figuras1[i][3] = l

                            figuras1[i][4] = m
                            break
                        elif decision6 == '270' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]
                            b = figuras1[i][2] + figuras1[i][4]
                            j = int(-(y1 - (b / 2)) + (a / 2))
                            k = int((x1 - (a / 2)) + (b / 2))
                            l = int(-(y2 - (b / 2)) + (a / 2))
                            m = int((x2 - (a / 2)) + (b / 2))
                            if j < 1 or j > 20 or k < 1 or k > 20 or \
                                    l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break

                            borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)
                            cuadrado.Square.draw_squareminus270(figuras1[i][1], figuras1[i][2], figuras1[i][3],figuras1[i][4], matriz)

                            figuras1[i][1] = j

                            figuras1[i][2] = k

                            figuras1[i][3] = l

                            figuras1[i][4] = m
                            break




                else:
                    print("No hay nada que mostrar")

            elif figuras[decision5][1] == 'Línea':
                print("LINEA")
                if 1 <= decision4 <= len(figuras1):

                    for i in range(len(figuras1)):

                        if decision6 == '90' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            j = int(-(y1 - (b / 2)) + (a / 2))

                            k = int((x1 - (a / 2)) + (b / 2))

                            l = int(-(y2 - (b / 2)) + (a / 2))

                            m = int((x2 - (a / 2)) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break

                            borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            linea.Line.draw_line90(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)

                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            
                            figuras1[i][1] = int(-(y1 - (b / 2)) + (a / 2))

                            figuras1[i][2] = int((x1 - (a / 2)) + (b / 2))

                            figuras1[i][3] = int(-(y2 - (b / 2)) + (a / 2))

                            figuras1[i][4] = int((x2 - (a / 2)) + (b / 2))
                            """
                            break
                        elif decision6 == '-90' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int((y1 - (b / 2)) + (a / 2))

                            k = int(-(x1 - (a / 2)) + (b / 2))

                            l = int((y2 - (b / 2)) + (a / 2))

                            m = int(-(x2 - (a / 2)) + (b / 2))
                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            linea.Line.draw_lineminus90(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)

                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            figuras1[i][1] = int((y1 - (b / 2)) + (a / 2))

                            figuras1[i][2] = int(-(x1 - (a / 2)) + (b / 2))

                            figuras1[i][3] = int((y2 - (b / 2)) + (a / 2))

                            figuras1[i][4] = int(-(x2 - (a / 2)) + (b / 2))
                             """

                            break


                        elif decision6 == '180' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int(-(x1 - (a / 2)) + (a / 2))

                            k = int(-(y1 - (b / 2)) + (b / 2))

                            l = int(-(x2 - (a / 2)) + (a / 2))

                            m = int(-(y2 - (b / 2)) + (b / 2))
                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            linea.Line.draw_line180(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            figuras1[i][1] = int(-(x1 - (a / 2)) + (a / 2))

                            figuras1[i][2] = int(-(y1 - (b / 2)) + (b / 2))

                            figuras1[i][3] = int(-(x2 - (a / 2)) + (a / 2))

                            figuras1[i][4] = int(-(y2 - (b / 2)) + (b / 2))
                            """

                            break
                        elif decision6 == '-180' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int((x1 - (a / 2)) + (a / 2))

                            k = int((y1 - (b / 2)) + (b / 2))

                            l = int((x2 - (a / 2)) + (a / 2))

                            m = int((y2 - (b / 2)) + (b / 2))
                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            linea.Line.draw_line180(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            figuras1[i][1] = int((x1 - (a / 2)) + (a / 2))

                            figuras1[i][2] = int((y1 - (b / 2)) + (b / 2))

                            figuras1[i][3] = int((x2 - (a / 2)) + (a / 2))

                            figuras1[i][4] = int((y2 - (b / 2)) + (b / 2))
                            """

                            break
                        elif decision6 == '270' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int((y1 - (b / 2)) + (a / 2))

                            k = int(-(x1 - (a / 2)) + (b / 2))

                            l = int((y2 - (b / 2)) + (a / 2))

                            m =  int(-(x2 - (a / 2)) + (b / 2))
                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            linea.Line.draw_line270(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                    figuras1[i][5], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            figuras1[i][1] = int((y1 - (b / 2)) + (a / 2))

                            figuras1[i][2] = int(-(x1 - (a / 2)) + (b / 2))

                            figuras1[i][3] = int((y2 - (b / 2)) + (a / 2))

                            figuras1[i][4] = int(-(x2 - (a / 2)) + (b / 2))
                            """
                            break
                        elif decision6 == '-270' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            j = int(-(y1 - (b / 2)) + (a / 2))

                            k = int((x1 - (a / 2)) + (b / 2))

                            l = int(-(y2 - (b / 2)) + (a / 2))

                            m = int((x2 - (a / 2)) + (b / 2))
                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], matriz)
                            linea.Line.draw_lineminus270(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                    figuras1[i][5], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            """

                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            figuras1[i][1] = int(-(y1 - (b / 2)) + (a / 2))

                            figuras1[i][2] = int((x1 - (a / 2)) + (b / 2))

                            figuras1[i][3] = int(-(y2 - (b / 2)) + (a / 2))

                            figuras1[i][4] = int((x2 - (a / 2)) + (b / 2))
                            """
                            break




                else:
                    print("No hay nada que mostrar")



            elif figuras[decision5][1] == 'Triángulo':

                print("TRIANGULO")

                print(decision4)

                print(decision6)

                if 1 <= decision4 <= len(figuras1):

                    for i in range(len(figuras1)):

                        if decision6 == '90' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]



                            j = int(-(y1 - (b / 2)) + (a / 2))

                            k = int((x1 - (a / 2)) + (b / 2))

                            l = int(-(y2 - (b / 2)) + (a / 2))

                            m = int((x2 - (a / 2)) + (b / 2))

                            n =  int(-(y3 - (b / 2)) + (a / 2))

                            o = int((x3 - (a / 2)) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20 or n < 1 or n > 20 or o < 1 or o > 20:
                                print("Invalid operation")
                                break



                            borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],

                                                       figuras1[i][5], figuras1[i][6], matriz)

                            triangulo.Triangle.draw_triangle90(figuras1[i][1], figuras1[i][2], figuras1[i][3],
                                                               figuras1[i][4],

                                                               figuras1[i][5], figuras1[i][6], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            figuras1[i][5] = n
                            figuras1[i][6] = o

                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]



                            a = figuras1[i][1]  + figuras1[i][3]

                            b = figuras1[i][2]  + figuras1[i][4]

                            figuras1[i][1] = int(-(y1 - (b / 2)) + (a / 2))

                            figuras1[i][2] = int((x1 - (a / 2)) + (b / 2))

                            figuras1[i][3] = int(-(y2 - (b / 2)) + (a / 2))

                            figuras1[i][4] = int((x2 - (a / 2)) + (b / 2))

                            figuras1[i][5] = int(-(y3 - (b / 2)) + (a / 2))

                            figuras1[i][6] = int((x3 - (a / 2)) + (b / 2))


                            print(figuras1[i][1])

                            print(figuras1[i][2])

                            print(figuras1[i][3])

                            print(figuras1[i][4])

                            print(figuras1[i][5])

                            print(figuras1[i][6])
                            """

                            break

                        elif decision6 == '180' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            j = int(-(x1 - (a / 2)) + (a / 2))

                            k = int(-(y1 - (b / 2)) + (b / 2))

                            l = int(-(x2 - (a / 2)) + (a / 2))

                            m = int(-(y2 - (b / 2)) + (b / 2))

                            n = int(-(x3 - (a / 2)) + (a / 2))

                            o = int(-(y3 - (b / 2)) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20 or n < 1 or n > 20 or o < 1 or o > 20:
                                print("Invalid operation")
                                break

                            borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],

                                                       figuras1[i][5], figuras1[i][6], matriz)

                            triangulo.Triangle.draw_triangle180(figuras1[i][1], figuras1[i][2], figuras1[i][3],
                                                                figuras1[i][4],

                                                                figuras1[i][5], figuras1[i][6], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            figuras1[i][5] = n
                            figuras1[i][6] = o
                            """

                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]
                            figuras1[i][1] = int(-(x1 - (a / 2)) + (a / 2))

                            figuras1[i][2] = int(-(y1 - (b / 2)) + (b / 2))

                            figuras1[i][3] = int(-(x2 - (a / 2)) + (a / 2))

                            figuras1[i][4] = int(-(y2 - (b / 2)) + (b / 2))

                            figuras1[i][5] = int(-(x3 - (a / 2)) + (a / 2))

                            figuras1[i][6] = int(-(y3 - (b / 2)) + (b / 2))
                            """

                            break

                        elif decision6 == '270' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            j = int((y1 - (b / 2)) + (a / 2))

                            k = int(-(x1 - (a / 2)) + (b / 2))

                            l = int((y2 - (b / 2)) + (a / 2))

                            m = int(-(x2 - (a / 2)) + (b / 2))

                            n = int((y3 - (b / 2)) + (a / 2))

                            o = int(-(x3 - (a / 2)) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20 or n < 1 or n > 20 or o < 1 or o > 20:
                                print("Invalid operation")
                                break

                            borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],

                                                       figuras1[i][5], figuras1[i][6], matriz)

                            triangulo.Triangle.draw_triangle270(figuras1[i][1], figuras1[i][2], figuras1[i][3],
                                                                figuras1[i][4],

                                                                figuras1[i][5], figuras1[i][6], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            figuras1[i][5] = n
                            figuras1[i][6] = o
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            figuras1[i][1] = int((y1 - (b / 2)) + (a / 2))

                            figuras1[i][2] = int(-(x1 - (a / 2)) + (b / 2))

                            figuras1[i][3] = int((y2 - (b / 2)) + (a / 2))

                            figuras1[i][4] = int(-(x2 - (a / 2)) + (b / 2))

                            figuras1[i][5] = int((y3 - (b / 2)) + (a / 2))

                            figuras1[i][6] = int(-(x3 - (a / 2)) + (b / 2))
                            """

                            break
                        elif decision6 == '-90' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            j = int((y1 - (b / 2)) + (a / 2))
                            k = int(-x1 + (a / 2) + (b / 2))

                            l = int((y2 - (b / 2)) + (a / 2))

                            m = int(-x2 + (a / 2) + (b / 2))

                            n = int((y3 - (b / 2)) + (a / 2))
                            o = int(-x3 + (a / 2) + (b / 2))

                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20 or n < 1 or n > 20 or o < 1 or o > 20:
                                print("Invalid operation")
                                break


                            borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],

                                                       figuras1[i][5], figuras1[i][6], matriz)
                            triangulo.Triangle.draw_triangleminus90(figuras1[i][1], figuras1[i][2], figuras1[i][3],
                                                                figuras1[i][4],

                                                                figuras1[i][5], figuras1[i][6], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            figuras1[i][5] = n
                            figuras1[i][6] = o
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            figuras1[i][1] = int((y1 - (b / 2)) + (a / 2))
                            figuras1[i][2] = int(-x1 + (a / 2) + (b / 2))
                            figuras1[i][3] = int((y2 - (b / 2)) + (a / 2))
                            figuras1[i][4] = int(-x2 + (a / 2) + (b / 2))
                            figuras1[i][5] = int((y3 - (b / 2)) + (a / 2))
                            figuras1[i][6] = int(-x3 + (a / 2) + (b / 2))
                            """
                            break
                        elif decision6 == '-180' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            j = -(x1 - (a / 2)) + (a / 2)
                            k = -(y1 - (b / 2)) + (b / 2)

                            l = -(x2 - (a / 2)) + (a / 2)

                            m = -(y2 - (b / 2)) + (b / 2)

                            n = -(x3 - (a / 2)) + (a / 2)
                            o = -(y3 - (b / 2)) + (b / 2)

                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20 or n < 1 or n > 20 or o < 1 or o > 20:
                                print("Invalid operation")
                                break
                            borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],

                                                       figuras1[i][5], figuras1[i][6], matriz)

                            triangulo.Triangle.draw_triangleminus180(figuras1[i][1], figuras1[i][2], figuras1[i][3],
                                                               figuras1[i][4],

                                                               figuras1[i][5], figuras1[i][6], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            figuras1[i][5] = n
                            figuras1[i][6] = o
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            figuras1[i][1] = -(x1 - (a / 2)) + (a / 2)
                            figuras1[i][2] = -(y1 - (b / 2)) + (b / 2)
                            figuras1[i][3] = -(x2 - (a / 2)) + (a / 2)
                            figuras1[i][4] = -(y2 - (b / 2)) + (b / 2)
                            figuras1[i][5] = -(x3 - (a / 2)) + (a / 2)
                            figuras1[i][6] = -(y3 - (b / 2)) + (b / 2)
                            """
                            break
                        elif decision6 == '-270' and figuras1[i][0] == str(decision4):
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            j = int(-(y1 - (b / 2)) + (a / 2))
                            k = int((x1 - (a / 2)) + (b / 2))
                            l = int(-(y2 - (b / 2)) + (a / 2))

                            m = int((x2 - (a / 2)) + (b / 2))

                            n = int(-(y3 - (b / 2)) + (a / 2))
                            o = int((x3 - (a / 2)) + (b / 2))
                            if j < 1 or j > 20 or k < 1 or k > 20 or l < 1 or l > 20 or m < 1 or m > 20 or n < 1 or n > 20 or o < 1 or o > 20:
                                print("Invalid operation")
                                break

                            borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],

                                                       figuras1[i][5], figuras1[i][6], matriz)

                            triangulo.Triangle.draw_triangleminus270(figuras1[i][1], figuras1[i][2], figuras1[i][3],
                                                                figuras1[i][4],

                                                                figuras1[i][5], figuras1[i][6], matriz)
                            figuras1[i][1] = j
                            figuras1[i][2] = k
                            figuras1[i][3] = l
                            figuras1[i][4] = m
                            figuras1[i][5] = n
                            figuras1[i][6] = o
                            """
                            x1 = figuras1[i][1]
                            y1 = figuras1[i][2]
                            x2 = figuras1[i][3]
                            y2 = figuras1[i][4]
                            x3 = figuras1[i][5]
                            y3 = figuras1[i][6]

                            a = figuras1[i][1] + figuras1[i][3]

                            b = figuras1[i][2] + figuras1[i][4]

                            figuras1[i][1] = int(-(y1 - (b / 2)) + (a / 2))

                            figuras1[i][2] = int((x1 - (a / 2)) + (b / 2))

                            figuras1[i][3] = int(-(y2 - (b / 2)) + (a / 2))

                            figuras1[i][4] = int((x2 - (a / 2)) + (b / 2))

                            figuras1[i][5] = int(-(y3 - (b / 2)) + (a / 2))

                            figuras1[i][6] = int((x3 - (a / 2)) + (b / 2))
                            """

                            break
                    else:
                        print("El valor de decision4 está fuera del rango válido.")
                else:
                    print("El valor de decision4 está fuera del rango válido.")
            for i in range(len(figuras)):
                    if figuras[i][1] == "Cuadrado":
                        borrar.borrar.del_square(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4], matriz)
                        cuadrado.Square.draw_square(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                    matriz)
                    elif figuras[i][1] == "Círculo":
                        borrar.borrar.del_circle(figuras1[i][1], figuras1[i][2], figuras1[i][3], matriz)
                        circulo.Circle.draw_circle(figuras1[i][1], figuras1[i][2], figuras1[i][3], matriz)
                    elif figuras[i][1] == 'Línea':
                        borrar.borrar.del_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                               figuras1[i][5], matriz)
                        linea.Line.draw_line(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                             figuras1[i][5], matriz)
                    elif figuras[i][1] == "Triángulo":
                        borrar.borrar.del_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                   figuras1[i][5], figuras1[i][6], matriz)
                        triangulo.Triangle.draw_triangle(figuras1[i][1], figuras1[i][2], figuras1[i][3], figuras1[i][4],
                                                         figuras1[i][5], figuras1[i][6], matriz)
        else:
            print("No hay figuras para rotar")

    elif decision1 == "EXIT":
        break