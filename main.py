#Recebe as informações do usuário:
nome = str(input("Digite seu nome: "))
idade = int(input("Qual a sua idade hoje? "))
anoatual = int(input("Em que ano estamos? "))
outroano = int(input("Digite outro ano: "))


#Idade no futuro
idadefutura = int(outroano-(anoatual-idade))


print(f'{nome}, no ano de {outroano} você terá {idadefutura} anos.')