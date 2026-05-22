import request

url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso'

codigo = input('Digite o código do país: ')
operacao = input('Digite a operação (telefone 1, moeda 2 ou nome 3): ')
telefone = "CountryIntPhoneCode"
moeda = "CountryCurrency"
nome = "CountryName"
if operacao == "1":
    funcao = telefone
elif operacao == "2":
    funcao = moeda
elif operacao == "3":
    funcao = nome
else:
    print("Operação inválida!")
    exit()


payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <{funcao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>string</sCountryISOCode>
    </{funcao}>
  </soap:Body>
</soap:Envelope>"""


headers = {
    'Content-Type': 'text/xml; charset=utf-8',
}



response = requests.post(url, headers=headers, data=payload)

dom = parse