from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Listar pessoas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar pessoas
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('Digite uma opção válida!')
    sleep(2)

