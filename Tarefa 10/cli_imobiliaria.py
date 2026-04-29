import json

with open("imobiliaria.json", "r", encoding="utf-8") as f:
    imoveis = json.load(f)


print("Bem-vindo à Imobiliária X!")
print("-" * 30)

for i, imovel in enumerate(imoveis, start=1):
    print(f"{i}. {imovel['descricao']} - R${imovel['valor']}")

opcao = int(input("Digite o número do imóvel que deseja ver os detalhes: "))

imovel_escolhido = imoveis[opcao - 1]

print("\nDetalhes do Imóvel:")
print(f"Descrição: {imovel_escolhido['descricao']}")
print(f"Valor: R${imovel_escolhido['valor']}")

print("\nEndereço:")
print(f"Rua: {imovel_escolhido['endereco']['rua']}")
print(f"Número: {imovel_escolhido['endereco']['numero']}")
print(f"Bairro: {imovel_escolhido['endereco']['bairro']}")
print(f"Cidade: {imovel_escolhido['endereco']['cidade']}")

print("\nCaracterísticas:")
print(f"Tamanho: {imovel_escolhido['caracteristicas']['tamanho']} m²")
print(f"Número de Quartos: {imovel_escolhido['caracteristicas']['numQuartos']}")
print(f"Número de Banheiros: {imovel_escolhido['caracteristicas']['numBanheiros']}")

print("\nProprietário:")
print(f"Nome: {imovel_escolhido['proprietario']['nome']}")
print("Telefones:")
for telefone in imovel_escolhido['proprietario']['telefones']:
    print(f"- {telefone}")
if imovel_escolhido['proprietario']['email']:
    print(f"Email: {imovel_escolhido['proprietario']['email']}")
    