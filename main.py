from api_client import buscar_usuario

user = input('Digite o nome do usuário no Github: ').strip().lower()
resultado = buscar_usuario(user)
if resultado is not None:
    print("Nome:", resultado["name"])
    print("Usuário:", resultado["login"])
    print("Seguidores:", resultado["followers"])
    print("Repositórios públicos:", resultado["public_repos"])
else:
     print('Não foi possível obter os dados do usuário.')



