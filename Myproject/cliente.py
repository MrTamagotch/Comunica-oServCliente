import requests

# URL do servidor
url = 'http://localhost:5000/data'

# Dados para enviar
mensagem = {"mensagem": "Olá!"}

# Enviar a requisição POST
response = requests.post(url, json=mensagem)

# Exibir a resposta do servidor
print(f"Resposta do servidor: {response.json()}")
