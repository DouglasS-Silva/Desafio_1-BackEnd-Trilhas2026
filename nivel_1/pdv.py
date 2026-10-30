# PDV com Descontos - Desafio Nível 1 (com bônus e preço unitário)
# O valor da compra é calculado pelo sistema: preço unitário x quantidade

compras = []  # cada item: [subtotal, desconto, valor_final, quantidade, cupom]

print("")
print(">>> PDV - Ponto de Venda (preço unitário) <<<")
print("Digite 0 no preço unitário para encerrar. \n")


while True:
    # ---- Entrada do preço unitário ----
    while True:
        texto = input("Preço unitário (R$): ").strip().replace(",", ".")
        negativo = texto.startswith("-")
        corpo = texto[1:] if negativo else texto
        if corpo.replace(".", "", 1).isdigit():
            preco = float(texto)
            if preco < 0:
                print("Aviso: o preço não pode ser negativo. Tente novamente.")
            else:
                break
        else:
            print("Aviso: digite um número válido. Tente novamente.")

    # Encerra o loop quando o preço for 0
    if preco == 0:
        break

    # ---- Entrada da quantidade (com validação) ----
    while True:
        texto = input("Quantidade de itens: ").strip()
        if texto.startswith("-") and texto[1:].isdigit():
            print("Aviso: a quantidade não pode ser negativa. Tente novamente.")
        elif texto.isdigit():
            quantidade = int(texto)
            if quantidade < 1:
                print("Aviso: a quantidade deve ser pelo menos 1.")
            else:
                break
        else:
            print("Aviso: digite uma quantidade válida (número inteiro). Tente novamente.")

    # ---- Entrada da idade ----
    while True:
        texto = input("Idade do cliente: ").strip()
        if texto.startswith("-") and texto[1:].isdigit():
            print("Aviso: a idade não pode ser negativa. Tente novamente.")
        elif texto.isdigit():
            idade = int(texto)
            break
        else:
            print("Aviso: digite uma idade válida (número inteiro). Tente novamente.")

    # ---- Cupom de fidelidade (Enter = sem cupom) ----
    cupom = input("Cupom de fidelidade (Enter se não tiver): ").strip().upper()

    # ---- Subtotal ----
    valor = round(preco * quantidade, 2)
    print(f"Subtotal: R$ {valor:.2f} ({quantidade} x R$ {preco:.2f})")

    # ---- Regras de desconto ----
    valor_atual = valor

    # Regra 1: desconto por idade (>= 65 anos -> 20%)
    if idade >= 65:
        valor_atual = round(valor_atual * 0.8, 2)

    # Regra 2: desconto por valor (> 100 já com desconto de idade -> 10% extra)
    if valor_atual > 100:
        valor_atual = round(valor_atual * 0.9, 2)

    # Bônus 1: desconto por quantidade (> 3 itens -> 5% extra)
    if quantidade > 3:
        valor_atual = round(valor_atual * 0.95, 2)

    # Bônus 2: cupom de fidelidade (FIDELIDADE10 -> 10% extra)
    if cupom == "FIDELIDADE10":
        valor_atual = round(valor_atual * 0.9, 2)
    elif cupom != "":
        print("Aviso: cupom inválido, nenhum desconto de cupom aplicado.")
        cupom = ""

    valor_final = valor_atual
    desconto = round(valor - valor_final, 2)

    print(f"Valor final: R$ {valor_final:.2f}\n")

    compras.append([valor, desconto, valor_final, quantidade, cupom])

# ---- Resumo do dia ----
total_bruto = 0
total_descontos = 0
total_final = 0

for compra in compras:
    total_bruto += compra[0]
    total_descontos += compra[1]
    total_final += compra[2]

print("\n>>> RESUMO DO DIA <<<")
print(f"Quantidade de compras: {len(compras)}")
print(f"Total bruto:           R$ {total_bruto:.2f}")
print(f"Total de descontos:    R$ {total_descontos:.2f}")
print(f"Total final:           R$ {total_final:.2f}")

# ---- Salvar o resumo em resumo.txt ----
arquivo = open("resumo.txt", "w", encoding="utf-8")
arquivo.write("=== RESUMO DO DIA ===\n")
arquivo.write(f"Quantidade de compras: {len(compras)}\n")
arquivo.write(f"Total bruto:           R$ {total_bruto:.2f}\n")
arquivo.write(f"Total de descontos:    R$ {total_descontos:.2f}\n")
arquivo.write(f"Total final:           R$ {total_final:.2f}\n")
arquivo.write("\n--- Compras registradas ---\n")

numero = 1
for compra in compras:
    linha = f"{numero}. Subtotal: R$ {compra[0]:.2f} | Desconto: R$ {compra[1]:.2f} | Final: R$ {compra[2]:.2f} | Itens: {compra[3]}"
    if compra[4] != "":
        linha += f" | Cupom: {compra[4]}"
    arquivo.write(linha + "\n")
    numero += 1

arquivo.close()
print("\nResumo salvo em resumo.txt")
