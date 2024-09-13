import requests
"""sistema de comsulta de cep simples utilizando 'viacep'"""
while True:
    cep = input('digite CEP: ').strip()
    url = f'http://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    if resposta.status_code == 200:
     dados_cep = resposta.json()
     if 'erro' in dados_cep:
        print('cep nao encontrado, certifique que o numero esteja correto')
     else:
        print('requisição OK!')
        print(dados_cep['bairro'])
        print(dados_cep['localidade'])
        print(dados_cep['uf'])
        print(dados_cep['regiao'])
        break
    else:
       print('erro de requisição:', resposta.status_code)
       print('tente novamente')