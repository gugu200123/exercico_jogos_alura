import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")



    arquivo = open("palavras.txt","r")
    palavras = []
    for linha in arquivo:
        linha=linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    acertou = False
    enforcou = False
    tentativa = 0
    print(letras_acertadas)

    while not acertou and not enforcou:

        chute = input("Qual letra ?")
        chute = chute.strip().upper()

        if chute in palavra_secreta:

            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra

                posicao += 1
        else:
            tentativa += 1
            print("Você errou, faltam {} tentativas".format(7-tentativa))
        acertou = "_" not in letras_acertadas
        enforcou = tentativa == 7

        print(letras_acertadas)
    if acertou:
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!! A palavra era {}".format(palavra_secreta) )
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
