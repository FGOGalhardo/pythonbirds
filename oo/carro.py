"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor;
2) Direção.

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade;
2) Método acelerar, que deverá incrementar a velocidade de uma unidade;
3) Método frear, que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste e Oeste;
2) Método virar_a_direita;
3) Método virar_a_esquerda.

  N
O   L
  S

   Exemplo:
   >>> # Testando motor
   >>> motor = Motor()
   >>> motor.velocidade
   0
   >>> motor.acelerar()
   >>> motor.velocidade
   1
   >>> motor.acelerar()
   >>> motor.velocidade
   2
   >>> motor.acelerar()
   >>> motor.velocidade
   3
   >>> motor.frear()
   >>> motor.velocidade
   1
   >>> motor.frear()
   >>> motor.velocidade
   0
   >>> # Testando direção
   >>> direcao = Direcao()
   >>> direcao.valor
   'Norte'
   >>> direcao.virar_a_direita()
   >>> direcao.valor
   'Leste'
   >>> direcao.virar_a_direita()
   >>> direcao.valor
   'Sul'
   >>> direcao.virar_a_direita()
   >>> direcao.valor
   'Oeste'
   >>> direcao.virar_a_direita()
   >>> direcao.valor
   'Norte'
   >>> direcao.virar_a_esquerda()
   >>> direcao.valor
   'Oeste'
   >>> direcao.virar_a_esquerda()
   >>> direcao.valor
   'Sul'
   >>> direcao.virar_a_esquerda()
   >>> direcao.valor
   'Leste'
   >>> direcao.virar_a_esquerda()
   >>> direcao.valor
   'Norte'
   >>> # Criando a instância carro.
   >>> carro = Carro(direcao, motor)
   >>> carro.calcular_velocidade()
   0
   >>> # Testando o motor do carro
   >>> carro.acelerar()
   >>> carro.calcular_velocidade()
   1
   >>> carro.acelerar()
   >>> carro.calcular_velocidade()
   2
   >>> carro.frear()
   >>> carro.calcular_velocidade()
   0
   >>> # Testando a direção do carro.
   >>> carro.calcular_direcao()
   'Norte'
   >>> carro.virar_a_direita()
   >>> carro.calcular_direcao()
   'Leste'
   >>> carro.virar_a_esquerda()
   >>> carro.calcular_direcao()
   'Norte'
   >>> carro.virar_a_esquerda()
   >>> carro.calcular_direcao()
   'Oeste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade <= 2:
            self.velocidade = 0
        else:
            self.velocidade -= 2


class Direcao:
    rotacao_a_direita_dct = {
        'Norte': 'Leste', 'Leste': 'Sul', 'Sul': 'Oeste', 'Oeste': 'Norte'
    }
    rotacao_a_esquerda_dct = {
        'Norte': 'Oeste', 'Oeste': 'Sul', 'Sul': 'Leste', 'Leste': 'Norte'
    }

    def __init__(self):
        self.valor = 'Norte'

    def virar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def virar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def virar_a_direita(self):
        self.direcao.virar_a_direita()

    def virar_a_esquerda(self):
        self.direcao.virar_a_esquerda()


motor = Motor()
direcao = Direcao()
carro = Carro(direcao, motor)

















