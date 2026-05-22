import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def usu_lista():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter a lista de usuários: {response.status_code}")
        return []
    
def usu_detalhes(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter detalhes do usuário {user_id}: {response.status_code}")
        return None
    
def usu_criar(user_data):
    response = requests.post(BASE_URL, json=user_data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Erro ao criar usuário: {response.status_code}")
        return None
    
def usu_atualizar(user_id, user_data):
    url = f"{BASE_URL}/{user_id}"
    response = requests.put(url, json=user_data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao atualizar usuário {user_id}: {response.status_code}")
        return None
    
def usu_deletar(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        return True
    else:
        print(f"Erro ao deletar usuário {user_id}: {response.status_code}")
        return False
    
def listar_usuarios():
    url = f"{BASE_URL}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao listar usuários: {response.status_code}")
        return []