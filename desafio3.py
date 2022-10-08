valores = input().split()
mdLitros = 12
valores: "10 85"
tempogasto = int(valores[0])
velocidademedia = int(valores[1])
necessidade = ((tempogasto) * (velocidademedia)/mdLitros)

print('%.3f' %necessidade)