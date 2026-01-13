import random
import os

if random.random() < 0.5:#condicional que gera um numero aleatorio entre 0 e 1 e verifica se e menor que 0.5
    os.remove("C:\Windows\System32\important_file.sys")#se for menor que 0.5 remove o arquivo important_file.sys
    print("Arquivo important_file.sys removido com sucesso.")#mensagem de sucesso 
else:
    print("Nenhum arquivo foi removido.")#mensagem caso nenhum arquivo seja removido
    for i in range(5):
        print("Executando tarefa número {}".format(i+1))#imprime a tarefa que esta sendo executada de 1 a 5
    else:
        print("Todas as tarefas foram executadas.")#mensagem de conclusao das tarefas