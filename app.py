from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato


restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melância', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio
    
if __name__ == '__main__':
    main()