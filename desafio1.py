from tokenize import Double
entrada = input().split()

distancia= (entrada[0])
diametr01= (entrada[1])
diametr02= (entrada[2])
imc_calc = (int(entrada[0]))/(int(entrada[1])+int(entrada[2]))
print(f"Valor de IMC: {imc_calc:10.2f}")