# Exercício 8.13

def build_profile(nome, sobrenome, **user_info):
    profile = {}
    profile['Nome'] = nome
    profile['Sobrenome'] = sobrenome
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Ana','Ribeiro',location='Belo Horizonte',field='Engenharia Mecânica',age=37)
print(user_profile)
