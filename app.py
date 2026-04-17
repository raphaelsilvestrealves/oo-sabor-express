from models.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Laís', 8)
restaurante_praca.receber_avaliacao('Emy', 2)


def main():
    Restaurante.listar_restaurantes()
    pass

if __name__ == '__main__':
    main()