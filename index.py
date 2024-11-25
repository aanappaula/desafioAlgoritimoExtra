# Aluna: Ana Paula de Souza

# Faça um programa que retorne a pontuação de uma senha, podendo assim ser avaliada se é forte ou não. Utilize a tabela de resultado abaixo para informar ao usuário se a senha escolhida é muito fraca, fraca, boa, forte ou muito forte.

# Regras da pontuação:
# - Adições (soma pontos):
# Número de caracteres * 4
# Maiúsculas: (Número de caracteres - maiúsculas) * 2
# Minúsculas: (Número de caracteres - minúsculas) * 2
# Números: número de dígitos * 4 ?
# Símbolos: número de símbolos * 6
# Numeros e símbolos no meio da senha: número * 2
# Regras extras: número de regras atendidas * 2
# Mínimo 8 caracteres ?
# 3/4 de maiúsculas ou minúsculas ou números ou símbolos ?

# - Deduções (reduz pontos):
# Somente letras: número de letras
# Somente números: número de dígitos
# Caracteres repetidos (insensível ao case): número de repetidos
# Maiúsculas repetidas consecutivamente: maiúsculas repetidas * 2
# Minúsculas repetidas consecutivamente: minúsculas repetidas * 2
# Números consecutivos: consecutivos * 2
# Letras sequenciais (ex: abc) (>3): (caracteres na sequência - 2) * 3
# Números sequenciais (ex: 123) (>3): (caracteres na sequências - 2) * 3
# Símbolos sequenciais (ex: !@#) (>3): (caracteres na sequências - 2) * 3

# - Resultado:
# Pontuação < 20): "Muito fraca"
# 20 <= Pontuação < 40): "Fraca"
# 40 <= Pontuação < 60): "Boa"
# 60 <= Pontuação < 80): "Forte"
# 80 <= Pontuação: "Muito forte"


