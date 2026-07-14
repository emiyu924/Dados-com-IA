import requests as rq

nome = input("Bem vindo, por favor insira seu nome: ")

cep = input("Insira o seu CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/" 

dados = rq.get(url)
resposta = dados.json()


print(f" Olá {nome} Você mora na rua {resposta["logradouro"]} no bairro {resposta["bairro"]} na cidade de {resposta["localidade"]} no estado de {resposta["estado"]}")




