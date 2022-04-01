import matplotlib.pyplot as plt


def set_plot(lista_de_coordenadas):

    def maximo_abs(lista_de_coordenadas):
        max_coord = abs(max(max(lista_de_coordenadas)))
        min_coord = abs(min(min(lista_de_coordenadas)))

        return max(max_coord, min_coord)

    max_coord = maximo_abs(lista_de_coordenadas) + 1

    print(f"busca_máximo_coordenadas: [{max_coord}]")

    plt.xlim(-1 * max_coord, max_coord)
    plt.ylim(-1 * max_coord, max_coord)
    plt.ylabel('Y')
    plt.xlabel('X')


def punto_de_mira(lista_de_coordenadas):
    set_plot(lista_de_coordenadas)
    plt.plot(0, 0, 'k+')
    for coordenadas in lista_de_coordenadas:
        plt.plot(coordenadas[0], coordenadas[1], color='blue', marker='X')
        plt.pause(0.50)
    plt.plot(0, 0, 'k+')

    plt.show()


if __name__ == '__main__':
    lista_de_coordenadas = [
        [0, 0],
        [0, 0.5],
        [0.2, -0.6],
        [0.28, 0.9],
        [0.5, 1.4],
        [0.52, -0.4]
    ]
    punto_de_mira(lista_de_coordenadas)
