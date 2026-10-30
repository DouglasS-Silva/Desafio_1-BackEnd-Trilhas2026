# Desafio Nível 1 — PDV com Descontos (Python)

## O que o código faz

O `pdv.py` simula a lógica de um PDV (Ponto de Venda). Ele recebe o **preço unitário** do produto, a **quantidade de itens**, a **idade do cliente** e um **cupom** opcional. Com isso calcula o valor da compra (`preço unitário × quantidade`), aplica descontos progressivos (por idade, por valor, por quantidade e por cupom), mostra o valor final em reais e repete o processo para várias compras seguidas. Ao encerrar, exibe um resumo do dia com a quantidade de compras, o total bruto, o total de descontos e o total final, e salva esse resumo no arquivo `resumo.txt`.

## Sobre o preço unitário

Para que a quantidade de itens tenha efeito real no cálculo, o programa pede o preço unitário e calcula o valor da compra (subtotal) multiplicando pela quantidade. Assim, a regra do bônus “se for maior que 3, aplicar 5% extra” é aplicada em conjunto com os demais descontos.

> Detalhe: Para testar os casos do enunciado (que informam o valor total da compra), use **quantidade = 1**. Deixe o cupom em branco (Enter).

## Como ele faz

1. O código pede o **preço unitário**, a **quantidade de itens**, a **idade do cliente** e o **cupom** (opcional, basta apertar Enter para não usar).
2. Se o preço, a quantidade ou a idade forem negativos ou inválidos (e se a quantidade for menor que 1), mostra um aviso e pede novamente.
3. Calcula o subtotal: `preço unitário × quantidade`.
4. Verifica se a idade é **maior ou igual a 65**; se sim, aplica **20% de desconto**.
5. Depois verifica se o valor **já descontado pela idade** é **maior que 100 reais**; se sim, aplica mais **10% de desconto** sobre esse valor.
6. **Bônus 1:** se a quantidade de itens for **maior que 3**, aplica mais **5% de desconto**.
7. **Bônus 2:** se o cupom for `FIDELIDADE10`, aplica mais **10% de desconto**. Cupom inválido gera um aviso e nenhum desconto.
8. Arredonda para duas casas decimais e exibe o valor final no formato `R$ 144.00`.
9. Guarda cada compra (subtotal, desconto, valor final, quantidade e cupom) numa lista usando `.append()`.
10. O loop continua até o usuário digitar `0` no preço unitário.
11. Ao encerrar, percorre a lista com um `for`, soma tudo e mostra o resumo do dia.
12. **Bônus 3:** grava o resumo e a lista de compras no arquivo `resumo.txt` usando `open(..., "w")` e um `for`.

Os descontos são aplicados nesta ordem, sempre sobre o valor já descontado: idade → valor → quantidade → cupom.

## Como rodar

```
python pdv.py
```

## Tabela de exemplos

Regras básicas (quantidade 1, sem cupom, então preço unitário = valor da compra):

| Caso | Preço unit. | Idade | Valor final esperado | Observação                                  |
|------|-------------|-------|----------------------|---------------------------------------------|
| 1    | 50.00       | 30    | R$ 50.00             | sem nenhum desconto                         |
| 2    | 100.00      | 30    | R$ 100.00            | 100 não é maior que 100                     |
| 4    | 100.00      | 70    | R$ 80.00             | só desconto de idade                        |
| 5    | 125.00      | 70    | R$ 100.00            | 125 × 0.8 = 100, não é maior que 100        |
| 7    | 101.00      | 30    | R$ 90.90             | só desconto de valor                        |
| 8    | 200.00      | 65    | R$ 144.00            | 200 × 0.8 = 160, depois 160 × 0.9 = 144     |
| 10   | 200.00      | 64    | R$ 180.00            | idade 64: só desconto de valor              |

Exemplos com quantidade e cupom:

| Preço unit. | Qtd | Idade | Cupom          | Subtotal   | Valor final | Observação                                  |
|-------------|-----|-------|----------------|------------|-------------|---------------------------------------------|
| 80.00       | 1   | 65    | —              | R$ 80.00   | R$ 64.00    | só desconto de idade                        |
| 80.00       | 2   | 65    | —              | R$ 160.00  | R$ 115.20   | 160 → 128 → 115.20                          |
| 50.00       | 4   | 30    | —              | R$ 200.00  | R$ 171.00   | 200 → 180 → 171 (5% por quantidade)         |
| 40.00       | 5   | 65    | FIDELIDADE10   | R$ 200.00  | R$ 123.12   | 160 → 144 → 136.80 → 123.12                 |
| 12.50       | 4   | 30    | —              | R$ 50.00   | R$ 47.50    | só desconto por quantidade                  |
