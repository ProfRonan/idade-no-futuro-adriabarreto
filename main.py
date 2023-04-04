#Recebe as informações do usuário:
nome = input("Digite seu nome: ")
idade = int(input("Qual a sua idade hoje? "))
anoatual = int(input("Em que ano estamos? "))
outroano = int(input("Digite outro ano: "))


#Idade no futuro
nascimento = int(anoatual-idade)
futuro = outroano-nascimento

print(f'{nome}, no ano de {outroano} você terá {futuro} anos.')