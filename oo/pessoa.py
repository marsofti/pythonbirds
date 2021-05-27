class Pessoa:
    olhos = 2
    #metodo funcao pertence a classe
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    marcelo = Pessoa(nome='Marcelo')
    luciano = Pessoa(marcelo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(marcelo.__dict__)
    print(Pessoa.olhos)
    Pessoa.olhos = 3
    print(luciano.olhos)
    print(marcelo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(marcelo.olhos))








