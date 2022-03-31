import matplotlib.pyplot as plt

def punto_de_mira():
    plt.plot([0], [0], 'k+')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()
    print("Hola Punto de mira")

if __name__ == '__main__':
    punto_de_mira()
