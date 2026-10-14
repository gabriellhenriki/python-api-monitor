import requests

def buscar_usuario(user):
    try:
        #Timeout inserido, se a conexão ficar travada por mais de 10 segundos, o requests gera uma exceção e cai no except.
        response = requests.get(
            f"https://api.github.com/users/{user}",
            timeout=10
            )
        if response.status_code == 200:
                dados = response.json()
                return dados
                
        elif response.status_code == 404:
            return None
        else:
            return None
    except requests.exceptions.RequestException:
        return None