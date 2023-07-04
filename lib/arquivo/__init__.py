from lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        ('Houve um ERRO na criação do arquivp')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:3>} anos')
    finally:
        a.close()


def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao adicionar os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