while True:
    print("Olá, seja bem-vindo ao nosso classificador de senhas! Vamos começar:")
    senha = input("Digite a sua senha: ")

    def verificaSpace():
        for i in range(len(senha)):
            if senha[i].isspace():
                return True
        return False

    def qtdCaracter():
        totalCaracter = len(senha)
        return totalCaracter

    def isMinuscula():
        totalMinuscula = 0
        for i in range(len(senha)):
            if senha[i].islower():
                totalMinuscula += 1
        return totalMinuscula

    def isMaiuscula():
        totalMaiuscula = 0
        for i in range(len(senha)):
            if senha[i].isupper():
                totalMaiuscula += 1
        return totalMaiuscula

    def isNumber():
        totalNumber = 0
        for i in range(len(senha)):
            if senha[i].isnumeric():
                totalNumber += 1
        return totalNumber

    def isSymbol():
        totalSymbol = 0
        for i in range(len(senha)):
            if not senha[i].isalnum():
                totalSymbol += 1
        return totalSymbol

    def meioNumberOrSymbol():
        totalNumberOrSymbol = 0
        for i in range(1, len(senha) - 1):
            if not senha[i].isalnum() or senha[i].isnumeric():
                totalNumberOrSymbol += 1
        return totalNumberOrSymbol

    def tresQuartos():
        limite75 = len(senha) * 0.75

        if (
            isMaiuscula() >= limite75
            or isMinuscula() >= limite75
            or isNumber() >= limite75
            or isSymbol() >= limite75
        ):
            return True

    def regrasAtentidas():
        totalRegras = 0
        if qtdCaracter() > 0:
            totalRegras += 1
        if isMaiuscula() > 0:
            totalRegras += 1
        if isMinuscula() > 0:
            totalRegras += 1
        if isNumber() > 0:
            totalRegras += 1
        if isSymbol() > 0:
            totalRegras += 1
        if meioNumberOrSymbol() > 0:
            totalRegras += 1
        if tresQuartos() is True:
            totalRegras += 1
        if len(senha) > 8:
            totalRegras += 1
        return totalRegras

    def adicoes():
        maiusculaPontos = (qtdCaracter() - isMaiuscula()) * 2
        minusculaPontos = (qtdCaracter() - isMinuscula()) * 2
        pontos = (
            (qtdCaracter() * 4)
            + maiusculaPontos
            + minusculaPontos
            + (isNumber() * 4)
            + (isSymbol() * 6)
            + (meioNumberOrSymbol() * 2)
            + (regrasAtentidas() * 2)
        )
        return pontos

    def isLetra():
        letras = 0
        for i in range(len(senha)):
            if senha[i].isalpha:
                letras += 1
        return letras

    def somenteLetras():
        if isLetra() == len(senha):
            return len(senha)
        else:
            return 0

    def somenteNumero():
        if isNumber() == len(senha):
            return len(senha)
        else:
            return 0

    def caracterRepetido():
        repetidos = 0
        for i in range(len(senha) - 1):
            if senha[i].lower() == senha[i + 1].lower():
                repetidos += 1
        return repetidos

    def maiusculasRepetido():
        repetidos = 0
        for i in range(len(senha) - 1):
            if senha[i].isupper() and senha[i] == senha[i + 1]:
                repetidos += 1
        return repetidos * 2 

    def minusculasRepetido():
        repetidos = 0
        for i in range(len(senha) - 1):
            if senha[i].islower() and senha[i] == senha[i + 1]:
                repetidos += 1
        return repetidos * 2

    def numerosConsecutivos():
        total = 0
        tamanho_seq = 1
        for i in range(len(senha) - 1):
            if senha[i].isdigit() and senha[i+1].isdigit() and int(senha[i+1]) == int(senha[i]) + 1:
                tamanho_seq += 1
            else:
                if tamanho_seq >= 2:
                    total += tamanho_seq * 2
                tamanho_seq = 1
        if tamanho_seq >= 2: 
            total += tamanho_seq * 2
        return total

    def letrasSequenciais():
        total = 0
        tamanho_seq = 1
        for i in range(len(senha) - 1):
            if senha[i].isalpha() and ord(senha[i+1]) == ord(senha[i]) + 1:
                tamanho_seq += 1
            else:
                if tamanho_seq > 3:
                    total += (tamanho_seq - 2) * 3
                tamanho_seq = 1
        if tamanho_seq > 3: 
            total += (tamanho_seq - 2) * 3
        return total
    
    def numerosSequenciais() -> int:
        total = 0
        tamanho_seq = 1
        for i in range(len(senha) - 1):
            if senha[i].isdigit() and senha[i+1].isdigit() and int(senha[i+1]) == int(senha[i]) + 1:
                tamanho_seq += 1
            else:
                if tamanho_seq > 2:
                    total += (tamanho_seq - 2) * 3
                tamanho_seq = 1
        if tamanho_seq > 2:
            total += (tamanho_seq - 2) * 3
        return total

    def simbolosSequenciais():
        total = 0
        tamanho_seq = 1
        for i in range(len(senha) - 1):
            if not senha[i].isalnum() and ord(senha[i+1]) == ord(senha[i]) + 1:
                tamanho_seq += 1
            else:
                if tamanho_seq > 3:
                    total += (tamanho_seq - 2) * 3
                tamanho_seq = 1
        if tamanho_seq > 3: 
            total += (tamanho_seq - 2) * 3
        return total

    def deducoes() -> int:
        total = (
            somenteLetras()
            + somenteNumero()
            + caracterRepetido()
            + maiusculasRepetido()
            + minusculasRepetido()
            + numerosConsecutivos()
            + letrasSequenciais()
            + numerosSequenciais()
            + simbolosSequenciais()
        )
        return total

    def pontuacao():
        total = adicoes() - deducoes()
        if total < 20:
            print("Muito fraca, o seu total de pontos foi: ", total)
        elif total >= 20 and total < 40:
            print("Fraca, o seu total de pontos foi: ", total)
        elif total >= 40 and total < 60:
            print("Boa, o seu total de pontos foi: ", total)
        elif total >= 60 and total < 80:
            print("Muito boa, o seu total de pontos foi: ", total)
        elif total >= 80:
            print("Muito forte, o seu total de pontos foi: ", total)

    if verificaSpace():
        print("A senha não deve conter espaços em branco. Tente novamente!")
        continue
    else:
        pontuacao()
        pergunta = input("Deseja classificar uma nova senha? Digite S para sim e N para não ")
        if pergunta == 'S' or pergunta == "s":
            continue
        else:
            break
