# O que tem que fazer?
# -começar a escrever tentativas:
# -Começando com 1 caracter, do 1° até a última letra
# -Depois caracter+=1
# -caracter 1+caracter1
# -caracter 1+caracter2
# -caracter 1+caracter3...

print(
    "░██╗░░░░░░░██╗██╗░░██╗░█████╗░░█████╗░███╗░░░███╗░░░░░░██╗\n░██║░░██╗░░██║██║░░██║██╔══██╗██╔══██╗████╗░████║░░░░░░██║\n░╚██╗████╗██╔╝███████║██║░░██║███████║██╔████╔██║█████╗██║\n░░████╔═████║░██╔══██║██║░░██║██╔══██║██║╚██╔╝██║╚════╝██║\n░░╚██╔╝░╚██╔╝░██║░░██║╚█████╔╝██║░░██║██║░╚═╝░██║░░░░░░██║\n░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░░╚═╝")
print(
    "==========Bem vindo ao wordListGenerator!==========\n*Responda com n ou y*\nDeseja passar algum parâmetro inicial?")
preWord = input()
if preWord == "y":
    print("Digite os parâmetros os dividindo por vírgula:")  # A fazer isso ******
    parameter = input()
else:
    print("Deseja tentativas incluindo Upper Case na primera letra?")  # A fazer isso ******
    uppCase = input()
print("Deseja tentativas com numeros?")
nums = input()
print("Deseja tentativas incluindo cacteres especiais?")
espCarac = input()
print("Insira o numero de caracteres mínimo:")
minCarac = input()
print("Insira o numero de caracteres máximo:")
maxCarac = input()

caracTemp = []  # var temporária para guardar valores do input
i = 10
while i <= 35:
    caracTemp.append(i)
    i += 1
print(caracTemp)
if (nums == "y"):
    caracTemp.insert(0, 0)
    i = 1
    while i <= 9:
        caracTemp.insert(i, i)
        i += 1
if (espCarac == "y"):
    i = 36
    while i <= 41:
        caracTemp.append(i)
        i += 1

with open('payload.txt', 'r') as file:
    lines = file.read().split("\n")
    i = 0
    caracFinal = []
    while i < len(caracTemp):  # compara a temp com o txt payload e daí coloca os
        caracFinal.append(lines[caracTemp[i]])
        i += 1
    print(caracFinal)

wordlist = []
end = 0
index = 0
numCarac = minCarac
while end <= len(caracFinal)**maxCarac:
    wordlist.append()


def wordlist():
    with open('wordlist.txt', 'r') as file:
        file.write(wordlist)

# def payload():
#      with open('payload.txt','r') as file:
#          lines = file.read().split("\n")
#       string = []
#     for line in lines:
#           line = line.replace('-\n','')
#           string.append(line)
#     return (' '.join(string))
# def wordlist():
#      with open('payload.txt','r') as file:
#          lines = file.read().split("\n")
#       string = []
#     for line in lines:
#           line = line.replace('-\n','')
#           string.append(line)
#     return (' '.join(string))


# def file_string():
#     with open('speech.txt','r') as file:
#         lines = file.read().split("\n")
#      string = []
#      for line in lines:
#          line = line.replace('-\n','')
#          string.append(line)
#      return (' '.join(string))

# print(file_string())
