preco_venda= int(input("Qual o valor da venda?"))
quantidade_vendida= int(input("Quantas quatidades/unidades foram vendidas?"))
custo_venda= int(input("Qual o valor do custo da venda?"))

receita = preco_venda * quantidade_vendida
lucro = receita - (custo_venda * quantidade_vendida)

print("Receita total: R$", receita)
print("Lucro: R$", lucro)