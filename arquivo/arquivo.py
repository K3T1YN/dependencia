"""Escreva um programa de solicite a um dado
numero de entrevistados responder
perguntas de um questionário e escreva em
um arquivo os dados obtidos.
Em seguida leia os dados armazenados no
arquivo."""


with open ("arquivo.txt","a") as arquivo: 
     entrevista = str(input("Você nos ajudaria respondendo uma perguntas? [S/N]: ")).upper()
     


     if entrevista == "S":
        p1 = str(input("Qual seu nome?"))
        p2 = str(input("Qual sua idade?"))
        p3 = str(input("Quais são suas experiencias?"))
        p4 = str(input("Qual sua disponibilidade?"))
        arquivo.write(p1+"\n")
        arquivo.write(p2+"\n")
        arquivo.write(p3+"\n")
        arquivo.write(p4+"\n")
        arquivo.close()
     else:
        print("Certo, obrigada pela atenção.")

