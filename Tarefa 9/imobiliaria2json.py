from xml.dom.minidom import parse
import json

# Faz o parse do XML
dom = parse("imobiliaria.xml")

# Elemento raiz
imobiliaria = dom.documentElement

# Lista de imóveis
imoveis_xml = imobiliaria.getElementsByTagName("imovel")

# Lista final para o JSON
imoveis_json = []

# Percorre cada imóvel
for imovel in imoveis_xml:

    descricao = imovel.getElementsByTagName("descricao")[0]\
        .firstChild.nodeValue

    valor = imovel.getElementsByTagName("valor")[0]\
        .firstChild.nodeValue

    # ENDEREÇO
    endereco = imovel.getElementsByTagName("endereco")[0]

    rua = endereco.getElementsByTagName("rua")[0]\
        .firstChild.nodeValue

    numero = endereco.getElementsByTagName("numero")[0]\
        .firstChild.nodeValue

    bairro = endereco.getElementsByTagName("bairro")[0]\
        .firstChild.nodeValue

    cidade = endereco.getElementsByTagName("cidade")[0]\
        .firstChild.nodeValue

    # CARACTERÍSTICAS
    caracteristica = imovel.getElementsByTagName("caracteristica")[0]

    tamanho = caracteristica.getElementsByTagName("tamanho")[0]\
        .firstChild.nodeValue

    quartos = caracteristica.getElementsByTagName("numQuartos")[0]\
        .firstChild.nodeValue

    banheiros = caracteristica.getElementsByTagName("numBanheiros")[0]\
        .firstChild.nodeValue

    # PROPRIETÁRIO
    proprietario = imovel.getElementsByTagName("proprietario")[0]

    nome = proprietario.getElementsByTagName("nome")[0]\
        .firstChild.nodeValue

    # Pode existir mais de um telefone
    telefones_xml = proprietario.getElementsByTagName("telefone")

    telefones = []

    for telefone in telefones_xml:
        telefones.append(telefone.firstChild.nodeValue)

    # Email pode não existir
    emails = proprietario.getElementsByTagName("Email")

    email = ""

    if len(emails) > 0:
        email = emails[0].firstChild.nodeValue

    # Cria o dicionário
    dados_imovel = {
        "descricao": descricao,
        "valor": valor,

        "endereco": {
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade
        },

        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": quartos,
            "numBanheiros": banheiros
        },

        "proprietario": {
            "nome": nome,
            "telefones": telefones,
            "email": email
        }
    }

    # Adiciona na lista final
    imoveis_json.append(dados_imovel)

# Salva o JSON
with open("imobiliaria.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(
        imoveis_json,
        arquivo_json,
        indent=4,
        ensure_ascii=False
    )

print("Arquivo imobiliaria.json criado com sucesso!")