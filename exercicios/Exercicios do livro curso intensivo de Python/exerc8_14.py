# Exercício 8.14

def make_car(fabricante, modelo, **car_info):
    profile = {}
    profile['Fabricante'] = fabricante
    profile['Modelo'] = modelo
    for key, value in car_info.items():
        profile[key] = value
    return profile


car_profile = make_car('subaru','outback',color='blue',tow_package=True)
print(car_profile)