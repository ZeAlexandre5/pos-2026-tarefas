from xml.dom.minidom import parse

dom = parse('cardapio.xml')

cardapio = dom.documentElement
pratos = dom.getElementsByTagName('prato')

id_prato = 0

for prato in pratos:
    id_prato = prato.getElementsByTagName('id')[0].firstChild.data
    nome = prato.getElementsByTagName('nome')[0].firstChild.data
    print(f"{id_prato}: {nome}")


id_escolhido = int(input("Digite o ID do prato que deseja escolher: "))
prato = pratos[id_escolhido - 1]
print("---\n")

nome = prato.getElementsByTagName('nome')[0].firstChild.data
descricao = prato.getElementsByTagName('descricao')[0].firstChild.data  
preco = prato.getElementsByTagName('preco')[0].firstChild.data
calorias = prato.getElementsByTagName('calorias')[0].firstChild.data
tempo_preparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.data
print(f"Prato: {nome}")
print(f"Descrição: {descricao}")
print(f"Preço: R${preco}")
print(f"Calorias: {calorias} kcal")
print(f"Tempo de Preparo: {tempo_preparo}")