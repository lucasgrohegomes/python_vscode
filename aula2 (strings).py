faturamento = 1200
custo = 700
lucro = faturamento - custo
print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email_cliente = "lira@gmail.com"

# Maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)

# Minúscula
email_cliente = email_cliente.lower()
print(email_cliente)


# Verificar @
print(email_cliente.find("@")) # -1 quando não encontrar

# tamanho do texto
print(len(email_cliente)) # numero de carácteres

# pegar um caractere
print(email_cliente[0])

