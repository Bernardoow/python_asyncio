import random

def lancar_dados(n):
    print('Funcao iniciada')
    for i in range(0, n):
        print('entrou no for')
        yield random.randint(1,6)
        print('entrou no saiu')
    print('fim da funcao')

if __name__ == '__main__':
    for dado in lancar_dados(2):
        print(dado)