# Faça um programa que calcule o retorno de um investimento financeiro
# fazendo as contas mês a mês, sem usar a fórmula de juros compostos

# 1. O usuário deve informar quanto será investido por mês e qual será
# a taxa de juros mensal
# 2. O programa deve informar o saldo do investimento após um ano (soma das
# aplicações mês a mês considerando os juros compostos) e perguntar se o
# usuário deseja calcular o do ano seguinte, sucessivamente
# Exemplo: R$ 100,00 ao mês com uma taxa de 1% => saldo R$ 1268,25

# @author = Fernando
# @date = 07/09/2019

div = ('=' * 60)
print("\n" + div + "\n")
print("{:^60}".format("Cálculo do rendimento anual por juros compostos"))
print("\n" + div + "\n")

def rendimento_mensal(montante, juros_mensal):
    return montante * juros_mensal

def rendimento_anual(investimento, aporte_mensal, juros_mensal, anos):
    for mes in range(12 * anos):
        investimento += aporte_mensal + rendimento_mensal(investimento, juros_mensal)
    else:
        print("Ao final de um ano teremos o valor de: R$" + str(investimento))

aporte_mensal = float(input("> Digite o valor do aporte mensal: R$"))
juros_mensal = float(input("> Digite o valor do rendimento mensal (em %): "))

investimento = 0
rendimento_anual(investimento, aporte_mensal, juros_mensal / 100, 1)