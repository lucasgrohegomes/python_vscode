faturamento = 1200
custo = 750.0

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1
lucro = faturamento - custo - imposto

margem_lucro = lucro / faturamento

print("Faturamento foi de {}".format(faturamento))
print("O custo foi de {}".format(custo))
print("O lucro foi de {}".format(lucro))
print("A margem de lucro foi de {}".format(round(margem_lucro, 3)))