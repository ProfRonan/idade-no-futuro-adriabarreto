#Recebe as informações do usuário:
anoatual = int(input("Em que ano estamos? "))
idade = int(input("Qual a sua idade hoje? "))
outroano = int(input("Digite outro ano: "))
nome = str(input("Digite seu nome: "))

#Idade no futuro
idadefutura = int(outroano-(anoatual-idade))


print(f'{nome}, no ano de {outroano} você terá {idadefutura} anos')